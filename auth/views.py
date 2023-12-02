from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been registered as a user successfully')
            return redirect('signup-url')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {"form": form})


def login(request):
    return render(request, 'dairy/choose_activity.html')
