from django.urls import path
from .views import EditAvatarView, UserProfileView

urlpatterns = [
    path('<slug:pk>/', UserProfileView.as_view(), name="profile"),
    path('edit-avatar/<slug:pk>/',
         EditAvatarView.as_view(), name="edit_avatar"),
]
