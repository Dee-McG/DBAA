from django.urls import path
from .views import (
    EditAvatarView,
    EditDetailsView,
    UserDetailView,
    UserEventView,
    UserProfileView
)

urlpatterns = [
    path('<slug:pk>/', UserProfileView.as_view(), name="profile"),
    path('details/<slug:pk>/', UserDetailView.as_view(), name="view_details"),
    path('edit-avatar/<slug:pk>/',
         EditAvatarView.as_view(), name="edit_avatar"),
    path('edit-details/<slug:pk>/',
         EditDetailsView.as_view(), name="edit_details"),
    path('view-events/<slug:pk>/', UserEventView.as_view(),
         name="view_profile_events")
]
