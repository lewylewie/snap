from django import forms
from .models import Profile, Comment
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image_cover', 'image_caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

