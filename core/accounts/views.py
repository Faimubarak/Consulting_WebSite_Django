from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile
from .forms import UserForm , ProfileForm , UserCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages


#View for user sgin up to check the user information
def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})


#Get the user profile for user who log in on page
def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})


#Edit the proflie and user information
def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)
        if profile_form.is_valid():
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    else:
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{'profile_form' : profile_form})






