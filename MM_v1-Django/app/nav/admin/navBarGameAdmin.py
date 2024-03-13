from django.contrib import admin
from nav.models import NavBarGame


@admin.register(NavBarGame)
class NavBarGameAdmin(admin.ModelAdmin):
    """Game Nav Admin panel."""

    list_display = [field.name for field in NavBarGame._meta.get_fields() if field.name not in ['id']]
