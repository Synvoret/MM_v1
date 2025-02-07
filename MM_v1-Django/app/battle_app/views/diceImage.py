import random
from django.http import JsonResponse
from dataset.models import Dice


def diceImage(request):
    """Endpoint return a dice image."""

    data = {}

    dices = ['one', 'two', 'three', 'four', 'skull5', 'skull6']

    if request.method == 'GET':
        dice1 = Dice.objects.get(name='one')
        dice2 = Dice.objects.get(name='two')
        dice3 = Dice.objects.get(name='three')
        dice4 = Dice.objects.get(name='four')
        diceskull5 = Dice.objects.get(name='skull5')
        diceskull6 = Dice.objects.get(name='skull6')
        data["dice1Image"] = dice1.image.url
        data["dice2Image"] = dice2.image.url
        data["dice3Image"] = dice3.image.url
        data["dice4Image"] = dice4.image.url
        data["dice5Image"] = diceskull5.image.url
        data["dice6Image"] = diceskull6.image.url

    return JsonResponse(data)
