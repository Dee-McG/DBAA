from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Post, Reply


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


class ReplyForm (forms.ModelForm):

    class Meta:
        model = Reply
        # specify fields
        fields = ['body']
        labels = {
            'body': 'Reply',
        }
        reply = forms.CharField(widget=RichTextWidget())
