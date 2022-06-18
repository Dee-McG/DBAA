from django import forms

from .models import UserProfile


class UserAvatarForm(forms.ModelForm):
    "User image form"

    class Meta:
        model = UserProfile
        fields = ["avatar"]
        avatar = forms.ImageField(label="Image", required=False)
