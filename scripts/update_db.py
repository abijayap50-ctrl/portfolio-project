from app.database import SessionLocal
from app.models import Experience, SocialLink
from datetime import date

db = SessionLocal()
try:
    # Update or insert TapAcademy experience
    exp = db.query(Experience).first()
    if exp:
        exp.job_title = "Full Stack Web Development Intern"
        exp.company_name = "TapAcademy"
        exp.employment_type = "Internship"
        exp.start_date = date(2026, 6, 1)
        exp.is_active = True
        exp.description = (
            "Currently pursuing a Full Stack Web Development internship, where I am learning to build and develop "
            "web applications using modern technologies. I am improving my Python programming and SQL database skills "
            "through practical projects and gaining exposure to Agentic AI concepts such as LLMs, prompt engineering, "
            "and AI agents. I also use Git/GitHub for version control and follow best coding practices while working "
            "on real-world applications."
        )
        exp.responsibilities = "Python\nPython and Django Developer\nSQL\nSQLAlchemy\nORM"
        print("Updated experience in database.")
    else:
        exp = Experience(
            job_title="Full Stack Web Development Intern",
            company_name="TapAcademy",
            employment_type="Internship",
            start_date=date(2026, 6, 1),
            is_active=True,
            description=(
                "Currently pursuing a Full Stack Web Development internship, where I am learning to build and develop "
                "web applications using modern technologies. I am improving my Python programming and SQL database skills "
                "through practical projects and gaining exposure to Agentic AI concepts such as LLMs, prompt engineering, "
                "and AI agents. I also use Git/GitHub for version control and follow best coding practices while working "
                "on real-world applications."
            ),
            responsibilities="Python\nPython and Django Developer\nSQL\nSQLAlchemy\nORM"
        )
        db.add(exp)
        print("Added experience to database.")

    # Update GitHub social link
    git_link = db.query(SocialLink).filter(SocialLink.platform == "GitHub").first()
    if git_link:
        git_link.url = "https://github.com/abijayap50-ctrl/portfolio-project"
        print("Updated GitHub link in database.")
    else:
        git_link = SocialLink(
            platform="GitHub",
            url="https://github.com/abijayap50-ctrl/portfolio-project",
            display_order=2
        )
        db.add(git_link)
        print("Added GitHub link to database.")

    db.commit()
    print("Database updated successfully.")
finally:
    db.close()
