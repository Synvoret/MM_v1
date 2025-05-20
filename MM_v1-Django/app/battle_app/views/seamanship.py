import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


def seamanship(request):

    data = {}
    combat_record = CombatFlow.objects.first()
    # raw data
    data['roundRecord'] = combat_record.combat[-1]
    # processed data
    aggressor = combat_record.combat[-1]['aggressor']
    defender = combat_record.combat[-1]['defender']

    # SEAMANSHIP (Captains use their seamanship to try to gain the upper hand) 2 Combat Flow Diagram
    # Remember - Add 1 die seamanship if a ship's maneuverability is 2+ higher than the opponent's
    if aggressor['maneuverability'] - defender['maneuverability'] <= -2:
        data['roundRecord']['defender']['seamanship'] += 1
    elif aggressor['maneuverability'] - defender['maneuverability'] >= 2:
        data['roundRecord']['aggressor']['seamanship'] += 1
    # Rememeber - If masts are at 0 roll only one die for seamanship
    if aggressor['masts'] == 0:
        data['roundRecord']['aggressor']['seamanship'] = 1
    if defender['masts'] == 0:
        data['roundRecord']['defender']['seamanship'] = 1

    return JsonResponse(data, safe=False)