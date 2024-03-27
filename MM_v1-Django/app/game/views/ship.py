from django.http import HttpResponse
from dataset.models import Ship


def ship(request):
    """Endpoint return a ship for player."""

    unit = request.GET.get('unit')
    colour = ((request.GET.get('colour', None)).replace("-", " ").title()).replace('_', ' ')

    ship = Ship.objects.get(name=unit.title(), colour=colour)

    return HttpResponse(ship.image.url)
