"""Forms used for user information.

User registration and profile update forms
"""

from django                     import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models                    import Profile


class UserRegisterForm(UserCreationForm):
    """Form used for new user registration"""
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """Form used to update existing user info"""
    email = forms.EmailField()

    class Meta:
        model   = User
        fields  = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """For used to update user profile picture"""
    class Meta:
        model   = Profile
        fields  = ['image']