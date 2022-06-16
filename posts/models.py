from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
import cloudinary
import cloudinary.uploader
import uuid


class Post(models.Model):
    """
    Post model
    """
    user = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)
    did = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    title = models.CharField(max_length=250, null=False, blank=False)
    body = RichTextField(max_length=10000, null=False, blank=False)
    image = models.ImageField(upload_to='post_images/', blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.did)


class Reply(models.Model):
    """
    Reply model
    """
    user = models.ForeignKey(User, related_name='reply_user', on_delete=models.CASCADE)
    rid = models.ForeignKey(Post, related_name="post_reply", on_delete=models.CASCADE)
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    body = RichTextField(max_length=10000, null=False, blank=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body