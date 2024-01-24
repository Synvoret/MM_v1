from django.shortcuts import render
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations
from game.models import StackEventsCards
from game.models import StackEventsNPCCaptains
from game.models import StackMissionsCards
from game.models import TrackEnemyHitLocations

from game.models import PlayersGloryCards
from game.models import TrackPlayerHitLocations


def game(request):

    # Create random game
    # new_game = Game.objects.create()

    # RESET GAME
    Game.set_default_values()
    # RESET PLAYERS BOARDs
    PlayersGloryCards.set_values_default()
    TrackPlayerHitLocations.set_values_default()

    # RESET PLAYERs CAPTAINs CARDs
    PlayersCaptainsCards.set_default_values()

    # RESET PLAYERs SHIPs CARDs
    PlayersShipsCards.set_default_values()

    # RESET SHIPS LOCALISATIONs
    ShipsLocalisations.set_default_values()

    # RESET STACKs
    StackEventsCards.objects.all().delete()
    StackEventsNPCCaptains.objects.all().delete()
    StackMissionsCards.objects.all().delete()

    # RESET and create new track hit locations for Enemy.
    TrackEnemyHitLocations.objects.all().delete()
    TrackEnemyHitLocations.objects.create(game_number=Game.objects.get(pk=1))

    return render(request, 'game/game.html')
