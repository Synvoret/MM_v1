from django.contrib import admin
from dataset.models import DemandTokens


@admin.register(DemandTokens)
class DemandTokensAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in DemandTokens._meta.get_fields() if not (field.many_to_many or field.one_to_many)]

    list_display = [
        'cargo',
        'awers',
    ]
