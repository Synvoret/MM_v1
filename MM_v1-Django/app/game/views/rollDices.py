import random
from django.http import JsonResponse
from dataset.models import Dice


def rollDices(request):
    """Endpoint return a roll dice."""

    data = {}

    # CREATE 
    if request.GET.get('type') == 'create':
        dice1 = Dice.objects.get(name='one')
        data["dice1Image"] = dice1.image.url

    # ROLL
    if request.GET.get('type') == 'roll':
        dices = Dice.objects.all()
        amount_dices = int(request.GET.get('amountDices'))
        for i in range(1, amount_dices + 1):
            random_dice = random.choice(dices)
            data[f"dice{i}Image"] = random_dice.image.url
            data[f"dice{i}Value"] = random_dice.value

    data['playerColour'] = request.session['playerColourActive']
    return JsonResponse(data)
