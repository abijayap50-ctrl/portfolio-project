from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Achievement,
    Certificate,
    ContactMessage,
    Education,
    Experience,
    ProfileInformation,
    Project,
    Service,
    Skill,
    SocialLink,
    Testimonial,
)
from app.services.content import active_ordered
from app.templating import templates


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    profile = db.query(ProfileInformation).first()
    skills = active_ordered(db, Skill)
    grouped_skills = {}
    for skill in skills:
        grouped_skills.setdefault(skill.category or "General", []).append(skill)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "skills": skills,
            "grouped_skills": grouped_skills,
            "education": active_ordered(db, Education),
            "experience": active_ordered(db, Experience),
            "projects": active_ordered(db, Project),
            "certificates": active_ordered(db, Certificate),
            "achievements": active_ordered(db, Achievement),
            "services": active_ordered(db, Service),
            "testimonials": active_ordered(db, Testimonial),
            "social_links": active_ordered(db, SocialLink),
        },
    )


@router.post("/contact")
def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...), db: Session = Depends(get_db)):
    db.add(ContactMessage(name=name, email=email, message=message))
    db.commit()
    return RedirectResponse("/#contact", status_code=303)
