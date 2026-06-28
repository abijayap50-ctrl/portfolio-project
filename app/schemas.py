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
