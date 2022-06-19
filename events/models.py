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
    image = models.ImageField(upload_to="event_images/", blank=True)
    e_time = models.DateTimeField(blank=False)
    date = models.DateTimeField(auto_now=True)
    going = models.ManyToManyField(User, related_name="going_event", blank=True)
    location = models.CharField(max_length=160, blank=False, default="Not Provided")
    fee = models.DecimalField(default=0, help_text="$", decimal_places=2, max_digits=5)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def number_of_going(self):
        return self.going.count()


class CommentEvent(models.Model):
    """
    Comment event model
    """
    user = models.ForeignKey(User, related_name='event_user', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="comment_event", on_delete=models.CASCADE)
    body = RichTextField(max_length=10000, null=False, blank=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.body)


class EventNumbers(models.Model):
    """
    Event model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_numbers')

    def __str__(self):
        return self.event.title
