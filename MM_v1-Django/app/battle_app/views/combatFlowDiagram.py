from django.http import JsonResponse
from battle_app.models import CombatFlowDiagram

def combatFlowDiagram(request):
    """View responsible for show Combat Flow Diagram on wweb page."""

    data = {}

    combat_flow_diagram = CombatFlowDiagram.objects.get(name='Combat Flow Diagram')

    data['combatFlowDiagramImage'] = combat_flow_diagram.diagram.url

    return JsonResponse(data)
