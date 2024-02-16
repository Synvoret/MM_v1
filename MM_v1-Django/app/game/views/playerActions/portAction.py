from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, PLAYER_COLOURS
from game.models import Game
from game.models import ShipsLocalisations


@csrf_exempt
def portAction(request):
    """Function is responsible for Port Actions."""

    if request.GET.get('type_request') == 'port':
        data = {}
        print('JESTEM W PORCIE I PRZELACZAM NA AKCJE PORTOWE')
        game = Game.objects.get(number=100)
        # ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
        # player_colour = request.session['playerColourActive']
        # player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")


        # # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
        # if request.GET.get('type_request') == 'scout':
        #     ships = [field.name for field in ships_in_zone._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
        #     ships_values = {field_name: getattr(ships_in_zone, field_name) for field_name in ships}
        #     for ship in ships_values.keys():
        #         if f"{player_colour}_ship" == ship: # actual player
        #             continue
        #         elif ships_values[ship] == player_localisation and any([colour[0].lower() in ship for colour in PLAYER_COLOURS]): # other player
        #             if not getattr(ships_in_zone, ship.replace('_ship', '_in_port')):
        #                 data[f"{ship.replace('_ship', 'PlayerShip')}"] = True
        #         elif ships_values[ship] == player_localisation and any([colour[0].lower().replace(' ', '_') in ship for colour in COLOUR]): # other NPC
        #             data[f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}"] = True
        #         elif ship == 'merchants_ship': # merchants
        #             if ships_values['merchants_ship'][player_localisation]: # merchant is in sea zone with player
        #                 data['merchantToken'] = True


        # # Merchant - Raid, Trade, Escort
        # if request.GET.get('type_request') == 'merchant':
        #     print('MERCHANT OPTIONs')


        # data['playerColour'] = player_colour
        return JsonResponse(data)


    if request.GET.get('type_request') == 'visit shipyard':

        data = {}
        game = Game.objects.get(number=100)
        # ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
        # player_colour = request.session['playerColourActive']
        # player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")


        # # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
        # if request.GET.get('type_request') == 'scout':
        #     ships = [field.name for field in ships_in_zone._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
        #     ships_values = {field_name: getattr(ships_in_zone, field_name) for field_name in ships}
        #     for ship in ships_values.keys():
        #         if f"{player_colour}_ship" == ship: # actual player
        #             continue
        #         elif ships_values[ship] == player_localisation and any([colour[0].lower() in ship for colour in PLAYER_COLOURS]): # other player
        #             if not getattr(ships_in_zone, ship.replace('_ship', '_in_port')):
        #                 data[f"{ship.replace('_ship', 'PlayerShip')}"] = True
        #         elif ships_values[ship] == player_localisation and any([colour[0].lower().replace(' ', '_') in ship for colour in COLOUR]): # other NPC
        #             data[f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}"] = True
        #         elif ship == 'merchants_ship': # merchants
        #             if ships_values['merchants_ship'][player_localisation]: # merchant is in sea zone with player
        #                 data['merchantToken'] = True


        # # Merchant - Raid, Trade, Escort
        # if request.GET.get('type_request') == 'merchant':
        #     print('MERCHANT OPTIONs')


        # data['playerColour'] = player_colour
        return JsonResponse(data)

