from django.shortcuts import render
from .models import Project

def home_view(request):
    projects=Project.objects.all()
    return render(request,'portfolio/index.html',{'projects':projects})




# Create your views here.
