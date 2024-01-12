from django.contrib import admin
from dataset.models import Back


@admin.register(Back)
class BackAdmin(admin.ModelAdmin):
    list_display = ['name', 'rewers']
