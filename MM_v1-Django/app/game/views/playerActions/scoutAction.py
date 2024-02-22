import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, PLAYER_COLOURS, HITS
from dataset.models import CargoCard
from dataset.models import MerchantTokens
from game.models import Game
from game.models import ShipsLocalisations
from game.models import PlayersCaptainsCards
from game.models import TrackMerchantTokens
from game.models import TrackPlayerSpecialWeapons


@csrf_exempt
def scoutAction(request):
    """Function is responsible for Scout Merchant."""


    data = {}
    game = Game.objects.get(number=100)
    ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
    player_colour = request.session['playerColourActive']
    player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")
    merchants_track = TrackMerchantTokens.objects.get(game_number=game)
    player_special_weapons_instance = TrackPlayerSpecialWeapons.objects.get(game_number=game)


    # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
    if request.GET.get('type_request') == 'scout':
        ships = [field.name for field in ships_in_zone._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
        ships_values = {field_name: getattr(ships_in_zone, field_name) for field_name in ships}
        for ship in ships_values.keys():
            if f"{player_colour}_ship" == ship: # actual player
                continue
            elif ships_values[ship] == player_localisation and any([colour[0].lower() in ship for colour in PLAYER_COLOURS]): # other player
                if not getattr(ships_in_zone, ship.replace('_ship', '_in_port')):
                    data[f"{ship.replace('_ship', 'PlayerShip')}"] = True
            elif ships_values[ship] == player_localisation and any([colour[0].lower().replace(' ', '_') in ship for colour in COLOUR]): # other NPC
                data[f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}"] = True
            elif ship == 'merchants_ship': # merchants
                if player_localisation in ships_values['merchants_ship']: # merchant is in sea zone with player
                    data['merchantToken'] = True


    # Merchant - Raid, Trade, Escort
    if request.GET.get('type_request') == 'merchant':
        print('MERCHANT OPTIONs')


    if request.POST.get('type_request') == 'merchant raid':
        # MOVE MERCHANT TOKEN to MERCHANTs TRACK on BOARD, if 9 then reset tokens
        for field in merchants_track._meta.fields:
            field_name = field.name
            if field_name == 'id' or field_name == 'game_number':
                continue
            elif getattr(merchants_track, field_name) == None:
                setattr(merchants_track, field_name, ships_in_zone.merchants_ship[player_localisation])
                merchants_track.save()
                data['merchantTrack'] = field_name
                token = MerchantTokens.objects.get(nationality=ships_in_zone.merchants_ship[player_localisation])
                data['merchantToken'] = token.awers.url # put metchant token on merchant track
                data['removeMerchantToken'] = player_localisation.lower().replace(' ','-') # remove merchant token from board, Sea Zone name
                del ships_in_zone.merchants_ship[player_localisation] # remove merchant token from sea zone db
                ships_in_zone.save()
                break
        else: # when on merchant track is 8 merchant tokens
            data['newDistributeMerchantTokens'] = True
            print('MAM JUZ 8 KUPCÓW NA TRAKU, TEN JEST 9')

        cargo_cards = CargoCard.objects.all() # drawing 3 cards
        cargo_card_1 = random.choice(cargo_cards)
        cargo_card_2 = random.choice(cargo_cards)
        cargo_card_3 = random.choice(cargo_cards)
        cargo_card_1_value = cargo_card_1.plunder_value
        cargo_card_2_value = cargo_card_2.plunder_value
        cargo_card_3_value = cargo_card_3.plunder_value

        hits_result = {} # hits result for merchant raid
        for location_hit in HITS:
            hits_result[location_hit[0]] = 0
        cargo_card_1_hits = cargo_card_1.hits
        cargo_card_2_hits = cargo_card_2.hits
        cargo_card_3_hits = cargo_card_3.hits
        hits_result[cargo_card_1_hits] += 1
        hits_result[cargo_card_2_hits] += 1
        hits_result[cargo_card_3_hits] += 1
        data['hullHits'] = hits_result['Hull']
        data['cargoHits'] = hits_result['Cargo']
        data['mastsHits'] = hits_result['Masts']
        data['crewHits'] = hits_result['Crew']
        data['cannonsHits'] = hits_result['Cannons']
        data['escapeResult'] = hits_result['Escape']

        cargo_cards_value_summary = cargo_card_1_value + cargo_card_2_value + cargo_card_3_value # golds for merchant raid
        data['cargoCardValue'] = cargo_cards_value_summary
        data['cargoCard1ImageUrl'] = cargo_card_1.awers.url
        data['cargoCard2ImageUrl'] = cargo_card_2.awers.url
        data['cargoCard3ImageUrl'] = cargo_card_3.awers.url

        # get Seamanship Captain
        player_captain_seamanship_value = getattr(PlayersCaptainsCards, f"player_{player_colour}") # .seamanship: get SEAMANSHIP Captain parameter as int

        # player special weapons
        player_special_weapons = getattr(player_special_weapons_instance, f"player_{player_colour}")
        data['playerSpecialWeapons'] = []
        for special_weapon in player_special_weapons:
            data['playerSpecialWeapons'].append(special_weapon.lower().replace(' ', '-'))

        # discard card

        # exchange choosen card

        print('BĘDZIE NAPAD NA KUPCA')


    # spend special weapon -> "scoutAction('spend special weapon chain-shot')"
    if 'spend special weapon' in str(request.POST.get('type_request')):
        spend_special_weapon = (request.POST.get('type_request')[21:]).replace('-', ' ').title()
        player_special_weapons = [item for item in getattr(player_special_weapons_instance, f"player_{player_colour}") if item != spend_special_weapon]
        setattr(player_special_weapons_instance, f"player_{player_colour}", player_special_weapons)
        player_special_weapons_instance.save()
        player_special_weapons = getattr(player_special_weapons_instance, f"player_{player_colour}")
        data['playerSpecialWeapons'] = []
        for special_weapon in player_special_weapons:
            data['playerSpecialWeapons'].append(special_weapon.lower().replace(' ', '-'))


    # draw card
    if request.POST.get('type_request') == 'merchant raid draw card': # for MERCHANT RAID
        amount_success = int(request.POST.get('amountSuccess'))
        if amount_success > 0:
            cargo_cards = CargoCard.objects.all() # drawing 3 cards
            cargo_card = random.choice(cargo_cards)
            data['cargoCardPlunderValue'] = cargo_card.plunder_value
            data['cargoCardHits'] = cargo_card.hits
            data['cargoCardDrawImageUrl'] = cargo_card.awers.url
        print('DOBIERAM KARTĘCARGO W MERCHANT RAID')


    if request.POST.get('type_request') == 'merchant raid accept': # for MERCHANT RAID
        print('ZAPISUJE WYNIK MERCHANT RAID')


    if request.POST.get('type_request') == 'merchant trade':
        print('BĘDZIE HANDEL Z KUPCEM')


    if request.POST.get('type_request') == 'merchant escort':
        print('BĘDZIE ESKORTA KUPCA')


    data['playerColour'] = player_colour
    return JsonResponse(data)
