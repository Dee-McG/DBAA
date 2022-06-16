from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class CreatePostView(CreateView):
    """
    A view to create a Post
    """
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = "/" #TODO Update to post list
    model = Post

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePostView, self).form_valid(form)
