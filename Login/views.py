from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.context_processors import login_redirect
import requests


def login(request):
    return render(request,'login.html')

@login_required
def home(request):
     username = request.user.username
     url = f"https://api.github.com/users/{username}/repos"     
     response = requests.get(url)
     repositories = response.json()
     return render(request,'home.html', {'repositories': repositories})




