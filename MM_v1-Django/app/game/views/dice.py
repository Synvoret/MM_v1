import random
from django.http import HttpResponse, JsonResponse
from dataset.models import Dice


def dice(request):
    """Endpoint return a roll dice."""

    dices = Dice.objects.all()
    random_dice = random.choice(dices)

    data = {
        "diceImage": random_dice.image.url,
        "diceValue": random_dice.value
    }

    return JsonResponse(data)
