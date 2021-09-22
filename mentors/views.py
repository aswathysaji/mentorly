from django.shortcuts import render
from . models import Mentor

# Create your views here.

def home(request):
    mentors = Mentor.objects.all()
    return render(request,'home.html',{
        "mentors" : mentors
    })
