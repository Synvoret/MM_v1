import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow

@csrf_exempt
def round(request):
    """Round view."""

    data = {}

    combat_record = CombatFlow.objects.first()
    print(combat_record)

    if request.method == 'POST':
        # data['round'] = combat_record.round
        data['round'] = 'RUNDA 1'

    # if request.method == 'POST':

    #     request_data = json.loads(request.body)
    #     # datas from frontend
    #     stage = request_data['stage']
    #     action = request_data['action']

    #     print(request_data)

    #     if combat_record is None: # make first record, start battle
    #         combat_record = CombatFlow.objects.create()
    #         combat_record.first_round('Sloop')
    #     elif stage == 'next':
    #         print(action)
    #         combat_record.next_round()

    # data = combat_record.combat

    # data['round'] = combat_record.round

    return JsonResponse(data, safe=False)


