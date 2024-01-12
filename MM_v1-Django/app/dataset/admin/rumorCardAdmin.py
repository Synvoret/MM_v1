from django.contrib import admin
from dataset.models import RumorCard


# admin.site.register(RumorCard)
@admin.register(RumorCard)
class RumorCardAdmin(admin.ModelAdmin):
    list_display = ()
