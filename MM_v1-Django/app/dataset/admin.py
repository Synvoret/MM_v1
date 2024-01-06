from django.contrib import admin
from .models import Deck, Coin, Back, Cube, Flag, Dice, Sign, Ship
from .models import (
    EventCard,
    MissionCard,
    RumorCard,
    GloryCard,
    ShipCard,
    CaptainCard,
    DemandTokens,
    ShipModifications,
    SpecialWeapon,
    MerchantTokens,
    LocationTokens,
)


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['deck', ]


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['coin', 'image', 'value']


@admin.register(Back)
class BackAdmin(admin.ModelAdmin):
    list_display = ['name', 'rewers']


@admin.register(Dice)
class DiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'value']


@admin.register(Cube)
class CubeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'value']


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'colour', 'image']


@admin.register(EventCard)
class EventCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'dutch_direction',
        'english_direction',
        'french_direction',
        'spanish_direction',
        'pirateFrigate_direction',
        'pirateSloop_direction',
        'notes',
    ]


@admin.register(MissionCard)
class MissionCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'earn',
        'requirements',
        'port',
        'notes'
    ]


@admin.register(ShipCard)
class ShipCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'ship',
        'expansion',
        'awers',
        'toughness',
        'cargo',
        'crew',
        'cannons',
        'maneuverability',
        'speed',
        'boats',
        'notes',
    ]



@admin.register(CaptainCard)
class CaptainCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'captain',
        'expansion',
        'awers',
        'home_port',
        'nationality',
        'seamanship',
        'scouting',
        'leadership',
        'influence',
        'notes',
    ]


@admin.register(GloryCard)
class GloryCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'notes',
    ]














@admin.register(DemandTokens)
class DemandTokensAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DemandTokens._meta.get_fields()]


@admin.register(ShipModifications)
class ShipModificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')


@admin.register(SpecialWeapon)
class SpecialWeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(MerchantTokens)
class MerchantTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')


@admin.register(LocationTokens)
class LocationTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers')


admin.site.register(RumorCard)

