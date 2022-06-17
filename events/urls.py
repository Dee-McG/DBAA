from django.urls import path
from . import views
from .views import CreateEventView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name="create_event"),
    path('events/', views.EventList.as_view(), name='events'),
]
