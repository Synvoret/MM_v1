from django.db import models


class CombatFlowDiagram(models.Model):
    """Combat Flow Diagram in pdf/page."""

    name = models.CharField(max_length=150, default='Combat Flow Diagram')
    diagram = models.ImageField(upload_to='battleApp/' ,null=True, blank=True)

    def __str__(self):
        return f"Combat Flow Diagram."
