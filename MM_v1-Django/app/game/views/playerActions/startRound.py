from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from game.models import Game


@csrf_exempt
def startRound(request):
    """Player End turn."""

    data = {}
    game = Game.objects.get(number=100)

    # When PLAYER CLICK END TURN BUTTON
    if request.method == 'POST':
        print('JESTEM')
        # game.increment_rounds()

    return JsonResponse(data)
