"""
Portfolio Models for Abijay AP's Portfolio Website
This module defines the database models for storing portfolio information.
"""

from django.db import models


class Profile(models.Model):
    """
    Model to store personal profile information.
    Only one instance should exist (singleton pattern).
    """
    name = models.CharField(max_length=100, default="Abijay AP")
    title = models.CharField(max_length=200, default="Data Analytics & Python Developer")
    email = models.EmailField(default="abijayap50@gmail.com")
    phone = models.CharField(max_length=20, default="7356741669")
    location = models.CharField(max_length=200, default="Palakkad, Kerala")
    linkedin = models.URLField(default="https://linkedin.com/in/abijay-ap-2004")
    profile_summary = models.TextField(
        default="Completed virtual internships and real-world projects in Data Analytics and Data Science using Python, SQL, and Power BI. Skilled in data cleaning, EDA, and building machine learning models with scikit-learn. Proficient in tools like Pandas, NumPy, Matplotlib, and Seaborn, with hands-on experience in creating dashboards and extracting insights from structured data."
    )
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    Model to store technical skills with categories.
    """
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('data_analysis', 'Data Analysis'),
        ('visualization', 'Visualization Tools'),
        ('tools', 'Tools & Platforms'),
        ('other', 'Other Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=80, help_text="Skill proficiency percentage (0-100)")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    
    class Meta:
        ordering = ['category', '-proficiency']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    """
    Model to store portfolio projects.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies used")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_completed', '-id']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """Return technologies as a list."""
        return [tech.strip() for tech in self.technologies.split(',')]


class Education(models.Model):
    """
    Model to store educational background.
    """
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently studying")
    description = models.TextField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Education"
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certificate(models.Model):
    """
    Model to store professional certifications.
    """
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    skills_gained = models.TextField(blank=True, null=True, help_text="Skills learned from this certification")
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"


class ContactMessage(models.Model):
    """
    Model to store contact form submissions.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class SocialLink(models.Model):
    """
    Model to store social media links.
    """
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('other', 'Other'),
    ]
    
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, default="fab fa-linkedin")
    
    class Meta:
        ordering = ['platform']
    
    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"
