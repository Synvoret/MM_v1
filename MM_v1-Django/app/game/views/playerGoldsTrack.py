from django.http import HttpResponse, JsonResponse
from dataset.models import Coin
from game.models import Game
from game.models import TrackPlayerGolds


def playerGoldsTrack(request):
    """Endpoint put all cubes on track Player Hit Locations."""

    colour = request.GET.get('colour', None)

    coin = Coin.objects.get(coin='One')
    coin_image = coin.image.url

    amount_golds = TrackPlayerGolds.objects.get(player_colour=colour.capitalize())

    data = {
        "coinImage": coin_image,
        "amountGolds": str(amount_golds.amount_gold),
    }

    return JsonResponse(data)
