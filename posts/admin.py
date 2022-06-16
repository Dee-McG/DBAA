from django.contrib import admin
from .models import Post, Reply


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


class ReplyAdmin(admin.ModelAdmin):
    """
    Class to view Replies on the admin panel
    """
    list_display = (
        'rid',
        'user',
        'body',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)