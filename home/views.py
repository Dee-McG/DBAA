from django.views.generic import ListView
from events.models import Event, EventNumbers
from django.db.models import Count
from django.db.models import Max


class IndexView(ListView):
    """ A view to return the home page """
    template_name = "home/index.html"
    model = Event

    def get_context_data(self, **kwargs):
        """ 
        Returns event with highest people marked 'going'
        and the next 6 upcoming events
        """
        events = EventNumbers.objects.values('event').annotate(total_count=Count('event'))[:1]

        featured = Event.objects.filter()
        for event in events:
            featured = Event.objects.filter(id=event['event'])
        
        next_events = Event.objects.all()[:6]

        context = {
            "featured": featured,
            "next_events": next_events,
        }
        return context