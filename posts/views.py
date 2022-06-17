from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .models import Post, Reply
from .forms import PostForm, ReplyForm


#Posts
class PostsView(LoginRequiredMixin, ListView):
    """ A view to return a list of posts """
    template_name = "posts/posts.html"
    model = Post
    success_url = "/posts/" 
    context_object_name = 'posts'

    def get_queryset(self):
        """ Return queryset by newest first """
        order_newest = Post.objects.order_by('-time')
        return order_newest


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    A view to create a Post
    """
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = "/posts/" 
    model = Post

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePostView, self).form_valid(form)


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a post """
    model = Post
    success_url = "/posts/"

    def test_func(self):
        return self.request.user == self.get_object().user


class ViewPostView(LoginRequiredMixin, FormMixin, DetailView):
    """
    A view to see a posts and its replies
    """
    template_name = 'posts/view_post.html'
    model = Post
    form_class = ReplyForm

    def get_context_data(self, **kwargs):
        # Get post and reply any data and add it to the context
        context = {
            'posts': self.model.objects.filter(pk=self.kwargs['pk']),
            'replies': Reply.objects.filter(rid=self.kwargs['pk']),
            'form': ReplyForm(),
        }
        return context


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit a post
    """
    form_class = PostForm
    template_name = 'posts/edit_post.html'
    model = Post
    context_object_name = 'post'

    def form_valid(self, form):
        # if form is valid return to discussion
        self.success_url = '/posts/view/' + str(self.object.did) + '/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user

# Replies
class CreateReplyView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm

    def form_valid(self, form):
        # if form is valid return to post
        self.success_url = '/posts/view/' + str(Post.objects.get(pk=self.kwargs['pk']).did) + '/'
        form.instance.rid = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditReplyView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit a reply
    """
    form_class = ReplyForm
    template_name = 'posts/edit_reply.html'
    model = Reply

    def form_valid(self, form):
        # if form is valid return to post
        self.success_url = '/posts/view/' + str(self.object.rid) + '/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteReplyView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an reply """
    model = Reply
    success_url = "/posts/"

    def test_func(self):
        return self.request.user == self.get_object().user