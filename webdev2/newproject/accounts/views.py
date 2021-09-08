from django.shortcuts import redirect, render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html',args)