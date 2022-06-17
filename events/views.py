from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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
    context_object_name = 'event'

    defpost(self, request, *args, )

    def get_context_data(self, **kwargs):
        data = self.get_object()

        context = {
        "events": data
        }
        return context

class EditEventView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to editing an event form for the event owner
    """
    form_class = EventForm
    template_name = "events/edit_event.html"
    model = Event

    def form_valid(self, form):
        self.success_url = "/"
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteEventView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete a post
    """
    model = Event
    success_url = "events/events"

    def test_func(self):
        return self.request.user == self.get_object().user
