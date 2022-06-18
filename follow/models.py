from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    """
    Model to allow users to follow others
    """
    user = models.ForeignKey(User, related_name='this_user', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)

    def __str__(self):
        return self.following.username