from django.contrib import admin
from .models import Game
from .models import StackEventsCards
from .models import StackMissionsCards
from .models import TrackEnemyHitLocations
from .models import PlayersCaptainsCards
from .models import PlayersShipsCards
from .models import PlayersGloryCards
from .models import TrackPlayerHitLocations
from .models import TrackGloryPoint
from .models import TrackLoyality
from .models import TrackFavors
from .models import TrackPlayerGolds


# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Game Admin model."""

    list_display = ['number', 'round', 'amount_players']


@admin.register(StackEventsCards)
class StackEventsCardsAdmin(admin.ModelAdmin):
    """Stack Events Cards on board for game."""

    list_display = [
        'game_number',
        'game_round',
        'event_card',
    ]


@admin.register(StackMissionsCards)
class StackMissionsCardsAdmin(admin.ModelAdmin):
    """Stack Missions Cards on board for game."""

    list_display = [
        'game_number',
        'game_round',
        'mission_1_card',
        'mission_2_card',
        'mission_3_card',
    ]


@admin.register(TrackEnemyHitLocations)
class TrackEnemyHitLocationsAdmin(admin.ModelAdmin):
    """Ttack Enemy Hit Locations on board for game."""

    list_display = [
        'game_number',
        'game_round',

        'hull',
        'cargo',
        'masts',
        'crew',
        'cannons'
    ]

@admin.register(PlayersCaptainsCards)
class PlayersCaptainsCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',
        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]


@admin.register(PlayersShipsCards)
class PlayersShipsCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',
        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]


@admin.register(PlayersGloryCards)
class PlayersGloryCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',
        'player_colour',
        'glory_card_1',
        'glory_card_2',
        'glory_card_3',
        'glory_card_4',
        'glory_card_5',
        'glory_card_6',
    ]


@admin.register(TrackPlayerHitLocations)
class TrackPlayerHitLocationsAdmin(admin.ModelAdmin):
    """Ttack Player Hit Locations on board for game."""

    list_display = [
        'game_number',
        'game_round',
        'player_colour',

        'hull',
        'cargo',
        'masts',
        'crew',
        'cannons'
    ]

@admin.register(TrackGloryPoint)
class TrackGloryPointAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]


@admin.register(TrackLoyality)
class TrackLoyalityAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]


@admin.register(TrackFavors)
class TrackFavorsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]


@admin.register(TrackPlayerGolds)
class TrackPlayerGoldsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',
        'player_colour',

        'amount_gold',
    ]
