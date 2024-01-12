from django.contrib import admin
from dataset.models import Flag


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
