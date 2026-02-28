from django import forms
from .models import User, Profile 
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    """ 
    UserCreationForm handles password1, password2, hashing. 
    Tell the form to use email instead of username
    """
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class LoginForm(forms.Form):
    """
    Not a ModelForm - you are not creating/editing a model 
    but collecting credentials
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name" , "avatar", "phone", "bio"]

# TODO: Email forms
# class EmailChangeForm
# class PasswordChangeForm