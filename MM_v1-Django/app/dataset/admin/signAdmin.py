from django.contrib import admin
from dataset.models import Sign


@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'value']
