import random
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from board.models import SeaZone
from dataset.utils.dataset.decorators.choices import ALLOWEDDESTINATIONS, DIRECTION
from game.models import Game
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations


@csrf_exempt
def scoutAction(request):

    data = {}

    game = Game.objects.get(number=100)
    ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
    player_colour = request.session['playerColourActive']
    player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")

    # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
    if request.GET.get('type_request') == 'scout':
        ships = [field.name for field in ships_in_zone._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
        ships_values = {field_name: getattr(ships_in_zone, field_name) for field_name in ships}
        for ship in ships_values.keys():
            if ships_values[ship]:
                if ship == 'merchants_ship':
                    print(ships_values['merchants_ship'][player_localisation], 'MERCHANT NATIONALITY')
                else:
                    print(ships_values[ship], f"{ship} ship")


    if request.method == 'POST':
        if request.POST.get('type_request') == 'merchant':
            print('BATTLE with MERFCHANT')


    return JsonResponse(data)





















# @csrf_exempt
# def moveAction(request):

#     print(dict(request.session))

#     player_colour = request.session['playerColourActive']
#     game = Game.objects.get(number=100)
#     player_ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)

#     data = {}


#     # WHEN CLICK "MOVES" BUTTON, CHECKING LOCALISATION for SHIP SEA ZONE or PORT
#     if request.GET.get('type_request', None) == 'moves':

#         if getattr(player_ship_localisation_instance, f"{player_colour}_in_port"):
#             data['unitInPort'] = True


#     if request.GET.get('type_request', None) == 'back':
#         data['playerInPort'] = getattr(player_ship_localisation_instance, f"{player_colour}_in_port")


#     # WHEN PLAYER move TO PORT or FROM PORT or TO SEA ZONE
#     if request.method == 'POST':
#         player_ship_unit_instance = getattr(PlayersShipsCards.objects.get(game_number=game), f"player_{player_colour}")
#         player_ship_unit = player_ship_unit_instance.ship
#         player_ship_position = getattr(player_ship_localisation_instance, player_colour + '_ship')

#         if request.POST.get('type_request') == 'to port':
#             setattr(player_ship_localisation_instance, f"{player_colour}_in_port", True)

#         if request.POST.get('type_request') == 'from port':
#             setattr(player_ship_localisation_instance, f"{player_colour}_in_port", False)
#             request.session['playerInPort'] = False

#         if request.POST.get('type_request') == 'to sea zone':
#             actual_sea_zone = SeaZone.objects.get(sea_zone_name=player_ship_position)
#             for direction in DIRECTION:
#                 destination = getattr(actual_sea_zone, f"{direction[0].lower()}_direction")
#                 if destination:
#                     data[direction[0].lower()] = destination

#         if request.POST.get('type_request') in ALLOWEDDESTINATIONS:
#             setattr(player_ship_localisation_instance, player_colour + '_ship', request.POST.get('type_request'))
#             player_ship_position = getattr(player_ship_localisation_instance, player_colour + '_ship')
#             print(f"PŁYNĘ DO {request.POST.get('type_request')}")

#         player_ship_localisation_instance.save()
#         data['playerShipUnit'] = player_ship_unit.lower()
#         data['playerDestination'] = player_ship_position.lower().replace(' ', '-')
#         data['playerColour'] = player_colour

#     return JsonResponse(data)










    # """Endpoint return a randomly fishing card."""

    # player_colour = request.session['playerColourActive']

    # # SERIALIZER
    # if 'fishingCard' not in request.session:
    #     # if does not exist, generate new randomly card and save in session
    #     fishing_cards = FishingCard.objects.all()
    #     random_fishing_card = random.choice(fishing_cards)
    #     # Serialize object to JSON and save in session
    #     serializer = FishingCardSerializer(random_fishing_card)
    #     serialized_fishing_card = serializer.data
    #     request.session['fishingCard'] = serialized_fishing_card
    #     print(dict(request.session))
    # else:
    #     # if exist in session
    #     serialized_fishing_card = request.session['fishingCard']
    #     serializer = FishingCardSerializer(data=serialized_fishing_card)
    #     serializer.is_valid()
    #     random_fishing_card = serializer.validated_data


    # # REQUEST METHOD GET
    # if request.method == 'GET':
    #     data = {
    #         'fishingCardImage': request.session['fishingCard']['awers'],
    #         'playerColour': player_colour,
    #     }
    #     return JsonResponse(data)


    # # REQUEST METHOD POST
    # if request.method == 'POST':
    #     data = {}
    #     fishing_card = request.session['fishingCard']
    #     game = Game.objects.get(number=100)
    #     if fishing_card['fishing_value']:
    #         player_golds = TrackPlayerGolds.objects.get(game_number=game)
    #         setattr(player_golds, 'player_' + player_colour, getattr(player_golds, 'player_' + player_colour) + fishing_card['fishing_value'])
    #         player_golds.save()
    #         data['fishingValue'] = True
    #     if fishing_card['fishing_hits']: 
    #         player_hits_locations = TrackPlayerHitLocations.objects.get(player_colour=player_colour.title())
    #         hit_location = fishing_card['fishing_hits']
    #         setattr(player_hits_locations, hit_location.lower(), getattr(player_hits_locations, hit_location.lower()) - 1)
    #         player_hits_locations.save()
    #         data['fishingHits'] = True
    #     del request.session['fishingCard']
    #     data['colour'] = player_colour
    #     return JsonResponse(data)
