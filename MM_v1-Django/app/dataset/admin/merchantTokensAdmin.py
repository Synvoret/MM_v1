from django.contrib import admin
from dataset.models import MerchantTokens


@admin.register(MerchantTokens)
class MerchantTokensAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')
