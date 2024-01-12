from django.contrib import admin
from dataset.models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['coin', 'image', 'value']
