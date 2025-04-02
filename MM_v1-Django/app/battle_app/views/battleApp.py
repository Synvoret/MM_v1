from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


@csrf_exempt
def battleApp(request):
    """Main view with list battle possibilities"""

    CombatFlow.objects.all().delete()

    return render(request, 'battle_app/battle_app.html')
