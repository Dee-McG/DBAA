from django.views.generic import ListView
from events.models import Event, EventNumbers
from django.db.models import Count
from django.db.models import Max


class IndexView(ListView):
    """ A view to return the home page """
    template_name = "home/index.html"
    model = Event

    def get_context_data(self, **kwargs):

        events = EventNumbers.objects.values('user').order_by().annotate(event=Count('event'))[:1]
        featured = Event.objects.filter()
        for event in events:
            featured = Event.objects.filter(id=event['event'])
        next_events = Event.objects.all()[:6]

        context = {
            "featured": featured,
            "next_events": next_events,
        }
        return context