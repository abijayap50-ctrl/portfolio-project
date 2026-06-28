from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password
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
    user = db.query(User).filter(User.role == "superuser").first()
    if user:
        if user.email != settings.ADMIN_EMAIL or not verify_password(settings.ADMIN_PASSWORD, user.hashed_password):
            user.email = settings.ADMIN_EMAIL
            user.hashed_password = hash_password(settings.ADMIN_PASSWORD)
            db.commit()
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
                personal_details="Primary language: Python\nBackend framework: Django\nDatabase logic: SQL",
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
        db.add(Experience(job_title="Add Internship", company_name="Company Name", employment_type="Internship", description="This section is ready for your internship or training details.", responsibilities="Add responsibility 1\nAdd responsibility 2\nAdd measurable impact", is_active=False))

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
