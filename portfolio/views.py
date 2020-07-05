from django.shortcuts import render
from .models import Project
# Create your views here.


def HomeView(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'prj': projects})
