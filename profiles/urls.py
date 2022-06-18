from django.urls import path
from .views import EditAvatarView, UserDetailView, UserProfileView

urlpatterns = [
    path('<slug:pk>/', UserProfileView.as_view(), name="profile"),
    path('details/<slug:pk>', UserDetailView.as_view(), name="view_details"),
    path('edit-avatar/<slug:pk>/',
         EditAvatarView.as_view(), name="edit_avatar"),
]
