from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
from .forms import EventForm


class EventList(ListView):
    """
    Create a list of events view
    """
    model = Event
    template_name = "events/events.html"
    context_object_name = "events"
    paginate_by = 6
    
    def get_queryset(self): 
        events = Event.objects.order_by("-e_time")
        return events


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

def EventGoing(request, pk):
    event = get_object_or_404(Event, id=request.POST.get("event_id"))
    if event.going.filter(id=request.user.id).exists():
        event.going.remove(request.user)
    else:
        event.going.add(request.user)
    return HttpResponseRedirect(reverse("events", args=[str(pk)]))

class EventDetailView(DetailView):
    """
    Event details view
    """
    model = Event
    template_name = "events/view_event.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        going_connected = get_object_or_404(Event, id=self.kwargs["pk"])
        going = False
        if going_connected.going.filter(id=self.request.user.id).exists():
            going = True
        data["number_of_going"] = going_connected.number_of_going()
        data["going_event"] = going
        return data


