import random
from django.http import JsonResponse
from dataset.models import ShipCard, CaptainCard


def newPlayer(request):
    """Endpoint return a new player (random two captains and two ships (flute and sloop) to select)."""

    captains = CaptainCard.objects.all()
    captain_1 = random.choice(captains)
    captain_2 = random.choice(captains)
    ship_sloop = ShipCard.objects.get(ship='Sloop')
    ship_flute = ShipCard.objects.get(ship='Flute')

    data = {
        'captain1Name': captain_1.captain,
        'captain1Image': captain_1.awers.url,
        'captain2Name': captain_2.captain,
        'captain2Image': captain_2.awers.url,
        'shipSloopImage': ship_sloop.awers.url,
        'shipFluteImage': ship_flute.awers.url,
    }

    return JsonResponse(data)
