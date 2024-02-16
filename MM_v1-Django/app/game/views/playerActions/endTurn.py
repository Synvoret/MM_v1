from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from game.models import Game


@csrf_exempt
def endTurn(request):
    """Player End turn."""

    data = {}
    game = Game.objects.get(number=100)

    if 'amountActions' in request.session:
        del request.session['amountActions']

    if 'currentAction' in request.session:
        del request.session['currentAction']

    player_colour = request.session['playerColourActive']
    data['playerColourEndingTurn'] = player_colour

    # When PLAYER CLICK END TURN BUTTON
    if request.method == 'POST':

        setattr(game, f'player_{player_colour}_done', True)
        game.save()

        # Is it end round?
        game = Game.objects.get(number=100)
        players = {
            'blue': (game.player_blue_play, game.player_blue_done),
            'green': (game.player_green_play, game.player_green_done),
            'red': (game.player_red_play, game.player_red_done),
            'yellow': (game.player_yellow_play, game.player_yellow_done),
        }
        request.session['whoEnded'] = 0
        for player in players.keys():
            if players[player][0] and players[player][1]:
                request.session['whoEnded'] += 1
                if request.session['whoEnded'] == game.amount_players:
                    data['endRound'] = True
                    print('KONIEC RUNDY')
            else:
                print('TOJESZCZE NIE KONIEC RUNDY')

        # return next_player()

        return JsonResponse(data)
