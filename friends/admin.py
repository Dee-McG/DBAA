from django.contrib import admin
from .models import Friend


class FriendAdmin(admin.ModelAdmin):
    """
    Class to view friends on the admin panel
    """
    list_display = [
        'user',
        'following',
    ]


admin.site.register(Friend, FriendAdmin)