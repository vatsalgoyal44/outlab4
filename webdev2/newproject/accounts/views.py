from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts')
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