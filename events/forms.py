from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Event, CommentEvent
from .widget import DatePickerInput


class EventForm(forms.ModelForm):
    """
    Form to create an event
    """
    class Meta:
        model = Event
        fields = ["title", "body", "e_time", "image", "location", "fee"]

        labels = {
            "title": "Title",
            "body": "Body",
            "e_time": "Event date",
            "image": "Image",
            "location": "Event Location",
            "Fee": "Admission Fee"
        }

        body = forms.CharField(widget=RichTextWidget())

        widgets = {
            "e_time": DatePickerInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            })
        }


class EventCommentForm (forms.ModelForm):

    class Meta:
        model = CommentEvent
        # specify fields
        fields = ['body']
        labels = {
            'body': 'Comment',
        }
        comment = forms.CharField(widget=RichTextWidget())
