"""
Views for the Portfolio app.
This module contains all the view functions for rendering portfolio pages.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Profile, Skill, Project, Education, 
    Certificate, ContactMessage, SocialLink
)


class HomeView(TemplateView):
    """
    Main home view that displays the complete portfolio.
    This is a single-page portfolio with all sections.
    """
    template_name = 'portfolio/index.html'
    
    def get_context_data(self, **kwargs):
        """Add all portfolio data to the context."""
        context = super().get_context_data(**kwargs)
        
        # Get or create profile (use first one if multiple exist)
        profile = Profile.objects.first()
        if not profile:
            # Create default profile if none exists
            profile = Profile.objects.create()
        context['profile'] = profile
        
        # Get all skills grouped by category
        skills = Skill.objects.all()
        skills_by_category = {}
        for skill in skills:
            category = skill.get_category_display()
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append(skill)
        context['skills_by_category'] = skills_by_category
        context['skills'] = skills
        
        # Get all projects
        context['projects'] = Project.objects.all()
        context['featured_projects'] = Project.objects.filter(is_featured=True)
        
        # Get all education entries
        context['education'] = Education.objects.all()
        
        # Get all certificates
        context['certificates'] = Certificate.objects.all()
        
        # Get social links
        context['social_links'] = SocialLink.objects.all()
        
        return context


def contact_submit(request):
    """
    Handle contact form submission via AJAX.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Save the message to database
            contact_msg = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Optionally send email notification
            try:
                profile = Profile.objects.first()
                if profile and profile.email:
                    send_mail(
                        f"Portfolio Contact: {subject}",
                        f"From: {name} <{email}>\n\n{message}",
                        email,
                        [profile.email],
                        fail_silently=True,
                    )
            except Exception:
                pass  # Silently fail if email sending fails
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! I will get back to you soon.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def download_resume(request):
    """
    Serve the resume file for download.
    """
    profile = get_object_or_404(Profile)
    if profile.resume:
        response = redirect(profile.resume.url)
        return response
    else:
        messages.error(request, "Resume not available for download.")
        return redirect('home')
