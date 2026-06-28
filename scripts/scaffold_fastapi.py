from __future__ import annotations

import re
import shutil
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(content).lstrip(), encoding="utf-8")


def extract_original_assets() -> tuple[str, str]:
    source = ROOT / "core" / "portfolio" / "templates" / "portfolio" / "index.html"
    html = source.read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", html, flags=re.S).group(1)
    js = re.search(r"<script>(.*?)</script>", html, flags=re.S).group(1)
    css = css.replace("border-radius: 26px;", "border-radius: 8px;")
    css = css.replace("border-radius: 24px;", "border-radius: 8px;")
    return css.strip(), js.strip()


BASE_CSS, BASE_JS = extract_original_assets()

ADMIN_CSS = r"""

/* Admin dashboard */
.admin-body {
    min-height: 100vh;
    background: #f6f8fb;
    color: #172033;
}

.admin-shell {
    display: grid;
    grid-template-columns: 250px minmax(0, 1fr);
    min-height: 100vh;
}

.admin-sidebar {
    position: sticky;
    top: 0;
    height: 100vh;
    padding: 22px;
    color: #fff;
    background: #101827;
    overflow-y: auto;
}

.admin-sidebar .brand {
    margin-bottom: 24px;
}

.admin-nav {
    display: grid;
    gap: 6px;
}

.admin-nav a,
.logout-button {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 42px;
    padding: 0 12px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    color: rgba(255, 255, 255, 0.78);
    background: rgba(255, 255, 255, 0.04);
    font-weight: 850;
}

.admin-nav a:hover,
.logout-button:hover {
    color: #fff;
    background: rgba(255, 255, 255, 0.1);
}

.logout-button {
    width: 100%;
    margin-top: 18px;
    cursor: pointer;
}

.admin-main {
    min-width: 0;
    padding: 26px;
}

.admin-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 22px;
}

.admin-topbar h1 {
    margin: 0;
    color: #101827;
    font-size: 30px;
    line-height: 1.1;
}

.admin-topbar p {
    margin: 6px 0 0;
    color: #65748b;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 14px;
    margin-bottom: 22px;
}

.metric-card,
.admin-panel,
.login-card {
    border: 1px solid #dbe2ea;
    border-radius: 8px;
    background: #fff;
    box-shadow: 0 20px 55px rgba(20, 31, 49, 0.08);
}

.metric-card {
    padding: 18px;
}

.metric-card span {
    display: block;
    color: #65748b;
    font-weight: 850;
}

.metric-card strong {
    display: block;
    margin-top: 8px;
    color: #101827;
    font-size: 34px;
}

.admin-panel {
    padding: 18px;
    margin-bottom: 18px;
}

.toolbar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 16px;
}

.toolbar form {
    display: flex;
    gap: 8px;
}

.admin-table {
    width: 100%;
    border-collapse: collapse;
}

.admin-table th,
.admin-table td {
    padding: 12px 10px;
    border-top: 1px solid #e6ecf2;
    color: #243044;
    text-align: left;
    vertical-align: top;
}

.admin-table th {
    color: #65748b;
    font-size: 12px;
    text-transform: uppercase;
}

.admin-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.admin-form {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.admin-form .wide,
.form-actions {
    grid-column: 1 / -1;
}

.field {
    display: grid;
    gap: 7px;
}

.field label {
    color: #334155;
    font-size: 13px;
    font-weight: 900;
}

.field input,
.field textarea,
.field select {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    border: 1px solid #ccd6e0;
    border-radius: 8px;
    color: #172033;
    background: #fff;
}

.field textarea {
    min-height: 118px;
    resize: vertical;
}

.check-field {
    display: flex;
    align-items: center;
    gap: 10px;
    min-height: 44px;
}

.check-field input {
    width: 18px;
    height: 18px;
}

.form-actions {
    display: flex;
    gap: 10px;
}

.login-page {
    display: grid;
    place-items: center;
    min-height: 100vh;
    padding: 20px;
    background: linear-gradient(135deg, #101827, #0f3a4f);
}

.login-card {
    width: min(440px, 100%);
    padding: 26px;
}

.login-card h1 {
    margin-bottom: 8px;
    color: #101827;
    font-size: 30px;
}

.alert {
    padding: 12px 14px;
    border: 1px solid #fecaca;
    border-radius: 8px;
    color: #991b1b;
    background: #fef2f2;
}

.recent-list {
    display: grid;
    gap: 10px;
    margin: 0;
    padding: 0;
    list-style: none;
}

.recent-list li {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 12px;
    border: 1px solid #e6ecf2;
    border-radius: 8px;
}

@media (max-width: 980px) {
    .admin-shell {
        grid-template-columns: 1fr;
    }

    .admin-sidebar {
        position: static;
        height: auto;
    }

    .metric-grid,
    .admin-form {
        grid-template-columns: 1fr;
    }

    .admin-table {
        display: block;
        overflow-x: auto;
    }
}
"""

APP_JS = BASE_JS.replace(
    'themeToggle.textContent = document.body.classList.contains("light-mode") ? "Light" : "Dark";',
    'themeToggle.textContent = document.body.classList.contains("light-mode") ? "Light" : "Dark";\n            localStorage.setItem("portfolio-theme", document.body.classList.contains("light-mode") ? "light" : "dark");',
)


write("app/__init__.py", "")
write(
    "app/config.py",
    """
    from functools import lru_cache
    import os
    from pathlib import Path


    class Settings:
        PROJECT_NAME = os.getenv("PROJECT_NAME", "Dynamic Portfolio")
        SECRET_KEY = os.getenv("SECRET_KEY", "change-this-development-secret")
        JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
        ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "480"))
        DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")
        ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
        ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "ChangeMe123!")
        MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", "10"))
        BASE_DIR = Path(__file__).resolve().parents[1]
        UPLOAD_DIR = BASE_DIR / "static" / "uploads"


    @lru_cache
    def get_settings() -> Settings:
        return Settings()
    """,
)

write(
    "app/database/session.py",
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import declarative_base, sessionmaker

    from app.config import get_settings


    settings = get_settings()
    connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
    engine = create_engine(settings.DATABASE_URL, connect_args=connect_args, future=True)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    Base = declarative_base()


    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    """,
)

write("app/database/__init__.py", "from app.database.session import Base, SessionLocal, engine, get_db\n")

write(
    "app/models.py",
    """
    from datetime import date, datetime

    from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text
    from sqlalchemy.orm import Mapped, mapped_column, relationship

    from app.database import Base


    class TimestampMixin:
        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
        updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        is_active: Mapped[bool] = mapped_column(Boolean, default=True)
        display_order: Mapped[int] = mapped_column(Integer, default=0)


    class User(Base):
        __tablename__ = "users"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
        full_name: Mapped[str] = mapped_column(String(255), default="Super User")
        hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
        role: Mapped[str] = mapped_column(String(50), default="superuser")
        is_active: Mapped[bool] = mapped_column(Boolean, default=True)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    class ProfileInformation(Base):
        __tablename__ = "profile_information"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        full_name: Mapped[str] = mapped_column(String(255), default="ABIJAY AP")
        professional_title: Mapped[str] = mapped_column(String(255), default="Python Developer")
        profile_photo: Mapped[str | None] = mapped_column(String(500), nullable=True)
        about_me: Mapped[str] = mapped_column(Text, default="")
        biography: Mapped[str] = mapped_column(Text, default="")
        resume_pdf: Mapped[str] = mapped_column(String(500), default="/static/docs/resume.pdf")
        contact_email: Mapped[str] = mapped_column(String(255), default="abijayap50@gmail.com")
        phone_number: Mapped[str] = mapped_column(String(80), default="7356741669")
        address: Mapped[str] = mapped_column(String(255), default="Bangalore, Karnataka")
        location: Mapped[str] = mapped_column(String(255), default="Bangalore, Karnataka")
        website_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        linkedin_url: Mapped[str] = mapped_column(String(500), default="https://linkedin.com/in/abijay-ap-2004")
        github_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        twitter_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        instagram_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        portfolio_logo: Mapped[str | None] = mapped_column(String(500), nullable=True)
        footer_information: Mapped[str] = mapped_column(String(500), default="ABIJAY AP | Python Developer Portfolio")
        hero_heading: Mapped[str] = mapped_column(String(255), default="Python Developer building useful backend systems.")
        hero_subheading: Mapped[str] = mapped_column(String(255), default="Backend Developer | AI and Data Science Student")
        hero_description: Mapped[str] = mapped_column(Text, default="")
        hero_background_image: Mapped[str] = mapped_column(String(500), default="/static/videos/hero-background.mp4")
        hero_profile_image: Mapped[str | None] = mapped_column(String(500), nullable=True)
        cta_primary_label: Mapped[str] = mapped_column(String(80), default="View Projects")
        cta_primary_url: Mapped[str] = mapped_column(String(500), default="#projects")
        cta_secondary_label: Mapped[str] = mapped_column(String(80), default="Download Resume")
        cta_secondary_url: Mapped[str] = mapped_column(String(500), default="/static/docs/resume.pdf")
        about_heading: Mapped[str] = mapped_column(String(255), default="Backend-focused fresher with AI and data science exposure.")
        about_content: Mapped[str] = mapped_column(Text, default="")
        personal_details: Mapped[str] = mapped_column(Text, default="")
        years_experience: Mapped[str] = mapped_column(String(80), default="Fresher")
        education_summary: Mapped[str] = mapped_column(Text, default="")
        career_summary: Mapped[str] = mapped_column(Text, default="")
        working_hours: Mapped[str] = mapped_column(String(255), default="Open to opportunities")
        updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    class Skill(TimestampMixin, Base):
        __tablename__ = "skills"

        name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
        category: Mapped[str] = mapped_column(String(120), default="General", index=True)
        percentage: Mapped[int] = mapped_column(Integer, default=75)
        level: Mapped[str] = mapped_column(String(80), default="Intermediate")
        icon: Mapped[str | None] = mapped_column(String(500), nullable=True)


    class Education(TimestampMixin, Base):
        __tablename__ = "education"

        institution_name: Mapped[str] = mapped_column(String(255), nullable=False)
        degree: Mapped[str] = mapped_column(String(255), nullable=False)
        field_of_study: Mapped[str | None] = mapped_column(String(255), nullable=True)
        start_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        end_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        grade_cgpa: Mapped[str | None] = mapped_column(String(80), nullable=True)
        description: Mapped[str] = mapped_column(Text, default="")
        location: Mapped[str | None] = mapped_column(String(255), nullable=True)
        badge: Mapped[str | None] = mapped_column(String(40), nullable=True)


    class Experience(TimestampMixin, Base):
        __tablename__ = "experience"

        job_title: Mapped[str] = mapped_column(String(255), nullable=False)
        company_name: Mapped[str] = mapped_column(String(255), nullable=False)
        company_logo: Mapped[str | None] = mapped_column(String(500), nullable=True)
        employment_type: Mapped[str | None] = mapped_column(String(120), nullable=True)
        start_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        end_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        description: Mapped[str] = mapped_column(Text, default="")
        responsibilities: Mapped[str] = mapped_column(Text, default="")


    class Project(TimestampMixin, Base):
        __tablename__ = "projects"

        title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
        description: Mapped[str] = mapped_column(Text, default="")
        detailed_description: Mapped[str] = mapped_column(Text, default="")
        technologies_used: Mapped[str] = mapped_column(Text, default="")
        github_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        live_demo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        project_image: Mapped[str | None] = mapped_column(String(500), nullable=True)
        project_category: Mapped[str] = mapped_column(String(120), default="Backend")
        featured: Mapped[bool] = mapped_column(Boolean, default=True)
        completion_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        gallery_images = relationship("ProjectGalleryImage", back_populates="project", cascade="all, delete-orphan")


    class ProjectGalleryImage(Base):
        __tablename__ = "project_gallery_images"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"))
        image_path: Mapped[str] = mapped_column(String(500), nullable=False)
        alt_text: Mapped[str | None] = mapped_column(String(255), nullable=True)
        display_order: Mapped[int] = mapped_column(Integer, default=0)
        project = relationship("Project", back_populates="gallery_images")


    class Certificate(TimestampMixin, Base):
        __tablename__ = "certificates"

        certificate_name: Mapped[str] = mapped_column(String(255), nullable=False)
        issuing_organization: Mapped[str] = mapped_column(String(255), nullable=False)
        issue_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        expiration_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        credential_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
        verification_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
        certificate_image: Mapped[str | None] = mapped_column(String(500), nullable=True)
        certificate_pdf: Mapped[str | None] = mapped_column(String(500), nullable=True)
        skills: Mapped[str] = mapped_column(Text, default="")


    class Achievement(TimestampMixin, Base):
        __tablename__ = "achievements"

        title: Mapped[str] = mapped_column(String(255), nullable=False)
        description: Mapped[str] = mapped_column(Text, default="")
        date: Mapped[date | None] = mapped_column(Date, nullable=True)
        image: Mapped[str | None] = mapped_column(String(500), nullable=True)


    class Service(TimestampMixin, Base):
        __tablename__ = "services"

        service_name: Mapped[str] = mapped_column(String(255), nullable=False)
        description: Mapped[str] = mapped_column(Text, default="")
        icon: Mapped[str | None] = mapped_column(String(255), nullable=True)


    class Testimonial(TimestampMixin, Base):
        __tablename__ = "testimonials"

        client_name: Mapped[str] = mapped_column(String(255), nullable=False)
        position: Mapped[str | None] = mapped_column(String(255), nullable=True)
        company: Mapped[str | None] = mapped_column(String(255), nullable=True)
        photo: Mapped[str | None] = mapped_column(String(500), nullable=True)
        review_text: Mapped[str] = mapped_column(Text, default="")
        rating: Mapped[int] = mapped_column(Integer, default=5)


    class SocialLink(TimestampMixin, Base):
        __tablename__ = "social_links"

        platform: Mapped[str] = mapped_column(String(120), nullable=False)
        url: Mapped[str] = mapped_column(String(500), nullable=False)
        icon: Mapped[str | None] = mapped_column(String(255), nullable=True)


    class MediaFile(Base):
        __tablename__ = "media_files"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        file_name: Mapped[str] = mapped_column(String(255), nullable=False)
        original_name: Mapped[str] = mapped_column(String(255), nullable=False)
        file_path: Mapped[str] = mapped_column(String(500), nullable=False)
        file_type: Mapped[str] = mapped_column(String(120), nullable=False)
        file_size: Mapped[int] = mapped_column(Integer, default=0)
        alt_text: Mapped[str | None] = mapped_column(String(255), nullable=True)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    class ContactMessage(Base):
        __tablename__ = "contact_messages"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        name: Mapped[str] = mapped_column(String(255), nullable=False)
        email: Mapped[str] = mapped_column(String(255), nullable=False)
        message: Mapped[str] = mapped_column(Text, nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
        is_read: Mapped[bool] = mapped_column(Boolean, default=False)


    class ActivityLog(Base):
        __tablename__ = "activity_logs"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
        action: Mapped[str] = mapped_column(String(255), nullable=False)
        entity_type: Mapped[str] = mapped_column(String(120), nullable=False)
        entity_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    """,
)

write(
    "app/schemas.py",
    """
    from datetime import date, datetime
    from typing import Optional

    from pydantic import BaseModel, EmailStr, Field


    class ORMModel(BaseModel):
        class Config:
            orm_mode = True


    class Token(BaseModel):
        access_token: str
        token_type: str = "bearer"


    class LoginRequest(BaseModel):
        email: EmailStr
        password: str


    class UserOut(ORMModel):
        id: int
        email: EmailStr
        full_name: str
        role: str


    class ProfileUpdate(BaseModel):
        full_name: str = "ABIJAY AP"
        professional_title: str = "Python Developer"
        about_me: str = ""
        biography: str = ""
        contact_email: EmailStr = "admin@example.com"
        phone_number: str = ""
        address: str = ""
        location: str = ""
        website_url: Optional[str] = None
        linkedin_url: Optional[str] = None
        github_url: Optional[str] = None
        twitter_url: Optional[str] = None
        instagram_url: Optional[str] = None
        footer_information: str = ""
        hero_heading: str = ""
        hero_subheading: str = ""
        hero_description: str = ""
        about_heading: str = ""
        about_content: str = ""
        personal_details: str = ""
        years_experience: str = ""
        education_summary: str = ""
        career_summary: str = ""
        working_hours: str = ""


    class SkillBase(BaseModel):
        name: str
        category: str = "General"
        percentage: int = Field(75, ge=0, le=100)
        level: str = "Intermediate"
        icon: Optional[str] = None
        display_order: int = 0
        is_active: bool = True


    class SkillOut(SkillBase, ORMModel):
        id: int


    class EducationBase(BaseModel):
        institution_name: str
        degree: str
        field_of_study: Optional[str] = None
        start_date: Optional[date] = None
        end_date: Optional[date] = None
        grade_cgpa: Optional[str] = None
        description: str = ""
        location: Optional[str] = None
        badge: Optional[str] = None
        display_order: int = 0
        is_active: bool = True


    class EducationOut(EducationBase, ORMModel):
        id: int


    class ExperienceBase(BaseModel):
        job_title: str
        company_name: str
        company_logo: Optional[str] = None
        employment_type: Optional[str] = None
        start_date: Optional[date] = None
        end_date: Optional[date] = None
        description: str = ""
        responsibilities: str = ""
        display_order: int = 0
        is_active: bool = True


    class ExperienceOut(ExperienceBase, ORMModel):
        id: int


    class ProjectBase(BaseModel):
        title: str
        description: str = ""
        detailed_description: str = ""
        technologies_used: str = ""
        github_url: Optional[str] = None
        live_demo_url: Optional[str] = None
        project_image: Optional[str] = None
        project_category: str = "Backend"
        featured: bool = True
        completion_date: Optional[date] = None
        display_order: int = 0
        is_active: bool = True


    class ProjectOut(ProjectBase, ORMModel):
        id: int


    class CertificateBase(BaseModel):
        certificate_name: str
        issuing_organization: str
        issue_date: Optional[date] = None
        expiration_date: Optional[date] = None
        credential_id: Optional[str] = None
        verification_url: Optional[str] = None
        certificate_image: Optional[str] = None
        certificate_pdf: Optional[str] = None
        skills: str = ""
        display_order: int = 0
        is_active: bool = True


    class CertificateOut(CertificateBase, ORMModel):
        id: int


    class AchievementBase(BaseModel):
        title: str
        description: str = ""
        date: Optional[date] = None
        image: Optional[str] = None
        display_order: int = 0
        is_active: bool = True


    class ServiceBase(BaseModel):
        service_name: str
        description: str = ""
        icon: Optional[str] = None
        display_order: int = 0
        is_active: bool = True


    class TestimonialBase(BaseModel):
        client_name: str
        position: Optional[str] = None
        company: Optional[str] = None
        photo: Optional[str] = None
        review_text: str = ""
        rating: int = Field(5, ge=1, le=5)
        display_order: int = 0
        is_active: bool = True


    class SocialLinkBase(BaseModel):
        platform: str
        url: str
        icon: Optional[str] = None
        display_order: int = 0
        is_active: bool = True


    class MediaFileOut(ORMModel):
        id: int
        file_name: str
        original_name: str
        file_path: str
        file_type: str
        file_size: int
        created_at: datetime
    """,
)

write(
    "app/auth/security.py",
    """
    from datetime import datetime, timedelta
    import secrets
    from typing import Any

    from fastapi import Depends, HTTPException, Request, status
    from fastapi.security import OAuth2PasswordBearer
    from jose import JWTError, jwt
    from passlib.context import CryptContext
    from sqlalchemy.orm import Session

    from app.config import get_settings
    from app.database import get_db
    from app.models import User


    settings = get_settings()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login", auto_error=False)


    def hash_password(password: str) -> str:
        return password_context.hash(password)


    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)


    def create_access_token(subject: str, extra: dict[str, Any] | None = None) -> str:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload: dict[str, Any] = {"sub": subject, "exp": expire}
        if extra:
            payload.update(extra)
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


    def create_csrf_token() -> str:
        return secrets.token_urlsafe(32)


    def token_from_request(request: Request, bearer_token: str | None = None) -> str | None:
        if bearer_token:
            return bearer_token
        return request.cookies.get("access_token")


    def get_current_user(
        request: Request,
        db: Session = Depends(get_db),
        bearer_token: str | None = Depends(oauth2_scheme),
    ) -> User:
        token = token_from_request(request, bearer_token)
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            email: str | None = payload.get("sub")
        except JWTError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
        user = db.query(User).filter(User.email == email, User.is_active.is_(True)).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive or missing user")
        return user


    def require_superuser(user: User = Depends(get_current_user)) -> User:
        if user.role != "superuser":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Super user access required")
        return user


    def validate_csrf(request: Request) -> None:
        cookie_token = request.cookies.get("csrf_token")
        submitted = request.headers.get("x-csrf-token")
        if request.method in {"POST", "PUT", "PATCH", "DELETE"}:
            submitted = submitted or getattr(request.state, "csrf_token", None)
        if not cookie_token or not submitted or not secrets.compare_digest(cookie_token, submitted):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid CSRF token")
    """,
)
write("app/auth/__init__.py", "")

write(
    "app/utils/files.py",
    """
    from pathlib import Path
    import re
    import shutil
    import uuid

    from fastapi import HTTPException, UploadFile, status

    from app.config import get_settings


    ALLOWED_EXTENSIONS = {
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
        ".pdf", ".mp4", ".webm",
    }


    def safe_filename(filename: str) -> str:
        stem = Path(filename).stem
        suffix = Path(filename).suffix.lower()
        cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "-", stem).strip("-") or "upload"
        return f"{cleaned}-{uuid.uuid4().hex[:10]}{suffix}"


    def save_upload(upload: UploadFile, folder: str = "media") -> tuple[str, int, str]:
        settings = get_settings()
        suffix = Path(upload.filename or "").suffix.lower()
        if suffix not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

        destination_dir = settings.UPLOAD_DIR / folder
        destination_dir.mkdir(parents=True, exist_ok=True)
        filename = safe_filename(upload.filename or "upload")
        destination = destination_dir / filename

        size = 0
        max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
        with destination.open("wb") as buffer:
            while chunk := upload.file.read(1024 * 1024):
                size += len(chunk)
                if size > max_bytes:
                    buffer.close()
                    destination.unlink(missing_ok=True)
                    raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File too large")
                buffer.write(chunk)

        rel_path = destination.relative_to(settings.BASE_DIR).as_posix()
        return f"/{rel_path}", size, suffix.lstrip(".")
    """,
)
write("app/utils/__init__.py", "")

write(
    "app/services/content.py",
    """
    from __future__ import annotations

    from datetime import date

    from sqlalchemy.orm import Session

    from app.auth.security import hash_password
    from app.config import get_settings
    from app.models import (
        Achievement,
        Certificate,
        Education,
        Experience,
        ProfileInformation,
        Project,
        Service,
        Skill,
        SocialLink,
        Testimonial,
        User,
    )


    def ensure_default_superuser(db: Session) -> None:
        settings = get_settings()
        existing = db.query(User).filter(User.email == settings.ADMIN_EMAIL).first()
        if existing:
            return
        db.add(
            User(
                email=settings.ADMIN_EMAIL,
                full_name="Portfolio Super User",
                hashed_password=hash_password(settings.ADMIN_PASSWORD),
                role="superuser",
            )
        )
        db.commit()


    def ensure_default_content(db: Session) -> None:
        if not db.query(ProfileInformation).first():
            db.add(
                ProfileInformation(
                    hero_description="Aspiring backend developer with Django, REST APIs, SQL, Git, debugging, and code optimization experience. I enjoy turning data and logic into useful web systems.",
                    about_me="Aspiring Backend Developer familiar with Django ORM, authentication systems, REST API operations, Git, SQL, debugging, and code optimization.",
                    biography="AI and Data Science student focused on practical backend engineering, clean database design, and useful automation.",
                    about_content="I enjoy turning data and logic into useful web systems, with a focus on clean backend structure, database work, and practical problem solving.",
                    personal_details="Primary language: Python\\nBackend framework: Django\\nDatabase logic: SQL",
                    education_summary="A recruiter-friendly education path from SSLC to Higher Secondary and current B-Tech studies.",
                    career_summary="Seeking Software Engineer or Backend Developer roles where I can contribute to scalable applications and grow through real product work.",
                )
            )

        if not db.query(Skill).first():
            for idx, item in enumerate([
                ("Python", "Backend", 88, "Advanced"),
                ("Django", "Backend", 82, "Intermediate"),
                ("REST API Operations", "Backend", 80, "Intermediate"),
                ("SQL", "Data and Tools", 78, "Intermediate"),
                ("Machine Learning Basics", "Data and Tools", 70, "Intermediate"),
                ("YOLO", "Data and Tools", 68, "Foundational"),
                ("Git", "Data and Tools", 76, "Intermediate"),
            ]):
                db.add(Skill(name=item[0], category=item[1], percentage=item[2], level=item[3], display_order=idx))

        if not db.query(Education).first():
            db.add_all([
                Education(institution_name="JCT College of Engineering and Technology", degree="B-Tech", field_of_study="Artificial Intelligence and Data Science", start_date=date(2022, 9, 1), description="Anna University", location="Pichanur, Tamil Nadu", badge="UG", display_order=1),
                Education(institution_name="GHSS Mankara", degree="Higher Secondary Education", start_date=date(2020, 6, 1), end_date=date(2022, 5, 1), location="Palakkad, Kerala", badge="+2", display_order=2),
                Education(institution_name="Seva Sadan Central School", degree="SSLC", end_date=date(2020, 4, 1), location="Palakkad, Kerala", badge="10", display_order=3),
            ])

        if not db.query(Project).first():
            db.add_all([
                Project(title="Car Damage Detection and Severity Classification", description="Computer vision system for vehicle damage detection, localization, and classification using a hybrid CNN-YOLO approach.", technologies_used="YOLOv8, CNN, Image Processing", detailed_description="Trained on 8K+ annotated images with preprocessing and augmentation. Evaluated with mAP, Precision, Recall, and IoU metrics.", display_order=1),
                Project(title="Fraud Detection System", description="Python-based system to detect suspicious email activities with rule-based logic and anomaly detection.", technologies_used="Python, Pandas, Anomaly Detection", detailed_description="Processed and cleaned datasets, simulated phishing and spoofing signals, and modularized code for maintainability.", display_order=2),
                Project(title="Data Processing Automation Tool", description="Python automation script for data cleaning and file processing tasks.", technologies_used="Python, Pandas, File Handling", detailed_description="Reduced manual effort in repetitive data tasks through reusable processing logic.", display_order=3),
            ])

        if not db.query(Certificate).first():
            db.add_all([
                Certificate(certificate_name="Tools of the Trade: Linux and SQL", issuing_organization="Google", skills="SQL, Linux CLI, Cloud VM Usage", display_order=1),
                Certificate(certificate_name="Tata Data Visualisation Job Simulation", issuing_organization="Tata Consultancy Services", skills="Data Visualisation, Business Insights, Decision Support", display_order=2),
            ])

        if not db.query(Experience).first():
            db.add(Experience(job_title="Add Internship", company_name="Company Name", employment_type="Internship", description="This section is ready for your internship or training details.", responsibilities="Add responsibility 1\\nAdd responsibility 2\\nAdd measurable impact", is_active=False))

        if not db.query(Achievement).first():
            db.add_all([
                Achievement(title="Achievement 1", description="Add competition, rank, academic recognition, or project milestone.", display_order=1),
                Achievement(title="Achievement 2", description="Add another measurable accomplishment.", display_order=2),
            ])

        if not db.query(Service).first():
            db.add_all([
                Service(service_name="Backend Development", description="Database-backed APIs, CRUD systems, and admin workflows.", icon="server", display_order=1),
                Service(service_name="Automation", description="Python scripts for data cleaning, reporting, and repetitive workflows.", icon="zap", display_order=2),
            ])

        if not db.query(SocialLink).first():
            db.add_all([
                SocialLink(platform="LinkedIn", url="https://linkedin.com/in/abijay-ap-2004", display_order=1),
                SocialLink(platform="GitHub", url="#", display_order=2),
            ])

        if not db.query(Testimonial).first():
            db.add(Testimonial(client_name="Future Client", position="Add testimonial", company="Portfolio", review_text="Add review text from a mentor, client, or teammate.", rating=5, is_active=False))

        db.commit()


    def active_ordered(db: Session, model):
        return db.query(model).filter(model.is_active.is_(True)).order_by(model.display_order.asc(), model.id.asc()).all()
    """,
)
write("app/services/__init__.py", "")

write(
    "app/routes/resources.py",
    """
    from __future__ import annotations

    from dataclasses import dataclass
    from datetime import date
    from typing import Any

    from sqlalchemy import or_

    from app import models


    @dataclass(frozen=True)
    class Field:
        name: str
        label: str
        kind: str = "text"
        required: bool = False
        wide: bool = False
        upload_folder: str | None = None


    @dataclass(frozen=True)
    class Resource:
        slug: str
        label: str
        model: type
        title_field: str
        fields: tuple[Field, ...]
        search_fields: tuple[str, ...]


    RESOURCES: dict[str, Resource] = {
        "skills": Resource("skills", "Skills", models.Skill, "name", (
            Field("name", "Skill Name", required=True),
            Field("category", "Category"),
            Field("percentage", "Skill Percentage", "number"),
            Field("level", "Skill Level"),
            Field("icon", "Icon", "file", upload_folder="skills"),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("name", "category", "level")),
        "education": Resource("education", "Education", models.Education, "degree", (
            Field("institution_name", "Institution Name", required=True),
            Field("degree", "Degree", required=True),
            Field("field_of_study", "Field of Study"),
            Field("start_date", "Start Date", "date"),
            Field("end_date", "End Date", "date"),
            Field("grade_cgpa", "Grade/CGPA"),
            Field("location", "Location"),
            Field("badge", "Badge"),
            Field("description", "Description", "textarea", wide=True),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("institution_name", "degree", "field_of_study", "description")),
        "experience": Resource("experience", "Experience", models.Experience, "job_title", (
            Field("job_title", "Job Title", required=True),
            Field("company_name", "Company Name", required=True),
            Field("company_logo", "Company Logo", "file", upload_folder="experience"),
            Field("employment_type", "Employment Type"),
            Field("start_date", "Start Date", "date"),
            Field("end_date", "End Date", "date"),
            Field("description", "Description", "textarea", wide=True),
            Field("responsibilities", "Responsibilities", "textarea", wide=True),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("job_title", "company_name", "description")),
        "projects": Resource("projects", "Projects", models.Project, "title", (
            Field("title", "Project Title", required=True),
            Field("project_category", "Project Category"),
            Field("description", "Description", "textarea", wide=True),
            Field("detailed_description", "Detailed Description", "textarea", wide=True),
            Field("technologies_used", "Technologies Used", "textarea", wide=True),
            Field("github_url", "GitHub URL", "url"),
            Field("live_demo_url", "Live Demo URL", "url"),
            Field("project_image", "Project Image", "file", upload_folder="projects"),
            Field("featured", "Featured", "checkbox"),
            Field("completion_date", "Completion Date", "date"),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("title", "description", "technologies_used", "project_category")),
        "certificates": Resource("certificates", "Certificates", models.Certificate, "certificate_name", (
            Field("certificate_name", "Certificate Name", required=True),
            Field("issuing_organization", "Issuing Organization", required=True),
            Field("issue_date", "Issue Date", "date"),
            Field("expiration_date", "Expiration Date", "date"),
            Field("credential_id", "Credential ID"),
            Field("verification_url", "Verification URL", "url"),
            Field("certificate_image", "Certificate Image", "file", upload_folder="certificates"),
            Field("certificate_pdf", "Certificate PDF", "file", upload_folder="certificates"),
            Field("skills", "Tags/Skills", "textarea", wide=True),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("certificate_name", "issuing_organization", "credential_id", "skills")),
        "achievements": Resource("achievements", "Achievements", models.Achievement, "title", (
            Field("title", "Title", required=True),
            Field("date", "Date", "date"),
            Field("image", "Image", "file", upload_folder="achievements"),
            Field("description", "Description", "textarea", wide=True),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("title", "description")),
        "services": Resource("services", "Services", models.Service, "service_name", (
            Field("service_name", "Service Name", required=True),
            Field("icon", "Icon"),
            Field("description", "Description", "textarea", wide=True),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("service_name", "description")),
        "testimonials": Resource("testimonials", "Testimonials", models.Testimonial, "client_name", (
            Field("client_name", "Client Name", required=True),
            Field("position", "Position"),
            Field("company", "Company"),
            Field("photo", "Photo", "file", upload_folder="testimonials"),
            Field("review_text", "Review Text", "textarea", wide=True),
            Field("rating", "Rating", "number"),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("client_name", "position", "company", "review_text")),
        "social-links": Resource("social-links", "Social Links", models.SocialLink, "platform", (
            Field("platform", "Platform", required=True),
            Field("url", "URL", "url", required=True),
            Field("icon", "Icon"),
            Field("display_order", "Display Order", "number"),
            Field("is_active", "Active", "checkbox"),
        ), ("platform", "url")),
    }


    def coerce_value(value: Any, kind: str) -> Any:
        if kind == "checkbox":
            return value in {"on", "true", "True", True, "1", 1}
        if value in {"", None}:
            return None if kind in {"date", "url"} else ""
        if kind == "number":
            return int(value)
        if kind == "date":
            return date.fromisoformat(str(value))
        return str(value)


    def apply_search(query, resource: Resource, term: str | None):
        if not term:
            return query
        clauses = [getattr(resource.model, field).ilike(f"%{term}%") for field in resource.search_fields]
        return query.filter(or_(*clauses))
    """,
)

write(
    "app/routes/public.py",
    """
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
    """,
)

write(
    "app/routes/auth.py",
    """
    from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
    from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
    from sqlalchemy.orm import Session

    from app.auth.security import create_access_token, create_csrf_token, get_current_user, verify_password
    from app.database import get_db
    from app.models import User
    from app.schemas import LoginRequest, Token, UserOut
    from app.templating import templates


    router = APIRouter()


    @router.get("/login", response_class=HTMLResponse)
    def login_page(request: Request):
        response = templates.TemplateResponse("admin/login.html", {"request": request, "error": None})
        response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
        return response


    @router.post("/login")
    def login_form(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == email, User.is_active.is_(True)).first()
        if not user or not verify_password(password, user.hashed_password):
            response = templates.TemplateResponse("admin/login.html", {"request": request, "error": "Invalid email or password"}, status_code=400)
            response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
            return response
        token = create_access_token(user.email, {"role": user.role})
        response = RedirectResponse("/admin", status_code=303)
        response.set_cookie("access_token", token, httponly=True, samesite="lax", max_age=60 * 60 * 8)
        response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
        return response


    @router.post("/logout")
    def logout():
        response = RedirectResponse("/login", status_code=303)
        response.delete_cookie("access_token")
        response.delete_cookie("csrf_token")
        return response


    @router.post("/api/login", response_model=Token)
    def api_login(payload: LoginRequest, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == payload.email, User.is_active.is_(True)).first()
        if not user or not verify_password(payload.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return Token(access_token=create_access_token(user.email, {"role": user.role}))


    @router.post("/api/logout")
    def api_logout():
        return JSONResponse({"message": "Logged out. Delete the bearer token client-side."})


    @router.get("/api/me", response_model=UserOut)
    def me(user: User = Depends(get_current_user)):
        return user
    """,
)

write(
    "app/routes/admin.py",
    """
    from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile
    from fastapi.responses import HTMLResponse, RedirectResponse
    from sqlalchemy.orm import Session

    from app.auth.security import create_csrf_token, require_superuser
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


    router = APIRouter(prefix="/admin", dependencies=[Depends(require_superuser)])


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
    """,
)

write(
    "app/routes/api.py",
    """
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
    """,
)
write("app/routes/__init__.py", "")

write(
    "app/templating.py",
    """
    from fastapi.templating import Jinja2Templates


    templates = Jinja2Templates(directory="templates")


    def nl2br(value: str | None) -> str:
        return "" if not value else "<br>".join(value.splitlines())


    def tags(value: str | None) -> list[str]:
        if not value:
            return []
        return [part.strip() for part in value.replace("\\n", ",").split(",") if part.strip()]


    templates.env.filters["nl2br"] = nl2br
    templates.env.filters["tags"] = tags
    """,
)

write(
    "app/main.py",
    """
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    from app.config import get_settings
    from app.database import Base, SessionLocal, engine
    from app.routes import admin, api, auth, public
    from app.services.content import ensure_default_content, ensure_default_superuser


    settings = get_settings()
    app = FastAPI(title=settings.PROJECT_NAME)
    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.include_router(auth.router)
    app.include_router(public.router)
    app.include_router(admin.router)
    app.include_router(api.router)


    @app.on_event("startup")
    def startup() -> None:
        settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        try:
            ensure_default_superuser(db)
            ensure_default_content(db)
        finally:
            db.close()
    """,
)

write(
    "templates/base.html",
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}{{ profile.full_name if profile else "Portfolio" }}{% endblock %}</title>
        <link rel="stylesheet" href="{{ url_for('static', path='css/style.css') }}">
    </head>
    <body>
        {% block body %}{% endblock %}
        <script src="{{ url_for('static', path='js/app.js') }}"></script>
    </body>
    </html>
    """,
)

write(
    "templates/index.html",
    """
    {% extends "base.html" %}
    {% block title %}{{ profile.full_name }} | {{ profile.professional_title }}{% endblock %}
    {% block body %}
    <header class="site-header">
        <nav class="nav" aria-label="Main navigation">
            <a class="brand" href="#home">
                <span class="brand-mark">{{ profile.full_name[:2] }}</span>
                <span class="brand-text"><span>{{ profile.full_name }}</span><span>{{ profile.professional_title }}</span></span>
            </a>
            <div class="nav-links" id="nav-links">
                <a href="#about">About</a><a href="#education">Education</a><a href="#skills">Skills</a><a href="#projects">Projects</a><a href="#experience">Experience</a><a href="#certificates">Certificates</a><a href="#contact">Contact</a>
            </div>
            <div class="header-actions">
                <button class="icon-btn" id="theme-toggle" type="button" aria-label="Toggle dark and light mode">Dark</button>
                <a class="btn btn-primary" href="{{ profile.cta_secondary_url }}">Resume</a>
                <button class="menu-toggle" type="button" aria-controls="nav-links" aria-expanded="false">Menu</button>
            </div>
        </nav>
    </header>

    <main>
        <section class="hero" id="home">
            {% if profile.hero_background_image and profile.hero_background_image.endswith('.mp4') %}
            <video class="hero-video" src="{{ profile.hero_background_image }}" autoplay muted loop playsinline></video>
            {% endif %}
            <div class="hero-inner">
                <div>
                    <p class="eyebrow">{{ profile.hero_subheading }}</p>
                    <h1>{{ profile.hero_heading }}</h1>
                    <p class="hero-copy">{{ profile.hero_description }}</p>
                    <div class="hero-actions">
                        <a class="btn btn-primary" href="{{ profile.cta_primary_url }}">{{ profile.cta_primary_label }}</a>
                        <a class="btn" href="{{ profile.cta_secondary_url }}">{{ profile.cta_secondary_label }}</a>
                    </div>
                </div>
                <aside class="profile-panel reveal">
                    <h2>{{ profile.full_name }}</h2>
                    <p>{{ profile.professional_title }}</p>
                    <ul class="info-list">
                        <li><strong>Email</strong><span>{{ profile.contact_email }}</span></li>
                        <li><strong>Phone</strong><span>{{ profile.phone_number }}</span></li>
                        <li><strong>Location</strong><span>{{ profile.location }}</span></li>
                        <li><strong>Focus</strong><span>{{ profile.career_summary }}</span></li>
                    </ul>
                </aside>
            </div>
        </section>

        <section class="section alt" id="about">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal">
                    <div><p class="section-label">About Me</p><h2>{{ profile.about_heading }}</h2></div>
                    <p class="section-text">{{ profile.about_content }}</p>
                </div>
                <div class="flow-grid">
                    <article class="flow-panel reveal"><h3>Profile</h3><p>{{ profile.about_me }}</p></article>
                    <article class="flow-panel reveal">
                        <h3>Career Objective</h3>
                        <p>{{ profile.career_summary }}</p>
                        <div class="stat-strip">
                            {% for line in profile.personal_details.split('\\n')[:3] %}
                            {% set parts = line.split(':', 1) %}
                            <div><strong>{{ parts[1].strip() if parts|length > 1 else line }}</strong><span>{{ parts[0].strip() if parts|length > 1 else "Detail" }}</span></div>
                            {% endfor %}
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <section class="section" id="education">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Education</p><h2>Branched academic journey.</h2></div><p class="section-text">{{ profile.education_summary }}</p></div>
                <div class="education-branch">
                    {% for item in education %}
                    <article class="edu-node reveal">
                        <div class="edu-card">
                            <h3>{{ item.degree }}{% if item.field_of_study %} {{ item.field_of_study }}{% endif %}</h3>
                            <p class="edu-meta">{{ item.institution_name }}{% if item.description %} | {{ item.description }}{% endif %}</p>
                            <p class="section-text">{{ item.start_date or "" }}{% if item.end_date %} - {{ item.end_date }}{% endif %}{% if item.location %} | {{ item.location }}{% endif %}</p>
                        </div>
                        <div class="edu-dot">{{ item.badge or loop.index }}</div>
                    </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="section alt" id="skills">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Skills</p><h2>Skills mapped around backend development.</h2></div><p class="section-text">Technical strengths organized for quick recruiter scanning.</p></div>
                <div class="skill-map">
                    {% for category, items in grouped_skills.items() %}
                    <article class="flow-panel reveal">
                        <h3>{{ category }}</h3>
                        <div class="tag-list">{% for skill in items %}<span class="tag">{{ skill.name }}{% if skill.percentage %} · {{ skill.percentage }}%{% endif %}</span>{% endfor %}</div>
                    </article>
                    {% if loop.first %}<div class="skill-center reveal"><div><strong>AI + Backend</strong><p class="section-text">Building APIs, automations, and data-driven systems.</p></div></div>{% endif %}
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="section" id="projects">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Projects</p><h2>Project showcase.</h2></div><p class="section-text">Projects automatically loaded from the admin dashboard.</p></div>
                <div class="project-path">
                    {% for project in projects %}
                    <article class="project-card project-node reveal" data-step="{{ '%02d' % loop.index }}">
                        <div class="project-top">{% if project.project_image %}<img src="{{ project.project_image }}" alt="{{ project.title }}">{% else %}<span>{{ project.title }}</span>{% endif %}</div>
                        <div class="project-body">
                            <h3>{{ project.title }}</h3>
                            <p>{{ project.description }}</p>
                            <div class="tag-list">{% for tech in project.technologies_used|tags %}<span class="tag">{{ tech }}</span>{% endfor %}</div>
                            {% if project.detailed_description %}<ul class="feature-list">{% for line in project.detailed_description.split('\\n') %}<li>{{ line }}</li>{% endfor %}</ul>{% endif %}
                            <div class="card-actions">{% if project.github_url %}<a class="btn" href="{{ project.github_url }}" target="_blank" rel="noreferrer">GitHub</a>{% endif %}{% if project.live_demo_url %}<a class="btn" href="{{ project.live_demo_url }}" target="_blank" rel="noreferrer">Live Demo</a>{% endif %}</div>
                        </div>
                    </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="section alt" id="experience">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Experience</p><h2>Practical exposure and role readiness.</h2></div><p class="section-text">Experience entries update from the dashboard.</p></div>
                {% for item in experience %}
                <div class="experience-rail reveal"><div class="rail-label">{{ item.employment_type or "Role" }}</div><article class="flow-panel"><h3>{{ item.job_title }} | {{ item.company_name }}</h3><p class="section-text">{{ item.start_date or "" }}{% if item.end_date %} - {{ item.end_date }}{% endif %}</p><p>{{ item.description }}</p><ul class="feature-list">{% for line in item.responsibilities.split('\\n') if line %}<li>{{ line }}</li>{% endfor %}</ul></article></div>
                {% endfor %}
            </div>
        </section>

        <section class="section" id="certificates">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Certifications</p><h2>Certificate gallery.</h2></div><p class="section-text">Certificates appear here as soon as the admin publishes them.</p></div>
                <div class="certificate-gallery">
                    {% for cert in certificates %}
                    <article class="certificate-card reveal"><h3>{{ cert.certificate_name }}</h3><p>Issuer: {{ cert.issuing_organization }}</p><div class="tag-list">{% for tag in cert.skills|tags %}<span class="tag">{{ tag }}</span>{% endfor %}</div><div class="card-actions" style="margin-top: 18px;">{% if cert.verification_url %}<a class="btn" href="{{ cert.verification_url }}" target="_blank" rel="noreferrer">Verify</a>{% endif %}{% if cert.certificate_pdf %}<a class="btn" href="{{ cert.certificate_pdf }}">PDF</a>{% endif %}</div></article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="section alt" id="achievements">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Achievements</p><h2>Signals recruiters can verify.</h2></div><p class="section-text">Achievements, awards, and milestones managed dynamically.</p></div>
                <div class="grid-2"><ul class="list-stack reveal">{% for item in achievements %}<li class="achievement-item">{{ item.title }}: {{ item.description }}</li>{% endfor %}</ul><div class="flow-panel reveal"><h3>Coding Profiles</h3><div class="quick-links">{% for link in social_links %}<a class="profile-link" href="{{ link.url }}" target="_blank" rel="noreferrer"><strong>{{ link.platform }}</strong><span>{{ link.url }}</span></a>{% endfor %}</div></div></div>
            </div>
        </section>

        <section class="section" id="services">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Services</p><h2>What I can help build.</h2></div><p class="section-text">Service cards are editable from the admin dashboard.</p></div>
                <div class="grid-2">{% for service in services %}<article class="flow-panel reveal"><h3>{{ service.service_name }}</h3><p>{{ service.description }}</p></article>{% endfor %}</div>
            </div>
        </section>

        <section class="section alt" id="contact">
            <div class="section-pulse"></div>
            <div class="wrap">
                <div class="section-head reveal"><div><p class="section-label">Contact</p><h2>Ready for recruiter conversations.</h2></div><p class="section-text">The fastest ways to reach me for Software Engineer, Backend Developer, or Python Developer opportunities.</p></div>
                <div class="contact-layout">
                    <article class="contact-card reveal"><h3>Contact Details</h3><ul class="info-list"><li><strong>Email</strong><span>{{ profile.contact_email }}</span></li><li><strong>Phone</strong><span>{{ profile.phone_number }}</span></li><li><strong>Address</strong><span>{{ profile.address }}</span></li><li><strong>Hours</strong><span>{{ profile.working_hours }}</span></li></ul></article>
                    <form class="contact-card contact-form reveal" id="contact-form" method="post" action="/contact"><div class="field"><label for="name">Name</label><input id="name" name="name" type="text" placeholder="Recruiter name" required></div><div class="field"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="recruiter@example.com" required></div><div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="Tell me about the opportunity" required></textarea></div><button class="btn btn-primary" type="submit">Send Message</button><p class="form-note" id="form-note">Message captured.</p></form>
                </div>
            </div>
        </section>
    </main>
    <footer><div class="wrap footer-row"><span>{{ profile.footer_information }}</span><span>{{ profile.location }} | {{ profile.contact_email }}</span></div></footer>
    {% endblock %}
    """,
)

write(
    "templates/admin/base.html",
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }} | Portfolio Admin</title>
        <link rel="stylesheet" href="{{ url_for('static', path='css/style.css') }}">
    </head>
    <body class="admin-body">
        <div class="admin-shell">
            <aside class="admin-sidebar">
                <a class="brand" href="/admin"><span class="brand-mark">AP</span><span class="brand-text"><span>Portfolio</span><span>Super Admin</span></span></a>
                <nav class="admin-nav">
                    <a href="/admin">Overview</a>
                    <a href="/admin/profile">Profile & Hero</a>
                    {% for slug, resource in resources.items() %}<a href="/admin/{{ slug }}">{{ resource.label }}</a>{% endfor %}
                    <a href="/admin/media">Media</a>
                    <a href="/">View Site</a>
                </nav>
                <form method="post" action="/logout"><button class="logout-button" type="submit">Logout</button></form>
            </aside>
            <main class="admin-main">
                {% block content %}{% endblock %}
            </main>
        </div>
    </body>
    </html>
    """,
)

write(
    "templates/admin/login.html",
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admin Login</title>
        <link rel="stylesheet" href="{{ url_for('static', path='css/style.css') }}">
    </head>
    <body class="login-page">
        <form class="login-card" method="post" action="/login">
            <h1>Super User Login</h1>
            <p>Manage portfolio content securely.</p>
            {% if error %}<p class="alert">{{ error }}</p>{% endif %}
            <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autofocus></div>
            <div class="field"><label for="password">Password</label><input id="password" name="password" type="password" required></div>
            <button class="btn btn-primary" type="submit">Login</button>
        </form>
    </body>
    </html>
    """,
)

write(
    "templates/admin/dashboard.html",
    """
    {% extends "admin/base.html" %}
    {% block content %}
    <div class="admin-topbar"><div><h1>Dashboard</h1><p>Manage all portfolio sections from one place.</p></div><a class="btn btn-primary" href="/admin/projects/new">New Project</a></div>
    <section class="metric-grid">{% for label, value in counts.items() %}<article class="metric-card"><span>{{ label }}</span><strong>{{ value }}</strong></article>{% endfor %}</section>
    <section class="admin-panel"><div class="toolbar"><h2>Quick Actions</h2></div><div class="quick-links">{% for slug, resource in resources.items() %}<a class="btn" href="/admin/{{ slug }}/new">Add {{ resource.label }}</a>{% endfor %}</div></section>
    <section class="grid-2">
        <div class="admin-panel"><h2>Recent Activities</h2><ul class="recent-list">{% for item in recent %}<li><span>{{ item.action }}</span><small>{{ item.created_at }}</small></li>{% else %}<li>No activity yet.</li>{% endfor %}</ul></div>
        <div class="admin-panel"><h2>Recent Messages</h2><ul class="recent-list">{% for item in messages %}<li><span>{{ item.name }}: {{ item.message[:80] }}</span><small>{{ item.email }}</small></li>{% else %}<li>No messages yet.</li>{% endfor %}</ul></div>
    </section>
    {% endblock %}
    """,
)

write(
    "templates/admin/resource_list.html",
    """
    {% extends "admin/base.html" %}
    {% block content %}
    <div class="admin-topbar"><div><h1>{{ resource.label }}</h1><p>{{ total }} total records</p></div><a class="btn btn-primary" href="/admin/{{ resource.slug }}/new">Add New</a></div>
    <section class="admin-panel">
        <div class="toolbar">
            <form method="get"><input name="q" value="{{ q }}" placeholder="Search {{ resource.label }}"><select name="sort"><option value="display_order">Display Order</option><option value="id">ID</option><option value="{{ resource.title_field }}">Title</option></select><button class="btn" type="submit">Search</button></form>
        </div>
        <table class="admin-table">
            <thead><tr><th>ID</th><th>Title</th><th>Status</th><th>Order</th><th>Actions</th></tr></thead>
            <tbody>
            {% for item in items %}
            <tr><td>{{ item.id }}</td><td>{{ item|attr(resource.title_field) }}</td><td>{{ "Active" if item.is_active else "Hidden" }}</td><td>{{ item.display_order }}</td><td><div class="admin-actions"><a class="btn" href="/admin/{{ resource.slug }}/{{ item.id }}/edit">Edit</a><form method="post" action="/admin/{{ resource.slug }}/{{ item.id }}/delete"><button class="btn" type="submit">Delete</button></form></div></td></tr>
            {% else %}<tr><td colspan="5">No records found.</td></tr>{% endfor %}
            </tbody>
        </table>
        <div class="toolbar"><a class="btn" href="?q={{ q }}&page={{ page - 1 if page > 1 else 1 }}">Previous</a><span>Page {{ page }}</span><a class="btn" href="?q={{ q }}&page={{ page + 1 }}">Next</a></div>
    </section>
    {% endblock %}
    """,
)

write(
    "templates/admin/resource_form.html",
    """
    {% extends "admin/base.html" %}
    {% block content %}
    <div class="admin-topbar"><div><h1>{{ title }}</h1><p>{{ resource.label }} content editor</p></div><a class="btn" href="/admin/{{ resource.slug }}">Back</a></div>
    <section class="admin-panel">
        <form class="admin-form" method="post" enctype="multipart/form-data">
            {% for field in resource.fields %}
            <div class="field {% if field.wide %}wide{% endif %}">
                {% set value = item|attr(field.name) if item else "" %}
                {% if field.kind == "checkbox" %}
                <label class="check-field"><input name="{{ field.name }}" type="checkbox" {% if value or not item %}checked{% endif %}> {{ field.label }}</label>
                {% elif field.kind == "textarea" %}
                <label for="{{ field.name }}">{{ field.label }}</label><textarea id="{{ field.name }}" name="{{ field.name }}" {% if field.required %}required{% endif %}>{{ value or "" }}</textarea>
                {% elif field.kind == "file" %}
                <label for="{{ field.name }}">{{ field.label }}</label><input id="{{ field.name }}" name="{{ field.name }}" type="file">{% if value %}<small>Current: <a href="{{ value }}" target="_blank">{{ value }}</a></small>{% endif %}
                {% else %}
                <label for="{{ field.name }}">{{ field.label }}</label><input id="{{ field.name }}" name="{{ field.name }}" type="{{ field.kind }}" value="{{ value or "" }}" {% if field.required %}required{% endif %}>
                {% endif %}
            </div>
            {% endfor %}
            <div class="form-actions"><button class="btn btn-primary" type="submit">Save</button><a class="btn" href="/admin/{{ resource.slug }}">Cancel</a></div>
        </form>
    </section>
    {% endblock %}
    """,
)

write(
    "templates/admin/profile_form.html",
    """
    {% extends "admin/base.html" %}
    {% block content %}
    <div class="admin-topbar"><div><h1>Profile, Hero, Contact</h1><p>Update the global website information and hero section.</p></div><a class="btn" href="/admin">Back</a></div>
    <section class="admin-panel">
        <form class="admin-form" method="post" enctype="multipart/form-data">
            {% for field in fields %}
            {% set wide = field in ["hero_description", "about_content", "about_me", "biography", "personal_details", "education_summary", "career_summary"] %}
            <div class="field {% if wide %}wide{% endif %}"><label for="{{ field }}">{{ field.replace("_", " ").title() }}</label>{% if wide %}<textarea id="{{ field }}" name="{{ field }}">{{ profile|attr(field) or "" }}</textarea>{% else %}<input id="{{ field }}" name="{{ field }}" value="{{ profile|attr(field) or "" }}">{% endif %}</div>
            {% endfor %}
            {% for file_field in ["profile_photo", "resume_pdf", "portfolio_logo", "hero_background_image", "hero_profile_image"] %}
            <div class="field"><label for="{{ file_field }}">{{ file_field.replace("_", " ").title() }}</label><input id="{{ file_field }}" name="{{ file_field }}" type="file">{% if profile|attr(file_field) %}<small>Current: <a href="{{ profile|attr(file_field) }}" target="_blank">{{ profile|attr(file_field) }}</a></small>{% endif %}</div>
            {% endfor %}
            <div class="form-actions"><button class="btn btn-primary" type="submit">Save Profile</button></div>
        </form>
    </section>
    {% endblock %}
    """,
)

write(
    "templates/admin/media.html",
    """
    {% extends "admin/base.html" %}
    {% block content %}
    <div class="admin-topbar"><div><h1>Media Manager</h1><p>Upload and manage images, PDFs, and portfolio assets.</p></div></div>
    <section class="admin-panel">
        <form class="admin-form" method="post" enctype="multipart/form-data"><div class="field"><label for="file">File</label><input id="file" name="file" type="file" required></div><div class="field"><label for="alt_text">Alt Text</label><input id="alt_text" name="alt_text"></div><div class="form-actions"><button class="btn btn-primary" type="submit">Upload</button></div></form>
    </section>
    <section class="admin-panel">
        <table class="admin-table"><thead><tr><th>Name</th><th>Type</th><th>Size</th><th>Path</th><th>Actions</th></tr></thead><tbody>{% for file in files %}<tr><td>{{ file.original_name }}</td><td>{{ file.file_type }}</td><td>{{ file.file_size }}</td><td><a href="{{ file.file_path }}" target="_blank">{{ file.file_path }}</a></td><td><form method="post" action="/admin/media/{{ file.id }}/delete"><button class="btn" type="submit">Delete</button></form></td></tr>{% else %}<tr><td colspan="5">No files uploaded yet.</td></tr>{% endfor %}</tbody></table>
    </section>
    {% endblock %}
    """,
)

write("static/css/style.css", BASE_CSS + ADMIN_CSS)
write("static/js/app.js", APP_JS)

write(
    "requirements.txt",
    """
    fastapi==0.115.6
    uvicorn[standard]==0.34.0
    SQLAlchemy==2.0.36
    pydantic[email]==2.10.4
    python-jose[cryptography]==3.3.0
    passlib[bcrypt]==1.7.4
    bcrypt==4.2.1
    python-multipart==0.0.20
    Jinja2==3.1.5
    alembic==1.14.0
    python-dotenv==1.0.1
    psycopg2-binary==2.9.10
    """,
)

write(
    ".env.example",
    """
    PROJECT_NAME="Dynamic Portfolio"
    SECRET_KEY="replace-with-a-long-random-secret"
    JWT_ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=480
    DATABASE_URL="sqlite:///./portfolio.db"
    ADMIN_EMAIL="admin@example.com"
    ADMIN_PASSWORD="ChangeMe123!"
    MAX_UPLOAD_SIZE_MB=10
    """,
)
write(
    ".env",
    """
    PROJECT_NAME="Dynamic Portfolio"
    SECRET_KEY="development-only-change-me"
    JWT_ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=480
    DATABASE_URL="sqlite:///./portfolio.db"
    ADMIN_EMAIL="admin@example.com"
    ADMIN_PASSWORD="ChangeMe123!"
    MAX_UPLOAD_SIZE_MB=10
    """,
)

write(
    "alembic.ini",
    """
    [alembic]
    script_location = alembic
    sqlalchemy.url = sqlite:///./portfolio.db

    [loggers]
    keys = root,sqlalchemy,alembic

    [handlers]
    keys = console

    [formatters]
    keys = generic

    [logger_root]
    level = WARN
    handlers = console
    qualname =

    [logger_sqlalchemy]
    level = WARN
    handlers =
    qualname = sqlalchemy.engine

    [logger_alembic]
    level = INFO
    handlers =
    qualname = alembic

    [handler_console]
    class = StreamHandler
    args = (sys.stderr,)
    level = NOTSET
    formatter = generic

    [formatter_generic]
    format = %(levelname)-5.5s [%(name)s] %(message)s
    datefmt = %H:%M:%S
    """,
)

write(
    "alembic/env.py",
    """
    from logging.config import fileConfig
    import os
    import sys
    from pathlib import Path

    from alembic import context
    from sqlalchemy import engine_from_config, pool

    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from app.config import get_settings
    from app.database import Base
    import app.models  # noqa: F401


    config = context.config
    config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL", get_settings().DATABASE_URL))
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)
    target_metadata = Base.metadata


    def run_migrations_offline():
        url = config.get_main_option("sqlalchemy.url")
        context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
        with context.begin_transaction():
            context.run_migrations()


    def run_migrations_online():
        connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
        with connectable.connect() as connection:
            context.configure(connection=connection, target_metadata=target_metadata)
            with context.begin_transaction():
                context.run_migrations()


    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
    """,
)

write(
    "alembic/versions/0001_initial.py",
    """
    \"\"\"Initial portfolio schema

    Revision ID: 0001_initial
    Revises:
    Create Date: 2026-06-19
    \"\"\"

    from alembic import op

    from app.database import Base
    import app.models  # noqa: F401


    revision = "0001_initial"
    down_revision = None
    branch_labels = None
    depends_on = None


    def upgrade() -> None:
        Base.metadata.create_all(bind=op.get_bind())


    def downgrade() -> None:
        Base.metadata.drop_all(bind=op.get_bind())
    """,
)

write(
    "README.md",
    """
    # Dynamic FastAPI Portfolio

    This project upgrades the original Django/static portfolio into a FastAPI full-stack application with a database-driven public site and a protected Super User dashboard.

    ## What Is Included

    - FastAPI application in `app/`
    - SQLAlchemy models for users, profile information, skills, education, experience, projects, certificates, achievements, services, testimonials, social links, media files, contact messages, and activity logs
    - Pydantic schemas in `app/schemas.py`
    - JWT login, bcrypt password hashing, protected admin routes, and logout
    - Admin dashboard with counts, search, pagination, sorting, quick actions, recent activity, and media uploads
    - Dynamic Jinja2 portfolio templates
    - Separated CSS in `static/css/style.css`
    - Separated JavaScript in `static/js/app.js`
    - Alembic setup and initial migration
    - SQLite by default, PostgreSQL-ready through `DATABASE_URL`

    ## Installation

    ```bash
    python -m venv .venv
    .venv\\Scripts\\activate
    pip install -r requirements.txt
    copy .env.example .env
    alembic upgrade head
    uvicorn app.main:app --reload
    ```

    Open:

    - Public site: http://127.0.0.1:8000/
    - Admin dashboard: http://127.0.0.1:8000/admin

    Default development admin:

    - Email: `admin@example.com`
    - Password: `ChangeMe123!`

    Change these immediately in `.env` before deployment.

    ## API Examples

    Authenticate:

    ```bash
    curl -X POST http://127.0.0.1:8000/api/login ^
      -H "Content-Type: application/json" ^
      -d "{\\"email\\":\\"admin@example.com\\",\\"password\\":\\"ChangeMe123!\\"}"
    ```

    Use the returned bearer token for protected endpoints:

    - `GET /api/projects`
    - `POST /api/projects`
    - `PUT /api/projects/{id}`
    - `DELETE /api/projects/{id}`

    Equivalent CRUD endpoints exist for:

    - `/api/skills`
    - `/api/education`
    - `/api/experience`
    - `/api/certificates`
    - `/api/achievements`
    - `/api/services`
    - `/api/testimonials`
    - `/api/social-links`

    ## Database

    Development uses SQLite:

    ```env
    DATABASE_URL="sqlite:///./portfolio.db"
    ```

    PostgreSQL deployment only requires changing the URL:

    ```env
    DATABASE_URL="postgresql+psycopg2://user:password@host:5432/portfolio"
    ```

    Then run:

    ```bash
    alembic upgrade head
    ```

    ## Deployment Guide

    1. Set a strong `SECRET_KEY`.
    2. Set `ADMIN_EMAIL` and `ADMIN_PASSWORD` for the first boot, then rotate the password.
    3. Use PostgreSQL for production.
    4. Serve uploaded files from durable storage or a mounted volume.
    5. Run behind HTTPS.
    6. Start with a production ASGI server command such as:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

    7. Put Nginx, Caddy, or a platform router in front for TLS, compression, static caching, and upload limits.

    ## Folder Structure

    ```text
    app/
      auth/
      database/
      routes/
      services/
      utils/
      main.py
      models.py
      schemas.py
    alembic/
    static/
      css/
      docs/
      js/
      uploads/
      videos/
    templates/
      admin/
      base.html
      index.html
    requirements.txt
    .env.example
    ```
    """,
)

write(
    "run_dev_server.cmd",
    r"""
    @echo off
    cd /d "C:\Users\Dell\My_portfolio_10"
    "C:\Users\Dell\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload > "C:\Users\Dell\My_portfolio_10\server-out.log" 2> "C:\Users\Dell\My_portfolio_10\server-err.log"
    """,
)

for folder in ["static/uploads", "static/docs", "static/videos", "static/images"]:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

asset_pairs = [
    ("core/portfolio/static/portfolio/docs/resume.pdf", "static/docs/resume.pdf"),
    ("core/portfolio/static/portfolio/videos/hero-background.mp4", "static/videos/hero-background.mp4"),
]
for source, dest in asset_pairs:
    src = ROOT / source
    dst = ROOT / dest
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

print("FastAPI portfolio scaffold generated.")
