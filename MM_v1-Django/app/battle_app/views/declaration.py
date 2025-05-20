import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


@csrf_exempt
def declaration(request):

    data = {}

    combat_record = CombatFlow.objects.first()

    if request.method == 'POST':

        request_data = json.loads(request.body)
        # datas from frontend
        side = request_data['side']
        action = request_data['act']

        combat_record.update_round_record(side, 'declaration', action)

    data = combat_record.combat[-1]

    return JsonResponse(data, safe=False)
