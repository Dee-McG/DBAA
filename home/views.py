from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ A view to return the home page """
    template_name = "home/index.html"