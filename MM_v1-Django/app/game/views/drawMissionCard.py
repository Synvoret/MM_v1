import random
from django.http import JsonResponse
from dataset.models import MissionCard
from dataset.models import Sign
from game.models import Game
from game.models import StackMissionsCards


def drawMissionCard(request):
    """Endpoint return a draw new Mission Card depending from number."""

    mission_number = request.GET.get('mission_number')
    mission_sign = Sign.objects.get(value=mission_number)
    game = Game.objects.get(number=100)

    cards = MissionCard.objects.all()
    random_card = random.choice(cards)

    try:
        stack = StackMissionsCards.objects.get(game_round=game.rounds)
    except:
        stack = StackMissionsCards(game_number=game, game_round=game.rounds)

    if int(mission_number) == 1:
        stack.mission_1_card = random_card
    elif int(mission_number) == 2:
        stack.mission_2_card = random_card
    elif int(mission_number) == 3:
        stack.mission_3_card = random_card

    stack.save()

    data = {
        'cardImage': random_card.awers.url,
        'portMission': random_card.port.lower().replace(' ', '-'),
        'signMission': mission_sign.image.url,
    }

    return JsonResponse(data)
