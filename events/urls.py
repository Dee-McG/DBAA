from django.urls import path
from .views import CreateEventView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name="create_event"),
]
