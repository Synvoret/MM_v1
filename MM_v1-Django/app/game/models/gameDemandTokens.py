from django.db import models
from dataset.models import DemandTokens
from .game import Game


class GameDemandTokens(models.Model):
    """Demands Tokens for Game."""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    basse_terre = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='basse_terre_demand_tokens', default=None)
    bridgetown = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='bridgetown_demand_tokens', default=None)
    caracas = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='caracas_demand_tokens', default=None)
    cartagena = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='cartagena_demand_tokens', default=None)
    curacao = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='curacao_demand_tokens', default=None)
    gulf_city = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='gulf_city_demand_tokens', default=None)
    nassau = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='nassau_demand_tokens', default=None)
    havana = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='havana_demand_tokens', default=None)
    old_providence = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='old_providence_demand_tokens', default=None)
    petite_goave = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='petite_goave_demand_tokens', default=None)
    port_royal = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='port_royal_demand_tokens', default=None)
    san_juan = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='san_juan_demand_tokens', default=None)
    santo_domingo = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='santo_domingo_demand_tokens', default=None)
    st_john = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='st_john_demand_tokens', default=None)
    st_maarten = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='st_maarten_demand_tokens', default=None)
    trinidad = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='trinidad_demand_tokens', default=None)
    tortuga = models.ForeignKey(DemandTokens, on_delete=models.CASCADE, null=True, blank=True, related_name='tortuga_demand_tokens', default=None)

    def __str__(self):
        return f"{self.game_number} Demands Token."
