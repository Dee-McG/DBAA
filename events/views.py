from django.views.generic import CreateView, ListView
from .models import Event
from .forms import EventForm


class EventList(ListView):
    """
    Create a list of events view
    """
    model = Event
    queryset = Event.objects.all().order_by("-e_time")
    template_name = "events_list.html"
    paginate_by = 6



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
