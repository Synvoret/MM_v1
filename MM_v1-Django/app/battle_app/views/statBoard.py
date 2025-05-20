import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


def statBoard(request):

    data = {}
    combat_record = CombatFlow.objects.first()
    # raw data
    data['roundRecord'] = combat_record.combat[-1]

    return JsonResponse(data, safe=False)
