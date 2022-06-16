from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Event
from .widget import DatePickerInput


class EventForm(forms.ModelForm):
    """
    Form to create an event
    """
    class Meta:
        model = Event
        fields = ["title", "body", "e_time", "image"]

        labels = {
            "title": "Title",
            "body": "Body",
            "e_time": "Event date",
            "image": "Image"
        }

        body = forms.CharField(widget=RichTextWidget())

        widgets = {
            "e_time": DatePickerInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            })
        }
