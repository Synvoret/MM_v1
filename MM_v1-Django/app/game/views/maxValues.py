from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import SHIPSLOCALIZATIONS
from dataset.models import Cube
from game.models import Game
from game.models import TrackPlayerHitLocations
from game.models import PlayersShipsCards

def maxValues(request):
    """
    Maximum parameter values for the player.
    
    Hull, Cargo, Masts, Crew, Cannons, Actions, etc.
    """

    data = {}

    # random colour player active
    game = Game.objects.get(number=100)
    player_colour = request.session['playerColourActive']
    colour_cube_max = Cube.objects.get(name=player_colour.capitalize() + ' Cube Max') # for mark the maximum value of parameter on player board
    colour_cube_max_image = colour_cube_max.image.url
    game_ships = PlayersShipsCards.objects.get(game_number=game)
    player_ship = getattr(game_ships, f"player_{player_colour}")

    # hull
    player_max_hull_ship = player_ship.toughness
    player_max_hull = player_max_hull_ship

    data['playerMaxAmountHull'] = player_max_hull

    # cargo
    player_max_cargo_ship = player_ship.cargo
    player_max_cargo = player_max_cargo_ship
    data['playerMaxAmountCargo'] = player_max_cargo
    
    # masts
    player_max_masts_ship = player_ship.toughness
    player_max_masts = player_max_masts_ship
    data['playerMaxAmountMasts'] = player_max_masts

    # crew
    player_max_crew_ship = player_ship.crew
    player_max_crew = player_max_crew_ship
    data['playerMaxAmountCrew'] = player_max_crew

    # cannons
    player_max_cannons_ship = player_ship.cannons
    player_max_cannons = player_max_cannons_ship
    data['playerMaxAmountCannons'] = player_max_cannons

    # actions
    player_max_speed_ship = player_ship.speed
    player_max_speed = player_max_speed_ship
    data['playerMaxAmountActions'] = player_max_speed

    # data['playerInPort'] = request.session['playerInPort']
    data['playerColour'] = player_colour
    data['playerCubeMaxImage'] = colour_cube_max_image

    return JsonResponse(data)
