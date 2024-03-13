import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, LOYALITY, PLAYER_COLOURS
from game.models import Game
from game.models import GameDemandTokens
from game.models import PlayersCaptainsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import StackPlayerCargoCards
from game.models import TrackFavors
from game.models import TrackGloryPoint
from game.models import TrackLoyality
from game.models import TrackPlayerGolds
from game.serializers import CargoCardSerializer


@csrf_exempt
def portAction(request):
    """Function is responsible for Port Actions."""

    data = {}
    game = Game.objects.get(number=100)
    player_colour = request.session['playerColourActive']
    demand_tokens = GameDemandTokens.objects.get(game_number=game)
    missions_stack = StackMissionsCards.objects.get(game_number=game)
    player_golds = TrackPlayerGolds.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_cargo_cards_instance = StackPlayerCargoCards.objects.get(player_colour=player_colour)
    ship_localisation_instance = ShipsLocalisations.objects.get(game_number=game)
    favours = TrackFavors.objects.get(game_number=game)
    loyality = TrackLoyality.objects.get(game_number=game)


    # GET method
    if request.method == 'GET':

        # port

        # sell goods (always as first, onlu one time in turn)
        if request.GET.get('type_request') == 'sell goods':
            for i in range(1, 9):
                if getattr(player_cargo_cards_instance, f"cargo_card_{i}"):
                    card = getattr(player_cargo_cards_instance, f"cargo_card_{i}")
                    # request.session[f"playerCargoCard{i}"] = CargoCardSerializer(card).data
                    data[f"playerCargo{i}"] = card.cargo
                    data[f"playerCargoCard{i}ImageUrl"] = card.awers.url
                else: break
            port_name = str(getattr(ship_localisation_instance, f"{player_colour}_ship")).lower().replace(' ', '_')
            demand_token_in_port = getattr(demand_tokens, port_name)
            data['demanTokenInPort'] = demand_token_in_port.cargo
            data['demanTokenInPortImageUrl'] = demand_token_in_port.awers.url

        # visit shipyard


    # POST method
    if request.method == 'POST':

        # accept sold goods
        if request.POST.get('type_request') == 'sell goods accept':
            port = str(getattr(ship_localisation_instance, f"{request.session['playerColourActive']}_ship"))
            data['port'] = port.lower().replace(' ', '-')
            list_numbers = list(json.loads(request.POST.get('numbers'))) # sold goods

            # update cargo cards
            for number in list_numbers:
                setattr(player_cargo_cards_instance, f"cargo_card_{number}", None)
                player_cargo_cards_instance.save()
                try: del request.session[f"playerCargoCard{number}"]
                except: pass
            player_goods = []
            for i in range(1, 9): # making new player goods list
                player_goods.append(getattr(player_cargo_cards_instance, f"cargo_card_{i}"))
                setattr(player_cargo_cards_instance, f"cargo_card_{i}", None) # clear db
            player_goods_new_queue = [cargo for cargo in player_goods if cargo is not None]
            for index, cargo in enumerate(player_goods_new_queue):
                setattr(player_cargo_cards_instance, f"cargo_card_{index + 1}", cargo) # add left goods to db
            player_cargo_cards_instance.save()

            # update golds
            if int(request.POST.get('golds')) != 0:
                player_golds.increase_golds(f"player_{player_colour}", int(request.POST.get('golds')))

            # update glory
            if int(request.POST.get('glory')) == 1:
                glory_points_track_instance = TrackGloryPoint.objects.get(game_number=game)
                glory_points_track_instance.increase_glory_point(f"player_{player_colour}")


        # stash gold
        if request.POST.get('type_request') == 'stash gold':
            if getattr(player_golds, f"player_{player_colour}") > 0:
                loyality.decrease_loyality(f"player_{player_colour}")


        # raise loyality
        if request.POST.get('type_request') == 'raise loyality':

            player_loyality = getattr(loyality, f"player_{player_colour}")

            if player_loyality == 'Fierce Loyality': # this is max at loyality track
                data['cantChangeLoyality'] = True

            if getattr(player_golds, f"player_{player_colour}") >= 3:
                if player_loyality == 'Happy':
                    player_golds.decrease_golds(f"player_{player_colour}", 3)
                elif player_loyality == 'Pleased':
                    player_golds.decrease_golds(f"player_{player_colour}", 3)
                elif player_loyality == 'Content':
                    player_golds.decrease_golds(f"player_{player_colour}", 3)
                elif player_loyality == 'Restless':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)
                elif player_loyality == 'Unhappy':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)
                elif player_loyality == 'Angry':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)
            elif getattr(player_golds, f"player_{player_colour}") == 2:
                if player_loyality == 'Restless':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)
                elif player_loyality == 'Unhappy':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)
                elif player_loyality == 'Angry':
                    player_golds.decrease_golds(f"player_{player_colour}", 2)

            loyality.increase_loyality(f"player_{player_colour}")


        # gain favour
        if request.POST.get('type_request') == 'get favour':
            if getattr(player_golds, f"player_{player_colour}") < 2:
                data['cantGetFavour'] = True
            else:
                player_golds.decrease_golds(f"player_{player_colour}", 2)
                favours.increase_favour_point(f"player_{player_colour}")

    data['playerColour'] = player_colour
    return JsonResponse(data)
