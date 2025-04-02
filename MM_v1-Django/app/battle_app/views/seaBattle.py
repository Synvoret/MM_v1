import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


@csrf_exempt
def seaBattle(request):

    data = {}

    combat_record = CombatFlow.objects.first()

    if request.method == 'POST':

        request_data = json.loads(request.body)
        # datas from frontend
        # stage = request_data['stage']

        if combat_record is None: # make first record, start battle
            combat_record = CombatFlow.objects.create()
            combat_record.first_round('Sloop')
        # elif stage == 'next':
        #     combat_record.next_round()

    data = combat_record.combat

    return JsonResponse(data, safe=False)
