from django.urls import path
from .views import FollowView

urlpatterns = [
    path('', FollowView.as_view(), name="follow"),
]