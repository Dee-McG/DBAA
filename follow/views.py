from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from posts.models import Post
from .models import Follow


class FollowView(LoginRequiredMixin, ListView):
    """ A view to return a list of friends activity """
    template_name = "follow/follow_list.html"
    model = Follow
    success_url = "/follow/"

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
