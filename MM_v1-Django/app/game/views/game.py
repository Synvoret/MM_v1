from django.shortcuts import render
from game.models import Game
from game.models import ShipsLocalisations
from game.models import StackEventsCards
from game.models import StackEventsNPCCaptains
from game.models import StackMissionsCards
from game.models import TrackEnemyHitLocations


def game(request):

    # Create random game
    # new_game = Game.objects.create()

    # Reset ROUNDs
    Game.objects.update(round=0)

    ShipsLocalisations.objects.all().update(
        blue_ship=None,
        green_ship= None,
        red_ship= None,
        yellow_ship= None,

        dutch_ship= None,
        english_ship= None,
        french_ship= None,
        spanish_ship= None,

        small_pirate_ship= None,
        large_pirate_ship= None,
    )

    # Reset STACKs
    StackEventsCards.objects.all().delete()
    StackEventsNPCCaptains.objects.all().delete()
    StackMissionsCards.objects.all().delete()

    # Reset and create new track hit locations for Enemy.
    TrackEnemyHitLocations.objects.all().delete()
    TrackEnemyHitLocations.objects.create(game_number=Game.objects.get(pk=1))


    return render(request, 'game/game.html')
