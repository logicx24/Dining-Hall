from django import forms
from foodfinder.models import Food, Menu, UserProfile
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "preferences")