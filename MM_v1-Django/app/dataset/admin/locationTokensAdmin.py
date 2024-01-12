from django.contrib import admin
from dataset.models import LocationTokens


@admin.register(LocationTokens)
class LocationTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers')
