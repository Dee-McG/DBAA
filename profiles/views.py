from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import UserProfile
from .forms import UserAvatarForm, UserDetailForm

from follow.models import Follow
from events.models import EventNumbers


class UserProfileView(LoginRequiredMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/profile.html'
    model = UserProfile

    def post(self, request, pk):
        """Function to toggle follow on and off"""
        follower = get_object_or_404(User, id=pk)
        user_profile = get_object_or_404(User, id=self.request.user.id)
        already_following = Follow.objects.filter(
            user=user_profile, following=follower)

        if already_following:
            already_following.delete()
        else:
            Follow.objects.create(
                user=user_profile,
                following=follower
            )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get(self, request, pk):
        # logged in user
        user = get_object_or_404(User, id=self.request.user.id)
        # user profile (whos profile you're viewing)
        user_profile = get_object_or_404(self.model, user=pk)
        # user object of whos profile you're viewing
        profile_user = get_object_or_404(User, id=pk)
        # list of follow objects of users you're following
        users_following = Follow.objects.filter(
            user=profile_user)
        # Iterate over users to get user_profiles
        follow_lst = UserProfile.objects.filter(id=0)
        for usr in users_following:
            follow_lst = follow_lst | UserProfile.objects.filter(
                id=usr.following.id)
        # used to check if already following the user you're viewing
        following = Follow.objects.filter(
            user=user, following=profile_user)

        context = {
            'user_id': pk,
            'user': user,
            'user_str': str(user),
            'following': following,
            'users_following': follow_lst,
            'user_profile': user_profile,
            'user_profile_str': str(user_profile),
        }

        return render(request, self.template_name, context)


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """View to show user profile"""

    template_name = 'profiles/personal_details.html'
    model = UserProfile

    def get(self, request, pk):
        user_profile = get_object_or_404(self.model, user=self.request.user)
        context = {
            'user_profile': user_profile,
        }

        return render(request, self.template_name, context)

    def test_func(self):
        return self.request.user == self.get_object().user


class UserEventView(LoginRequiredMixin, DetailView):
    """
    A view to show user's events they are attending and show 
    event's friends of other user's are attending
    """

    template_name = 'profiles/view_profile_events.html'
    model = UserProfile

    def get(self, request, pk):
        # logged in user
        user = get_object_or_404(User, id=self.request.user.id)
        # user profile (who's profile you're viewing)
        user_profile = get_object_or_404(self.model, user=pk)
        # user object of who's profile you're viewing
        profile_user = get_object_or_404(User, id=pk)
        # list of follow objects of users you're following
        users_following = Follow.objects.filter(user=profile_user)
        events = EventNumbers.objects.filter(user=profile_user)

        context = {
            'user_id': pk,
            'user': user,
            'user_str': str(user),
            'user_profile': user_profile,
            'user_profile_str': str(user_profile),
            'events': events
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
        user_profile = get_object_or_404(self.model, user=self.request.user)

        context = {
            'user_profile': user_profile,
            'form': UserAvatarForm(instance=user_profile)
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
        user_profile = get_object_or_404(UserProfile, id=self.request.user.id)
        data = get_object_or_404(self.model, id=self.request.user.id)

        context = {
            'user_profile': user_profile,
            'form': UserDetailForm(instance=data)
        }

        return context
