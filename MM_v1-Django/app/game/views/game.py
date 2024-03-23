from django.shortcuts import render
from nav.models import NavBarGame
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations
from game.models import StackEventsCards
from game.models import StackEventsNPCCaptains
from game.models import StackMissionsCards
from game.models import StackPlayerCargoCards
from game.models import TrackGloryPoint
from game.models import TrackEnemyHitLocations
from game.models import TrackPlayerGolds

from game.models import PlayersGloryCards
from game.models import TrackFavors
from game.models import TrackLoyality
from game.models import TrackPlayerBounties
from game.models import TrackPlayerHitLocations
from game.models import TrackPlayersShipModifications
from game.models import TrackPlayerSpecialWeapons
from game.models import TrackMerchantTokens


def game(request):

    # Create random game
    # new_game = Game.objects.create()

    # RESET SESSION
    request.session.clear()

    # RESET GAME
    Game.set_default_values()
    # RESET NAVBAR
    NavBarGame.set_default_values()
    # RESET PLAYERS BOARDs
    TrackLoyality.set_values_default()
    TrackFavors.set_values_default()
    TrackGloryPoint.set_values_default()
    PlayersGloryCards.set_values_default()
    StackPlayerCargoCards.set_default_values()
    TrackPlayerBounties.set_default_values()
    TrackPlayerHitLocations.set_values_default()
    TrackPlayersShipModifications.set_default_values()
    TrackPlayerSpecialWeapons.set_default_values()
    TrackMerchantTokens.set_default_values()

    # RESET PLAYERs CAPTAINs CARDs
    PlayersCaptainsCards.set_default_values()

    # RESET PLAYERs SHIPs CARDs
    PlayersShipsCards.set_default_values()

    # RESET PLAYERs GOLDs
    TrackPlayerGolds.set_default_values()

    # RESET SHIPS LOCALISATIONs
    ShipsLocalisations.set_default_values()

    # RESET STACKs
    StackEventsCards.objects.all().delete()
    StackEventsNPCCaptains.objects.all().delete()
    StackMissionsCards.objects.all().delete()

    # RESET and create new track hit locations for Enemy.
    TrackEnemyHitLocations.set_default_values()

    return render(request, 'game/game.html')
