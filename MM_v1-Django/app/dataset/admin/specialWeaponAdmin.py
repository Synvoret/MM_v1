from django.contrib import admin
from dataset.models import SpecialWeapon


@admin.register(SpecialWeapon)
class SpecialWeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']