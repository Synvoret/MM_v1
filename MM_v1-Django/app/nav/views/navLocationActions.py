from django.http import JsonResponse
from dataset.utils.dataset.decorators.choices import HIT_LOCATIONS, SHIPSLOCALIZATIONS
from game.models import Game
from game.models import TrackPlayerHitLocations
from game.models import PlayersCaptainsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards


def navLocationActions(request):

    data = {}
    # game = Game.objects.get(number=100)
    # player_colour = request.session['playerColourActive']
    # missions_stack = StackMissionsCards.objects.get(game_number=game)
    # player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    # player_hits_locations_instance = TrackPlayerHitLocations.objects.get(player_colour=player_colour)
    # ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)

    # # startPlayerTurn
    # if request.GET.get('when') == 'startPlayerTurn':
    #     # if any location is destroyed you cannot interact with merchant
    #     for hit_localisation in HIT_LOCATIONS:
    #         if getattr(player_hits_locations_instance, hit_localisation) == 0:
    #             data['playerHaveDestroyedHitLocation'] = True
    #             break

    #     if getattr(ship_localisation_instance, f"{player_colour}_in_port"):
    #         request.session['playerInPort'] = True
    #     else:
    #         request.session['playerInPort'] = False

    #     if getattr(ship_localisation_instance, f"{player_colour}_ship") == 'The Caribbean Sea':
    #         data['isInTheCaribbeanSea'] = True


    # # port
    # if request.GET.get('when') == 'port':        
    #     for mission_card in ['mission_1_card', 'mission_2_card', 'mission_3_card']:
    #         if getattr(missions_stack, mission_card) and (getattr(missions_stack, mission_card)).port == getattr(ship_localisation_instance, f"{player_colour}_ship"):
    #             data['missionInPort'] = True
    #     if player_captain_instance.home_port == getattr(ship_localisation_instance, f"{player_colour}_ship"): 
    #         data['playerHomePort'] = True


    # data['playerInPort'] = request.session['playerInPort']
    # data['playerColour'] = player_colour

    return JsonResponse(data)
