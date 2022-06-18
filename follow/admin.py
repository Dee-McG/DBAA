from django.contrib import admin
from .models import Follow


class FollowAdmin(admin.ModelAdmin):
    """
    Class to view followers on the admin panel
    """
    list_display = [
        'user',
        'following',
    ]


admin.site.register(Follow, FollowAdmin)