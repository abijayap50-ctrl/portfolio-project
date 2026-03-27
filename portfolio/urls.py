"""
URL configuration for the Portfolio app.
"""

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('resume/download/', views.download_resume, name='download_resume'),
]
