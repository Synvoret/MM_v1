from django.contrib import admin
from game.models import TrackMerchantTokens


@admin.register(TrackMerchantTokens)
class TrackMerchantTokensAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'first',
        'second',
        'thrith',
        'fourth',
        'fivth',
        'sixth',
        'seventh',
        'eighth',
    ]
