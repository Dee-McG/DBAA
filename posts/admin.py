from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Class to view Posts on the admin panel
    """
    list_display = (
        'did',
        'user',
        'title',
        'body',
    )

admin.site.register(Post, PostAdmin)