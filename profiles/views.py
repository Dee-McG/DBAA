from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import UserProfile
from .forms import UserAvatarForm, UserDetailForm

from follow.models import Follow


class UserProfileView(LoginRequiredMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/profile.html'
    model = UserProfile

    def post(self, request, pk):
        """Function to toggle follow on and off"""
        follower = get_object_or_404(User, id=pk)
        user = get_object_or_404(User, id=self.request.user.id)
        already_following = Follow.objects.filter(user=user, following=follower)
        
        if already_following:
            already_following.delete()
        else:
            Follow.objects.create(
                    user=user,
                    following=follower
                )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get(self, request, pk):
        user = get_object_or_404(self.model, user=pk)
        follower = get_object_or_404(User, id=pk)
        user_profile = get_object_or_404(User, id=self.request.user.id)
        following = Follow.objects.filter(user=user_profile, following=follower)

        context = {
            'user_id': pk,
            'user': user,
            'following': following,
        }

        return render(request, self.template_name, context)



class UserDetailView(LoginRequiredMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/personal_details.html'
    model = UserProfile

    def get(self, request, pk):
        user = get_object_or_404(self.model, user=self.request.user)

        context = {
            'user': user,
            'details': user,
        }

        return render(request, self.template_name, context)


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

    def get_context_data(self):
        user = get_object_or_404(self.model, user=self.request.user)

        context = {
            'user': user,
            'form': UserAvatarForm(instance=user)
        }

        return context


class EditDetailsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update user avatar"""

    form_class = UserDetailForm
    template_name = 'profiles/edit_details.html'
    model = User

    def form_valid(self, form):
        # if form is valid return profile
        self.success_url = f'/profile/details/{self.request.user.id}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.get_object().username

    def get_context_data(self):
        user = get_object_or_404(UserProfile, id=self.request.user.id)
        data = get_object_or_404(self.model, id=self.request.user.id)

        context = {
            'user': user,
            'form': UserDetailForm(instance=data)
        }

        return context
