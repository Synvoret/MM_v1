from django.http import JsonResponse
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards


def goGame(request):
    """
    Endpoint is responsible for start game after choosen players (colour, captains and ships).
    
    Proceeds to drawing the first event card in new game.
    """

    player_colours = ['player_blue', 'player_green', 'player_red', 'player_yellow']
    data = {}

    game = Game.objects.get(number=100)
    players_captains = PlayersCaptainsCards.objects.get(game_number=game)
    players_ships = PlayersShipsCards.objects.get(game_number=game)

    for player_colour in player_colours:
        captain = getattr(players_captains, player_colour)
        if captain:
            ship = getattr(players_ships, player_colour)
            data[player_colour + 'CaptainHomePort'] = (captain.home_port).lower().replace(' ', '-')
            data[player_colour + 'Ship'] = (ship.ship).lower()

    print(data)

    return JsonResponse(data)
