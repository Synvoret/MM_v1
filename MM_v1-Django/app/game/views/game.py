from django.shortcuts import render
from game.models import Game
from game.models import StackEventsCards
from game.models import StackMissionsCards
from game.models import TrackEnemyHitLocations


def game(request):

    # Create random game
    # new_game = Game.objects.create()

    # Reset ROUNDs
    Game.objects.update(round=0)

    # Reset STACKs
    StackEventsCards.objects.all().delete()
    StackMissionsCards.objects.all().delete()

    # Reset and create new track hit locations for Enemy.
    TrackEnemyHitLocations.objects.all().delete()
    TrackEnemyHitLocations.objects.create(game_number=Game.objects.get(pk=1))


    return render(request, 'game/game.html')
