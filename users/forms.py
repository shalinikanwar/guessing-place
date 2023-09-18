from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','age','place'] # Add other fields as needed
