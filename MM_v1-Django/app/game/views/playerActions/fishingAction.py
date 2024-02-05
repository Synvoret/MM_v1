import random
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.models import FishingCard
from game.models import Game
from game.models import TrackPlayerGolds
from game.models import TrackPlayerHitLocations
from game.serializers import FishingCardSerializer


@csrf_exempt
def fishingAction(request):
    """Endpoint return a randomly fishing card."""

    player_colour = request.session['playerColourActive']

    # SERIALIZER
    if 'fishingCard' not in request.session:
        # if does not exist, generate new randomly card and save in session
        fishing_cards = FishingCard.objects.all()
        random_fishing_card = random.choice(fishing_cards)
        # Serialize object to JSON and save in session
        serializer = FishingCardSerializer(random_fishing_card)
        serialized_fishing_card = serializer.data
        request.session['fishingCard'] = serialized_fishing_card
    else:
        # if exist in session
        serialized_fishing_card = request.session['fishingCard']
        serializer = FishingCardSerializer(data=serialized_fishing_card)
        serializer.is_valid()
        random_fishing_card = serializer.validated_data


    # REQUEST METHOD GET
    if request.method == 'GET':
        data = {
            'fishingCardImage': request.session['fishingCard']['awers'],
            'playerColour': player_colour,
        }
        return JsonResponse(data)


    # REQUEST METHOD POST
    if request.method == 'POST':
        data = {}
        fishing_card = request.session['fishingCard']
        game = Game.objects.get(number=100)
        if fishing_card['fishing_value']:
            player_golds = TrackPlayerGolds.objects.get(game_number=game)
            setattr(player_golds, 'player_' + player_colour, getattr(player_golds, 'player_' + player_colour) + fishing_card['fishing_value'])
            player_golds.save()
            data['fishingValue'] = True
        if fishing_card['fishing_hits']: 
            player_hits_locations = TrackPlayerHitLocations.objects.get(player_colour=player_colour.title())
            hit_location = fishing_card['fishing_hits']
            setattr(player_hits_locations, hit_location.lower(), getattr(player_hits_locations, hit_location.lower()) - 1)
            player_hits_locations.save()
            data['fishingHits'] = True
        del request.session['fishingCard']
        data['colour'] = player_colour
        return JsonResponse(data)
