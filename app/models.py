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
