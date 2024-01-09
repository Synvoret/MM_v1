from django.http import JsonResponse
from dataset.models import Coin
from game.models import TrackPlayerGolds


def updatePlayerGolds(request):
    """Endpoint put all cubes on track Player Hit Locations."""

    colour = request.GET.get('colour', None)

    coin = Coin.objects.get(coin='One')
    coin_image = coin.image.url

    values = TrackPlayerGolds.objects.get(game_number=1)

    if colour == 'blue':
        amount_golds = values.player_blue
    elif colour == 'green':
        amount_golds = values.player_green
    elif colour == 'red':
        amount_golds = values.player_red
    elif colour == 'yellow':
        amount_golds = values.player_yellow

    data = {
        "coinImage": coin_image,
        "amountGolds": str(amount_golds),
    }

    return JsonResponse(data)
