from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File
from sqlalchemy.orm import Session

from app.auth.security import require_superuser
from app.database import get_db
from app.models import MediaFile, User
from app.routes.resources import RESOURCES, apply_search, coerce_value
from app.utils.files import save_upload


router = APIRouter(prefix="/api", dependencies=[Depends(require_superuser)])


def serialize(item):
    data = {}
    for key, value in item.__dict__.items():
        if key.startswith("_"):
            continue
        data[key] = value.isoformat() if hasattr(value, "isoformat") else value
    return data


@router.get("/{resource_slug}")
def list_items(resource_slug: str, q: str = "", limit: int = 50, offset: int = 0, order_by: str = "display_order", db: Session = Depends(get_db)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    query = apply_search(db.query(resource.model), resource, q)
    if hasattr(resource.model, order_by):
        query = query.order_by(getattr(resource.model, order_by).asc())
    return {"items": [serialize(item) for item in query.offset(offset).limit(min(limit, 100)).all()]}


@router.post("/{resource_slug}")
async def create_item(resource_slug: str, request: Request, db: Session = Depends(get_db), user: User = Depends(require_superuser)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    payload = await request.json()
    item = resource.model()
    for field in resource.fields:
        if field.kind == "file":
            continue
        if field.name in payload:
            setattr(item, field.name, coerce_value(payload.get(field.name), field.kind))
    db.add(item)
    db.commit()
    db.refresh(item)
    return serialize(item)


@router.put("/{resource_slug}/{item_id}")
async def update_item(resource_slug: str, item_id: int, request: Request, db: Session = Depends(get_db)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    item = db.get(resource.model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    payload = await request.json()
    for field in resource.fields:
        if field.kind == "file":
            continue
        if field.name in payload:
            setattr(item, field.name, coerce_value(payload.get(field.name), field.kind))
    db.commit()
    db.refresh(item)
    return serialize(item)


@router.delete("/{resource_slug}/{item_id}")
def delete_item(resource_slug: str, item_id: int, db: Session = Depends(get_db)):
    resource = RESOURCES.get(resource_slug)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    item = db.get(resource.model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"deleted": True}


@router.post("/media/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    path, size, file_type = save_upload(file, "media")
    media_file = MediaFile(file_name=path.split("/")[-1], original_name=file.filename or "upload", file_path=path, file_type=file_type, file_size=size)
    db.add(media_file)
    db.commit()
    db.refresh(media_file)
    return serialize(media_file)
