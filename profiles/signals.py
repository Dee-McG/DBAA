from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Signal to create a new profile when new user is created"""
    if created:
        UserProfile.objects.create(user=instance)
