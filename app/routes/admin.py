from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.auth.security import create_csrf_token, require_csrf, require_superuser
from app.database import get_db
from app.models import (
    ActivityLog,
    Achievement,
    Certificate,
    ContactMessage,
    Education,
    Experience,
    MediaFile,
    ProfileInformation,
    Project,
    Service,
    Skill,
    SocialLink,
    Testimonial,
    User,
)
from app.routes.resources import RESOURCES, apply_search, coerce_value
from app.templating import templates
from app.utils.files import save_upload


router = APIRouter(prefix="/admin", dependencies=[Depends(require_superuser), Depends(require_csrf)])


def add_activity(db: Session, user: User, action: str, entity_type: str, entity_id: int | None = None):
    db.add(ActivityLog(user_id=user.id, action=action, entity_type=entity_type, entity_id=entity_id))


def admin_context(request: Request, **extra):
    context = {"request": request, "resources": RESOURCES, "csrf_token": request.cookies.get("csrf_token") or create_csrf_token()}
    context.update(extra)
    return context


@router.get("", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    counts = {
        "Projects": db.query(Project).count(),
        "Certificates": db.query(Certificate).count(),
        "Skills": db.query(Skill).count(),
        "Experiences": db.query(Experience).count(),
        "Education Records": db.query(Education).count(),
        "Testimonials": db.query(Testimonial).count(),
        "Achievements": db.query(Achievement).count(),
    }
    recent = db.query(ActivityLog).order_by(ActivityLog.created_at.desc()).limit(8).all()
    messages = db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).limit(5).all()
    response = templates.TemplateResponse("admin/dashboard.html", admin_context(request, title="Dashboard", counts=counts, recent=recent, messages=messages))
    if not request.cookies.get("csrf_token"):
        response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
    return response


@router.get("/profile", response_class=HTMLResponse)
def edit_profile(request: Request, db: Session = Depends(get_db)):
    profile = db.query(ProfileInformation).first()
    fields = [
        "full_name", "professional_title", "contact_email", "phone_number", "address", "location", "website_url",
        "linkedin_url", "github_url", "twitter_url", "instagram_url", "footer_information", "hero_heading",
        "hero_subheading", "hero_description", "cta_primary_label", "cta_primary_url", "cta_secondary_label",
        "cta_secondary_url", "about_heading", "about_content", "about_me", "biography", "personal_details",
        "years_experience", "education_summary", "career_summary", "working_hours",
    ]
    return templates.TemplateResponse("admin/profile_form.html", admin_context(request, title="Profile", profile=profile, fields=fields))


@router.post("/profile")
async def update_profile(request: Request, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    form = await request.form()
    profile = db.query(ProfileInformation).first()
    for key, value in form.items():
        if key.startswith("_") or key in {"profile_photo", "resume_pdf", "portfolio_logo", "hero_background_image", "hero_profile_image"}:
            continue
        if hasattr(profile, key):
            setattr(profile, key, value)
    for upload_field in ["profile_photo", "resume_pdf", "portfolio_logo", "hero_background_image", "hero_profile_image"]:
        upload = form.get(upload_field)
        if isinstance(upload, UploadFile) and upload.filename:
            path, _, _ = save_upload(upload, "profile")
            setattr(profile, upload_field, path)
            if upload_field == "resume_pdf":
                profile.cta_secondary_url = path
    add_activity(db, user, "Updated profile information", "profile", profile.id)
    db.commit()
    return RedirectResponse("/admin/profile", status_code=303)


@router.get("/media", response_class=HTMLResponse)
def media(request: Request, db: Session = Depends(get_db)):
    files = db.query(MediaFile).order_by(MediaFile.created_at.desc()).all()
    return templates.TemplateResponse("admin/media.html", admin_context(request, title="Media", files=files))


@router.post("/media")
def upload_media(request: Request, file: UploadFile = File(...), alt_text: str = Form(""), db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    path, size, file_type = save_upload(file, "media")
    media_file = MediaFile(file_name=path.split("/")[-1], original_name=file.filename or "upload", file_path=path, file_type=file_type, file_size=size, alt_text=alt_text)
    db.add(media_file)
    db.flush()
    add_activity(db, user, "Uploaded media", "media", media_file.id)
    db.commit()
    return RedirectResponse("/admin/media", status_code=303)


@router.post("/media/{item_id}/delete")
def delete_media(item_id: int, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    item = db.get(MediaFile, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Media not found")
    add_activity(db, user, "Deleted media", "media", item.id)
    db.delete(item)
    db.commit()
    return RedirectResponse("/admin/media", status_code=303)


@router.get("/{resource_slug}", response_class=HTMLResponse)
def list_resource(resource_slug: str, request: Request, q: str = "", sort: str = "display_order", page: int = 1, db: Session = Depends(get_db)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    page = max(page, 1)
    query = apply_search(db.query(resource.model), resource, q)
    if hasattr(resource.model, sort):
        query = query.order_by(getattr(resource.model, sort).asc())
    total = query.count()
    items = query.offset((page - 1) * 20).limit(20).all()
    return templates.TemplateResponse("admin/resource_list.html", admin_context(request, title=resource.label, resource=resource, items=items, q=q, sort=sort, page=page, total=total))


@router.get("/{resource_slug}/new", response_class=HTMLResponse)
def new_resource(resource_slug: str, request: Request):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return templates.TemplateResponse("admin/resource_form.html", admin_context(request, title=f"New {resource.label}", resource=resource, item=None))


@router.post("/{resource_slug}/new")
async def create_resource(resource_slug: str, request: Request, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    form = await request.form()
    item = resource.model()
    for field in resource.fields:
        if field.kind == "file":
            upload = form.get(field.name)
            if isinstance(upload, UploadFile) and upload.filename:
                path, _, _ = save_upload(upload, field.upload_folder or resource.slug)
                setattr(item, field.name, path)
            continue
        setattr(item, field.name, coerce_value(form.get(field.name), field.kind))
    db.add(item)
    db.flush()
    add_activity(db, user, f"Created {resource.label}", resource.slug, item.id)
    db.commit()
    return RedirectResponse(f"/admin/{resource_slug}", status_code=303)


@router.get("/{resource_slug}/{item_id}/edit", response_class=HTMLResponse)
def edit_resource(resource_slug: str, item_id: int, request: Request, db: Session = Depends(get_db)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    item = db.get(resource.model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse("admin/resource_form.html", admin_context(request, title=f"Edit {resource.label}", resource=resource, item=item))


@router.post("/{resource_slug}/{item_id}/edit")
async def update_resource(resource_slug: str, item_id: int, request: Request, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    item = db.get(resource.model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    form = await request.form()
    for field in resource.fields:
        if field.kind == "file":
            upload = form.get(field.name)
            if isinstance(upload, UploadFile) and upload.filename:
                path, _, _ = save_upload(upload, field.upload_folder or resource.slug)
                setattr(item, field.name, path)
            continue
        setattr(item, field.name, coerce_value(form.get(field.name), field.kind))
    add_activity(db, user, f"Updated {resource.label}", resource.slug, item.id)
    db.commit()
    return RedirectResponse(f"/admin/{resource_slug}", status_code=303)


@router.post("/{resource_slug}/{item_id}/delete")
def delete_resource(resource_slug: str, item_id: int, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    item = db.get(resource.model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    add_activity(db, user, f"Deleted {resource.label}", resource.slug, item.id)
    db.delete(item)
    db.commit()
    return RedirectResponse(f"/admin/{resource_slug}", status_code=303)
