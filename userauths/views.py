from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User
from .forms import UserRegisterForm


# Create your views here.

def RegisterView (request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, Your account was created succeffuly.")

            new_user = authenticate(username=form.cleaned_data["email"],
                                    password=form.cleaned_data["password1"])
            
            login(request, new_user)
            return redirect ("core:index")
    
    if request.user.is_authenticated:
        messages.warning(request, "You are already Logged in.")
        return redirect ("core:index")
    
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'userauths/sign-up.html', context)