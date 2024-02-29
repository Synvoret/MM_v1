from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import BOUNTIES
from dataset.models import Flag
from game.models import Game
from game.models import TrackPlayerBounties


def updatePlayerBounties(request):
    """Endpoint update Player Bounties on player board."""

    data = {}

    if request.method == 'GET':

        player_colour = request.GET.get('colour')
        game = Game.objects.get(number=100)
        player_bounties_instance = TrackPlayerBounties.objects.get(game_number=game)
        player_bounties = getattr(player_bounties_instance, f"player_{player_colour}")

        for bounty in BOUNTIES:
            if list(player_bounties).count(bounty) != 0:
                # amount bounties
                data[bounty.replace(" ", "")] = list(player_bounties).count(bounty)
                # bounty flag image url
                name = f"{bounty} Flag"
                data[f"{bounty.replace(' ', '')}Image"] = (Flag.objects.get(name=name)).image.url

    return JsonResponse(data)
