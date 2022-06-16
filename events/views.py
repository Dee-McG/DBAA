from .models import Event
from django.views.generic import CreateView
from .forms import EventForm


class CreateEventView(CreateView):
    """
    Create an event view
    """
    form_class = EventForm
    model = Event
    template_name = "events/create_event.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEventView, self).form_valid(form)
