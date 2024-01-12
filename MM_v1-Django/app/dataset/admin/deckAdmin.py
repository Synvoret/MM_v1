from django.contrib import admin
from dataset.models import Deck

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['deck', ]
