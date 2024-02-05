from django.http import JsonResponse

from game.models import Game
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations

from game.utils.game.utilUtil import next_player

def startPlayerActions(request):
    """Start Player Actions."""

    # random colour player active
    player_colour_active = next_player()
    request.session['playerColourActive'] = player_colour_active
    player_colour = request.session['playerColourActive']

    game = Game.objects.get(number=100)
    player_ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)

    data = {}

    if getattr(player_ship_localisation_instance, f"{player_colour}_in_port"):
        request.session['playerInPort'] = True
    else:
        request.session['playerInPort'] = False

    data['playerInPort'] = request.session['playerInPort']
    data['playerColour'] = player_colour

    return JsonResponse(data)
