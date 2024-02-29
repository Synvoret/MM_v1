import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from dataset.utils.dataset.decorators.choices import COLOUR, HITS, HIT_LOCATIONS, PLAYER_COLOURS
from dataset.models import CargoCard
from dataset.models import MerchantTokens
from game.models import Game
from game.models import ShipsLocalisations
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import StackPlayerCargoCards
from game.models import TrackMerchantTokens
from game.models import TrackPlayerBounties
from game.models import TrackPlayerGolds
from game.models import TrackPlayerHitLocations
from game.models import TrackPlayerSpecialWeapons
from game.models import TrackGloryPoint
from game.serializers import CargoCardSerializer


@csrf_exempt
def scoutAction(request):
    """Function is responsible for Scout Merchant."""


    data = {}
    game = Game.objects.get(number=100)
    ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
    player_colour = request.session['playerColourActive']
    data['playerColour'] = player_colour
    player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")
    merchants_track = TrackMerchantTokens.objects.get(game_number=game)
    player_captain_card = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_bounties_instance = TrackPlayerBounties.objects.get(game_number=game)
    player_special_weapons_instance = TrackPlayerSpecialWeapons.objects.get(game_number=game)
    player_hits_locations_instance = TrackPlayerHitLocations.objects.get(player_colour=player_colour)
    player_ship = getattr(PlayersShipsCards, f"player_{player_colour}")


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
                print(player_localisation)
                if player_localisation in ships_values['merchants_ship']: # merchant is in sea zone with player
                    data['merchantToken'] = True


    # Merchant - Raid, Trade, Escort
    if request.GET.get('type_request') == 'merchant':
        # if any location is destroyed you cannot interact with merchant
        for hit_localisation in HIT_LOCATIONS:
            if getattr(player_hits_locations_instance, hit_localisation) == 0:
                data['playerHaveDestroyedHitLocation'] = True
                break
        # if player is Pirate (have min. 1 Bounty)
        if len(getattr(player_bounties_instance, f"player_{player_colour}")) != 0:
            data['playerIsPirate'] = True
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
                player_bounties_list = getattr(player_bounties_instance, f"player_{player_colour}")
                player_bounties_list.append(token.nationality)
                setattr(player_bounties_instance, f"player_{player_colour}", player_bounties_list)
                # (getattr(player_bounties_instance, f"player_{player_colour}")).append(token.nationality)
                player_bounties_instance.save()
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
        data['cargoCard1Value'] = cargo_card_1_value
        data['cargoCard2Value'] = cargo_card_2_value
        data['cargoCard3Value'] = cargo_card_3_value

        hits_result = {} # hits result for merchant raid
        for location_hit in HITS:
            hits_result[location_hit[0]] = 0
        cargo_card_1_hits = cargo_card_1.hits
        cargo_card_2_hits = cargo_card_2.hits
        cargo_card_3_hits = cargo_card_3.hits
        data['cargoCard1Hit'] = cargo_card_1_hits.lower()
        data['cargoCard2Hit'] = cargo_card_2_hits.lower()
        data['cargoCard3Hit'] = cargo_card_3_hits.lower()
        hits_result[cargo_card_1_hits] += 1
        hits_result[cargo_card_2_hits] += 1
        hits_result[cargo_card_3_hits] += 1
        data['hullHits'] = hits_result['Hull']
        data['cargoHits'] = hits_result['Cargo']
        data['mastsHits'] = hits_result['Masts']
        data['crewHits'] = hits_result['Crew']
        data['cannonsHits'] = hits_result['Cannons']
        data['escapeResult'] = hits_result['Escape']
        data['shipManeuverability'] = player_ship.maneuverability

        cargo_cards_value_summary = cargo_card_1_value + cargo_card_2_value + cargo_card_3_value # golds for merchant raid
        data['cargoCardValue'] = cargo_cards_value_summary
        data['cargoCard1ImageUrl'] = cargo_card_1.awers.url
        data['cargoCard2ImageUrl'] = cargo_card_2.awers.url
        data['cargoCard3ImageUrl'] = cargo_card_3.awers.url

        # get Seamanship Captain
        data['playerCaptainSeamanshipValue'] = player_captain_card.seamanship  # .seamanship: get SEAMANSHIP Captain parameter as int

        # player special weapons
        player_special_weapons = getattr(player_special_weapons_instance, f"player_{player_colour}")
        data['playerSpecialWeapons'] = []
        for special_weapon in player_special_weapons:
            data['playerSpecialWeapons'].append(special_weapon.lower().replace(' ', '-'))


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
            data['cargoCardHits'] = (cargo_card.hits).lower()
            data['cargoCardDrawImageUrl'] = cargo_card.awers.url
        print('DOBIERAM KARTĘ CARGO W MERCHANT RAID')


    # exchange card
    if request.POST.get('type_request') == 'merchant raid exchange card':
        amount_success = int(request.POST.get('amountSuccess'))
        if amount_success > 0:
            cargo_cards = CargoCard.objects.all() # drawing 3 cards
            cargo_card = random.choice(cargo_cards)
            data['cargoCardPlunderValue'] = cargo_card.plunder_value
            data['cargoCardHits'] = (cargo_card.hits).lower()
            data['cargoCardDrawImageUrl'] = cargo_card.awers.url
        print('JEDZIEMY Z WYMIANĄKARTY CARGO')


    if request.POST.get('type_request') == 'merchant raid accept': # for MERCHANT RAID
        hit_locations = ['hull', 'cargo', 'masts', 'crew', 'cannons']
        # hits (getting all hits)
        for hit_location in HIT_LOCATIONS:
            hit_value = int(request.POST.get(f"get{hit_location.title()}Hit"))
            while hit_value > 0:
                if getattr(player_hits_locations_instance, hit_location) > 0:
                    setattr(player_hits_locations_instance, hit_location, getattr(player_hits_locations_instance, hit_location) - 1)
                    player_hits_locations_instance.save()
                hit_value -= 1
        # result: win or lose (checking all hit locations)
        for hit_location in HIT_LOCATIONS:
            if getattr(player_hits_locations_instance, hit_location) <= 0:
                data['resultMerchantRaid'] = 'lose'
                return JsonResponse(data)
        # golds
        if int(request.POST.get('getGold')) > 0:
            player_golds = TrackPlayerGolds.objects.get(game_number=game)
            setattr(player_golds, 'player_' + player_colour, getattr(player_golds, 'player_' + player_colour) + int(request.POST.get('getGold')))
            player_golds.save()
            if int(request.POST.get('getGold')) >= 12:
                glory_points_track_instance = TrackGloryPoint.objects.get(game_number=game)
                glory_points_track_instance.increase_glory_point(f"player_{player_colour}")
        data['resultMerchantRaid'] = 'win'


    if request.POST.get('type_request') == 'merchant trade':
        cargo_cards = CargoCard.objects.all() # drawing 3 cards
        # merchant cargo cards
        merchant_cargo_card_1 = random.choice(cargo_cards)
        merchant_cargo_card_2 = random.choice(cargo_cards)
        merchant_cargo_card_3 = random.choice(cargo_cards)
        serializer_1 = CargoCardSerializer(merchant_cargo_card_1)
        serializer_2 = CargoCardSerializer(merchant_cargo_card_2)
        serializer_3 = CargoCardSerializer(merchant_cargo_card_3)
        request.session['merchantCargoCard1'] = serializer_1.data
        request.session['merchantCargoCard2'] = serializer_2.data
        request.session['merchantCargoCard3'] = serializer_3.data
        
        data['merchantCargoCard1ImageUrl'] = request.session['merchantCargoCard1']['awers']
        data['merchantCargoCard2ImageUrl'] = request.session['merchantCargoCard2']['awers']
        data['merchantCargoCard3ImageUrl'] = request.session['merchantCargoCard3']['awers']

        # player cargo cards
        player_cargo_cards = StackPlayerCargoCards.objects.get(player_colour=player_colour)
        for i in range(1, 8):
            if (getattr(player_cargo_cards, (f"cargo_card_{i}"))):
                serializer = CargoCardSerializer(getattr(player_cargo_cards, (f"cargo_card_{i}")))
                request.session[f"playerCargoCard{i}"] = serializer.data
                data[f"playerCargoCard{i}ImageUrl"] = request.session[f"playerCargoCard{i}"]['awers']
        # captain influence
        data['playerCaptainInfluenceValue'] = player_captain_card.influence


    if request.POST.get('type_request') == 'merchant trade exchange cards':
        amount_success = int(request.POST.get('amountSuccess'))
        if amount_success > 0:
            pass
        print(dict(request.session))

    if request.POST.get('type_request') == 'merchant trade accept':
        print('AKCEPTUJĘ TRAXE Z MERCHANTGEM')

    if request.POST.get('type_request') == 'merchant escort':
        print('BĘDZIE ESKORTA KUPCA')

    return JsonResponse(data)
