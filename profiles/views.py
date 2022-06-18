from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile


class UserProfileView(LoginRequiredMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/profile.html'
    model = UserProfile

    def get(self, request, user_id):
        user = get_object_or_404(self.model, user=user_id)

        context = {
            'user_id': user_id,
            'user': user,
        }

        return render(request, self.template_name, context)
