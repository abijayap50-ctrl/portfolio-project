"""
Script to populate the portfolio database with resume data.
Run this script to initialize the database with default data.
"""

import os
import sys
import django

# Setup Django environment
sys.path.append('/home/z/my-project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Profile, Skill, Project, Education, Certificate, SocialLink


def populate_database():
    """Populate the database with resume data."""
    
    # Clear existing data (optional - comment out if you want to keep existing data)
    # Profile.objects.all().delete()
    # Skill.objects.all().delete()
    # Project.objects.all().delete()
    # Education.objects.all().delete()
    # Certificate.objects.all().delete()
    # SocialLink.objects.all().delete()
    
    # =============================================
    # Create Profile
    # =============================================
    profile, created = Profile.objects.get_or_create(
        defaults={
            'name': 'Abijay AP',
            'title': 'Data Analytics & Python Developer',
            'email': 'abijayap50@gmail.com',
            'phone': '7356741669',
            'location': 'Palakkad, Kerala',
            'linkedin': 'https://linkedin.com/in/abijay-ap-2004',
            'profile_summary': 'Completed virtual internships and real-world projects in Data Analytics and Data Science using Python, SQL, and Power BI. Skilled in data cleaning, EDA, and building machine learning models with scikit-learn. Proficient in tools like Pandas, NumPy, Matplotlib, and Seaborn, with hands-on experience in creating dashboards and extracting insights from structured data.'
        }
    )
    print(f"{'Created' if created else 'Already exists'}: Profile - {profile.name}")
    
    # =============================================
    # Create Skills
    # =============================================
    skills_data = [
        # Programming Languages
        {'name': 'Python', 'category': 'programming', 'proficiency': 90, 'icon': 'fab fa-python'},
        {'name': 'SQL', 'category': 'programming', 'proficiency': 85, 'icon': 'fas fa-database'},
        
        # Data Analysis
        {'name': 'Pandas', 'category': 'data_analysis', 'proficiency': 88, 'icon': 'fas fa-chart-bar'},
        {'name': 'NumPy', 'category': 'data_analysis', 'proficiency': 85, 'icon': 'fas fa-calculator'},
        {'name': 'Matplotlib', 'category': 'data_analysis', 'proficiency': 82, 'icon': 'fas fa-chart-line'},
        {'name': 'Seaborn', 'category': 'data_analysis', 'proficiency': 80, 'icon': 'fas fa-chart-pie'},
        {'name': 'Scikit-learn', 'category': 'data_analysis', 'proficiency': 75, 'icon': 'fas fa-brain'},
        
        # Visualization Tools
        {'name': 'Power BI', 'category': 'visualization', 'proficiency': 85, 'icon': 'fas fa-chart-area'},
        {'name': 'Excel', 'category': 'visualization', 'proficiency': 80, 'icon': 'fas fa-table'},
        
        # Tools & Platforms
        {'name': 'Git', 'category': 'tools', 'proficiency': 75, 'icon': 'fab fa-git-alt'},
        {'name': 'Jupyter Notebook', 'category': 'tools', 'proficiency': 90, 'icon': 'fas fa-book'},
        {'name': 'Linux CLI', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-linux'},
    ]
    
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            defaults=skill_data
        )
        print(f"{'Created' if created else 'Already exists'}: Skill - {skill.name}")
    
    # =============================================
    # Create Projects
    # =============================================
    projects_data = [
        {
            'title': 'Power BI Company Sales Report',
            'description': 'Cleaned and transformed raw sales data using Power Query. Designed interactive charts and visuals to analyze sales performance. Built a dynamic dashboard to track key metrics and identify trends. This project demonstrates proficiency in data visualization and business intelligence.',
            'technologies': 'Power BI, Power Query, DAX, Excel',
            'is_featured': True,
        },
        {
            'title': 'Gmail Fraud Detection Analyst',
            'description': 'Monitored and investigated Gmail-related fraud activities including phishing, account takeover (ATO), spoofing, and business email compromise (BEC) through log analysis, IP tracking, and behavioral anomaly detection. Applied risk scoring models and email authentication protocols (SPF, DKIM, DMARC) to identify suspicious patterns, reduce fraud exposure, and improve detection accuracy.',
            'technologies': 'Threat Intelligence, Log Analysis, SPF/DKIM/DMARC, Risk Scoring',
            'is_featured': True,
        },
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        print(f"{'Created' if created else 'Already exists'}: Project - {project.title}")
    
    # =============================================
    # Create Education
    # =============================================
    from datetime import date
    
    education_data = [
        {
            'degree': 'B-Tech Artificial Intelligence and Data Science',
            'institution': 'JCT College of Engineering and Technology | Anna University',
            'location': 'Pichanur, Tamil Nadu',
            'start_date': date(2022, 9, 1),
            'is_current': True,
        },
        {
            'degree': 'Higher Secondary Education',
            'institution': 'GHSS Mankara',
            'location': 'Palakkad, Kerala',
            'start_date': date(2020, 6, 1),
            'end_date': date(2022, 5, 31),
            'is_current': False,
        },
        {
            'degree': 'SSLC',
            'institution': 'Seva Sadan Central School',
            'location': 'Palakkad, Kerala',
            'start_date': date(2020, 4, 1),
            'end_date': date(2020, 4, 30),
            'is_current': False,
        },
    ]
    
    for edu_data in education_data:
        edu, created = Education.objects.get_or_create(
            degree=edu_data['degree'],
            institution=edu_data['institution'],
            defaults=edu_data
        )
        print(f"{'Created' if created else 'Already exists'}: Education - {edu.degree}")
    
    # =============================================
    # Create Certificates
    # =============================================
    certificates_data = [
        {
            'title': 'Tools of the Trade: Linux and SQL',
            'issuing_organization': 'Google',
            'skills_gained': 'SQL, Linux CLI, Cloud VM usage',
            'description': 'Comprehensive course on Linux command line and SQL fundamentals for data analysis.',
        },
        {
            'title': 'Tata Data Visualisation: Empowering Business with Effective Insights',
            'issuing_organization': 'Tata Consultancy Services',
            'skills_gained': 'Data Visualization, Decision Making, Business Analysis',
            'description': 'Job simulation program creating data visualizations for Tata Consultancy Services. Created visuals for data analysis to help executives with effective decision making.',
        },
    ]
    
    for cert_data in certificates_data:
        cert, created = Certificate.objects.get_or_create(
            title=cert_data['title'],
            issuing_organization=cert_data['issuing_organization'],
            defaults=cert_data
        )
        print(f"{'Created' if created else 'Already exists'}: Certificate - {cert.title}")
    
    # =============================================
    # Create Social Links
    # =============================================
    social_links_data = [
        {'platform': 'linkedin', 'url': 'https://linkedin.com/in/abijay-ap-2004', 'icon_class': 'fab fa-linkedin-in'},
        {'platform': 'github', 'url': 'https://github.com/', 'icon_class': 'fab fa-github'},
    ]
    
    for link_data in social_links_data:
        link, created = SocialLink.objects.get_or_create(
            platform=link_data['platform'],
            defaults=link_data
        )
        print(f"{'Created' if created else 'Already exists'}: Social Link - {link.get_platform_display()}")
    
    print("\n" + "="*50)
    print("Database population completed successfully!")
    print("="*50)


if __name__ == '__main__':
    populate_database()
