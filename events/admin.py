from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Class to view Event on the admin panel
    """
    list_display = (
        'user',
        'title',
        'body',
        'e_time',
    )


admin.site.register(Event, EventAdmin)
