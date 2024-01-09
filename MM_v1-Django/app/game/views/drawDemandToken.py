import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.models import DemandTokens
from game.models import GameDemandTokens


@csrf_exempt
def drawDemandToken(request):
    """Function return new randomly demand token for port."""

    port = request.GET.get("port")

    all_tokens = DemandTokens.objects.all()
    random_token = random.choice(all_tokens)

    game_demands_token = GameDemandTokens.objects.get(game_number=1)
    setattr(game_demands_token, f"{str(port).replace('-', '_')}", random_token.cargo)
    game_demands_token.save()

    data = {
        "demandTokenImage": random_token.awers.url,
    }

    return JsonResponse(data)
