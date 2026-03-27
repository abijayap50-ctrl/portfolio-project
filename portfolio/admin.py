"""
Admin configuration for the Portfolio app.
This module registers all models to the Django admin interface.
"""

from django.contrib import admin
from .models import (
    Profile, Skill, Project, Education, 
    Certificate, ContactMessage, SocialLink
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for Profile model."""
    list_display = ['name', 'title', 'email', 'phone', 'location']
    fields = ['name', 'title', 'email', 'phone', 'location', 'linkedin', 
              'profile_summary', 'profile_image', 'resume']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin configuration for Skill model."""
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for Project model."""
    list_display = ['title', 'date_completed', 'is_featured']
    list_filter = ['is_featured', 'date_completed']
    search_fields = ['title', 'description']
    date_hierarchy = 'date_completed'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin configuration for Education model."""
    list_display = ['degree', 'institution', 'location', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current']
    search_fields = ['degree', 'institution']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Admin configuration for Certificate model."""
    list_display = ['title', 'issuing_organization', 'issue_date']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['title', 'issuing_organization']
    date_hierarchy = 'issue_date'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin configuration for ContactMessage model."""
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    date_hierarchy = 'created_at'


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    """Admin configuration for SocialLink model."""
    list_display = ['platform', 'url']
    list_filter = ['platform']
