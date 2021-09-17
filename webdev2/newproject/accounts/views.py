from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Repository
from datetime import datetime
from django.db.models.signals import post_save
import requests
import os
from urllib.parse import urljoin
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/login')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/reg_form.html', args)

def explore(request):
    users=User.objects.all()  
    args = {'users': users} 
    return render(request,'accounts/explore.html', args)  

def profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html',args)

def update(request,pk=None):
    curr_user = User.objects.get(pk=pk)
    profile = Profile.objects.filter(user=curr_user)
    profile.delete()
    response = requests.get(urljoin('https://api.github.com/users/',curr_user.username))
    if response.status_code != 200:
        user_profile = Profile.objects.create(user=curr_user, title = curr_user.username)
        user_profile.save()
    else:
        d = response.json()
        user_profile = Profile.objects.create(user=curr_user, followernumber = int(d['followers']), title = curr_user.username)
        user_profile.save()

    str = urljoin('https://api.github.com/users/',user_profile.title+'/')
    responserepo = requests.get(urljoin(str,'repos'))
    if responserepo.status_code == 200:
        drepo = responserepo.json()
        for i in range(len(drepo)):
            rep = Repository.objects.create(owner = user_profile, repname=drepo[i]['name'], starrating = drepo[i]['stargazers_count'])

    user = User.objects.get(pk=pk)
    args = {'user': user}
    return render(request, 'accounts/profile.html',args)
