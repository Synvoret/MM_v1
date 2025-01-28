import random
from django.http import JsonResponse
from dataset.models import MerchantTokens
from game.models import Game
from game.models import ShipsLocalisations


def drawMerchantToken(request):
    """Function return new randomly Merchant Token fo Sea Zone."""

    data = {}
    all_tokens = MerchantTokens.objects.all()
    random_token = random.choice(all_tokens)

    if str(request.GET.get('seaZone')).title() != 'Basse-Terre':
        new_merchant_localisation = str(request.GET.get('seaZone')).replace('-', ' ').title()
    else:
        new_merchant_localisation = str(request.GET.get('seaZone')).title()


    game = Game.objects.get(number=100)
    merchant_localisation = ShipsLocalisations.objects.get(game_number=game)
    merchant_nationality = random_token.nationality
    if merchant_localisation.merchants_ship is None:
        merchant_localisation.merchants_ship = {}
    merchant_localisation.merchants_ship[new_merchant_localisation] = merchant_nationality
    merchant_localisation.save()

    awers_image = random_token.awers.url
    rewers_image = str(random_token.rewers)

    data['merchantTokenAwersImage'] = awers_image
    data['merchantTokenRewersImage'] = rewers_image

    return JsonResponse(data)
