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
    "contact-messages": Resource("contact-messages", "Inbox/Messages", models.ContactMessage, "name", (
        Field("name", "Name"),
        Field("email", "Email"),
        Field("message", "Message", "textarea", wide=True),
        Field("is_read", "Read Status", "checkbox"),
    ), ("name", "email", "message")),
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
