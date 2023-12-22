from django.http import HttpResponse
from dataset.models import EventCard


def drawEventCard(request):
    """Endpoint return a draw new Event Card."""

    event_card = EventCard.objects.get(card="Gentle Wind")
    return HttpResponse(event_card.awers.url)
