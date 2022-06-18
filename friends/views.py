
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Friend
from django.contrib.auth.models import User
from posts.models import Post, Reply


class FriendsView(LoginRequiredMixin, ListView):
    """ A view to return a list of friends activity """
    template_name = "friends/friends.html"
    model = Friend
    success_url = "/friends/"

    def get_context_data(self, **kwargs):
        """ Get all recent friends posts """
        following = self.model.objects.filter(user=self.request.user)
        posts = Post.objects.filter(title='')

        # Join querysets
        for person in following:
            user = User.objects.filter(username=person)
            posts = posts | Post.objects.filter(user__in=user.all()).order_by('-time')

        context = {
            'posts': posts
        }
        return context