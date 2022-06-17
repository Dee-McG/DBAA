from django.contrib import admin
from .models import Event, EventNumbers


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

class EventNumbersAdmin(admin.ModelAdmin):
    """
    Class to view EventNumbers on the admin panel
    """
    list_display = (
        'user',
        'event'
    )


admin.site.register(Event, EventAdmin)
admin.site.register(EventNumbers, EventNumbersAdmin)
