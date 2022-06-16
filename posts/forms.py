from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Post


class PostForm (forms.ModelForm):
    """ Form to create and edit Posts """
    class Meta:
        model = Post
        # specify fields
        fields = ['title', 'body', 'image']

        labels = {
            'title': 'Title',
            'body': 'Body',
            'image': 'Image'
        }
    
        body = forms.CharField(widget=RichTextWidget())
