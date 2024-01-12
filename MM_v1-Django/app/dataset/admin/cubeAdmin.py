from django.contrib import admin
from dataset.models import Cube


@admin.register(Cube)
class CubeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
