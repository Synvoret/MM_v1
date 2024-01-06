from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from dataset.models import Ship


def ship(request):
    """Endpoint return a ship for player."""

    unit = request.GET.get('unit', None)
    colour = request.GET.get('colour', None)

    shipImage = Ship.objects.get(name=unit.capitalize(), colour=colour.capitalize())

    return HttpResponse(shipImage.image.url)
