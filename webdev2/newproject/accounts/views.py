from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm

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