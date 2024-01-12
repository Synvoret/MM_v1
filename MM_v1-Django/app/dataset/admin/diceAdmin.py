from django.contrib import admin
from dataset.models import Dice


@admin.register(Dice)
class DiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'value']
