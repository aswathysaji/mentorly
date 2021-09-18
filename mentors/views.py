from django.shortcuts import render
from . models import Mentor

# Create your views here.
def mentor(request):
    mentors = Mentor.objects.all()
    print(mentors)
    return render(request,'home.html',{
        "mentors" : mentors
    })

def home(request):
    return render(request,'home.html',{})
