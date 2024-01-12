import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.models import ShipModifications
from game.models import GameShipModifications


@csrf_exempt
def drawShipModification(request):
    """Function return new randomly ship modifocation token for port."""

    port = request.GET.get("port")

    all_modifications = ShipModifications.objects.all()
    random_modifications = random.choice(all_modifications)

    game_ship_modification = GameShipModifications.objects.get(game_number=1)
    setattr(game_ship_modification, f"{str(port).replace('-', '_')}", random_modifications.name)
    game_ship_modification.save()

    data = {
        "shipModificationAwersImage": random_modifications.awers.url,
        "shipModificationRewersImage": str(random_modifications.rewers),
    }

    return JsonResponse(data)
