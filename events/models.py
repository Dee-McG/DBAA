from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

class Event(models.Model):
    """
    Event model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, null=False, blank=False)
    body = RichTextField(max_length=10000, null=False, blank=False)
    image = models.ImageField(upload_to="event_images", blank=True)
    e_time = models.DateTimeField(blank=False)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def number_of_going(self):
        return self.going.count()

    def number_of_not_going(self):
        return self.not_going.count()

