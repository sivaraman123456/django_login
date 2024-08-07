from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Signup
from django import forms
from django.contrib.auth.hashers import make_password
class CreateUserForm(UserCreationForm): # override the class
    class Meta:
        model= User
        fields=['username','email','password1','password2']

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields=["name",'email',"password"]
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
