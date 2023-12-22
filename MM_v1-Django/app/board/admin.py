from django.contrib import admin
from .models import Board
from .models import SeaZone
# from .models import (
#     StackEventsCards,
#     StackNPCDutchCaptains,
#     StackNPCEnglishCaptains,
#     StackNPCFrenchCaptains,
#     StackNPCSpanishCaptains,
#     StackNPCSloopPirate,
#     StackNPCFrigatePirate,
# )
# from .models import (
#     TrackMerchantToken,
#     TrackGloryPoints,
#     TrackEnemyHitLocation,
#     TrackMissions,
#     TrackAtWar,
# )

# admin.site.register(Board)
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'board')


@admin.register(SeaZone)
class SeaZoneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SeaZone._meta.get_fields()]
    search_fields = ('sea_zone_name', )


# @admin.register(StackEventsCards)
# class StackEventsCardsAdmin(admin.ModelAdmin):
#     list_display = ('board', 'event_card')


# @admin.register(StackNPCDutchCaptains)
# class StackNPCDutchCaptainsAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_dutch_captain')


# @admin.register(StackNPCEnglishCaptains)
# class StackNPCEnglishCaptainsAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_english_captain')


# @admin.register(StackNPCFrenchCaptains)
# class StackNPCFrenchCaptainsAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_french_captain')


# @admin.register(StackNPCSpanishCaptains)
# class StackNPCSpanishCaptainsAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_spanish_captain')


# @admin.register(StackNPCSloopPirate)
# class StackNPCSloopPirateAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_sloop_pirate')


# @admin.register(StackNPCFrigatePirate)
# class StackNPCFrigatePirateAdmin(admin.ModelAdmin):
#     list_display = ('board', 'npc_frigate_pirate')


# @admin.register(TrackMissions)
# class TrackMissionsAdmin(admin.ModelAdmin):
#     list_display = (
#         'board',
#         'card_one',
#         'card_two',
#     )


# @admin.register(TrackEnemyHitLocation)
# class TrackEnemyHitLocationAdmin(admin.ModelAdmin):
#     list_display = (
#         'hull',
#         'cargo',
#         'masts',
#         'crew',
#         'cannons',
#     )


# @admin.register(TrackMerchantToken)
# class TrackMerchantTokenAdmin(admin.ModelAdmin):
#     list_display = (
#         'board',
#         'first',
#         'second',
#         'thirth',
#         'fourth',
#         'fifth',
#         'sixth',
#         'seventh',
#         'eighth',
#     )


# @admin.register(TrackGloryPoints)
# class TrackGloryPointsAdmin(admin.ModelAdmin):
#     list_display = (
#         'board', 
#         'blue_player', 
#         'green_player',
#         'red_player',
#         'yellow_player',
#         )


# @admin.register(TrackAtWar)
# class TrackAtWarAdmin(admin.ModelAdmin):
#     list_display = (
#         'board',
#         'section_left',
#         'section_right',
#     )

# @admin.register(HavanaSeaZone)
# class HavanaSeaZoneAdmin(admin.ModelAdmin):
#     list_display = (
#         'board',
#         'demand',
#         'modification',
#         'nationality',
#         'merchant',
#         'location',
#     )
# @admin.register(NassauSeaZone)
# class NassauSeaZoneAdmin(admin.ModelAdmin):
#     list_display = (
#         'board',
#         'demand',
#         'modification',
#         'nationality',
#         'merchant',
#         'location',
#     )
