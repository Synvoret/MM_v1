import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.models import DemandTokens
from game.models import Game
from game.models import GameDemandTokens


@csrf_exempt
def drawDemandToken(request):
    """Function return new randomly demand token for port."""

    data = {}

    port = request.GET.get("port")

    game = Game.objects.get(number=100)
    game_demands_token = GameDemandTokens.objects.get(game_number=game)
    all_tokens = DemandTokens.objects.all()
    random_demand_token = random.choice(all_tokens)
    setattr(game_demands_token, f"{str(port).replace('-', '_')}", random_demand_token)
    game_demands_token.save()

    data['demandTokenImage'] = random_demand_token.awers.url

    return JsonResponse(data)
