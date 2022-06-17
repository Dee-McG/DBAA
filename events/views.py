from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .models import Event, EventNumbers
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


class EventDetailView(FormMixin, DetailView):
    """
    Event details view
    """
    model = Event
    template_name = "events/view_event.html"

    def post(self, request, *args, **kwargs):
        event = Event.objects.all()[:1].get()
        user = EventNumbers.objects.filter(user=self.request.user)
    
        if user:
            user.delete()
        else:
            EventNumbers.objects.create(
                user=self.request.user, 
                event=event
            )  

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    def get_context_data(self, **kwargs):
        context = {
            'events': self.model.objects.filter(pk=self.kwargs['pk']),
            'number': EventNumbers.objects.filter(event=self.kwargs['pk']).count,
        }
        return context


