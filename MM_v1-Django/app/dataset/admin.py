from django.contrib import admin
from .models import Deck, Back, Cube, Flag
from .models import (
    EventCard,
    MissionCard,
    RumorCard,
    GloryCard,
    ShipCard,
    CaptainCard,
    DemandTokens,
    ShipModifications,
    MerchantTokens,
    LocationTokens,
)


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['deck', ]


@admin.register(Back)
class BackAdmin(admin.ModelAdmin):
    list_display = ['name', 'rewers']


@admin.register(Cube)
class CubeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(EventCard)
class EventCardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventCard._meta.get_fields()]


@admin.register(DemandTokens)
class DemandTokensAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DemandTokens._meta.get_fields()]


@admin.register(ShipModifications)
class ShipModificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')


@admin.register(MerchantTokens)
class MerchantTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')


@admin.register(LocationTokens)
class LocationTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers')


admin.site.register(MissionCard)
admin.site.register(RumorCard)
admin.site.register(GloryCard)
admin.site.register(ShipCard)
admin.site.register(CaptainCard)

