from django import forms
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# form for sgin up
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# edit form for Django User info
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

# Edit the form for profile model 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','name','email','phone','address','city','state']
