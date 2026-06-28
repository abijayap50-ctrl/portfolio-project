from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50) # e.g., 'Python'
    # Field to store the path to the SVG/icon for that skill
    icon = models.FileField(upload_to='skills/icons/', blank=True) 

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100) # e.g., 'Django Card'
    description = models.TextField() # e.g., 'Summary details...'
    github_link = models.URLField(blank=True) 
    live_link = models.URLField(blank=True)
    image = models.FileField(upload_to='projects/cards/', blank=True, null=True) # For your "Project Cards"
    
    def __str__(self):
        return self.title
