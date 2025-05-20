import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


def shooting(request):

    data = {}
    combat_record = CombatFlow.objects.first()
    # raw data
    data['roundRecord'] = combat_record.combat[-1]
    # loser shot for all succes in seamanship
    for side in ['aggressor', 'defender']:
        if data['roundRecord'][side]['seamanship_result_comparison'] == 'loser':
            shots = 0
            for success in data['roundRecord'][side]['seamanship_roll_result']:
                if success == 'skull':
                    shots += 1
            if shots > data['roundRecord'][side]['cannons']:
                shots = data['roundRecord'][side]['cannons']
            data['roundRecord'][side]['cannons'] = shots
            break

    return JsonResponse(data, safe=False)