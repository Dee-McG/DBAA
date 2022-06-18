from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserAvatarForm(forms.ModelForm):
    "User image form"

    class Meta:
        model = UserProfile
        fields = ["avatar"]
        avatar = forms.ImageField(label="Image", required=False)


class UserDetailForm(forms.ModelForm):
    "User detail form"

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
