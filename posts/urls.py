from django.urls import path
from .views import (
    PostsView, CreatePostView, ViewPostView,
    CreateReplyView, EditPostView, DeletePostView,
    DeleteReplyView, EditReplyView
    )

urlpatterns = [
    path('', PostsView.as_view(), name="posts"),
    path('create/', CreatePostView.as_view(), name="create_post"),
    path('view/<slug:pk>/', ViewPostView.as_view(), name="view_post"),
    path('edit/<slug:pk>/', EditPostView.as_view(), name="edit_post"),
    path('delete/<slug:pk>/', DeletePostView.as_view(), name="delete_post"),
    path('edit/reply/<slug:pk>/', EditReplyView.as_view(), name="edit_reply"),
    path('delete/reply/<slug:pk>/', DeleteReplyView.as_view(), name="delete_reply"),
    path('reply/<slug:pk>/', CreateReplyView.as_view(), name="create_reply"),
]