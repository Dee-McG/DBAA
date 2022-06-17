from django.urls import path
from .views import CreateEventView, DeleteEventView, EditEventView, EventList, EventGoing, EventDetailView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name="create_event"),
    path('events/', EventList.as_view(), name='events'),
    path('view/<slug:pk>/', EventDetailView.as_view(), name="view_event"),
    path('edit/<slug:pk>/', EditEventView.as_view(), name="edit_event"),
    path('delete/<slug:pk>/', DeleteEventView.as_view(), name="delete_event"),
    path('going/<int:pk>', EventGoing, name="going_event"),
]
