from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import UserProfile
from .forms import UserAvatarForm


class UserProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/profile.html'
    model = UserProfile

    def get(self, request, pk):
        user = get_object_or_404(self.model, user=pk)

        context = {
            'user_id': pk,
            'user': user,
        }

        return render(request, self.template_name, context)

    def test_func(self):
        return self.request.user == self.get_object().user


class EditAvatarView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update user avatar"""

    form_class = UserAvatarForm
    template_name = 'profiles/edit_avatar.html'
    model = UserProfile

    def form_valid(self, form):
        # if form is valid return profile
        self.success_url = f'/profile/{self.request.user.id}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
