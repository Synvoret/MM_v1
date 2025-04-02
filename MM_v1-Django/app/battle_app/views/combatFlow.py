import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow


@csrf_exempt
def combatFlow(request):

    data = {}
    combat_record = CombatFlow.objects.first()

    if request.method == 'GET':
        if combat_record is None: # make first record, start battle
            combat_record = CombatFlow.objects.create()
            combat_record.first_round('Sloop')

    if request.method == 'POST':
        request_data = json.loads(request.body)
        # PO POST {'side': 'aggressor', 'parameter': 'declaration', 'value': 'Shoot'}
        print('PO POST', request_data)
        # datas from frontend
        side = request_data['side']
        parameter = request_data['parameter']
        value = request_data['value']
        next_round = request_data['next_round']
        # update round record
        combat_record.update_round_record(side, parameter, value)
        if combat_record.combat[-1]['aggressor']['declaration'] == combat_record.combat[-1]['defender']['declaration']:
            print('Obaj uciekają, koniec walki')
        # print(combat_record.combat[-1]['aggressor']['declaration'])
        # print(combat_record.combat[-1]['defender']['declaration'])

        if next_round:
            combat_record.next_round()

    # raw data
    data['roundRecord'] = combat_record.combat[-1]

    # processed data
    aggressor = combat_record.combat[-1]['aggressor']
    defender = combat_record.combat[-1]['defender']
    roles = ['aggressor', 'defender']

    # DECLARATION (Captains declare their tactics for this round)
    for role in roles:
        # Remember - In the first round the obnly possible action is shot
        if data['roundRecord']['round'] == 1:
            combat_record.update_round_record(role, 'declaration', 'shot')
        else:
            combat_record.update_round_record(role, 'actions', ['shot', 'board', 'flee'])
        # Remember - If crew are at 0, player cannot choose board
        if data['roundRecord'][role]['crew'] == 0:
            combat_record.update_round_record(role, 'actions', ['shot', 'flee'])
        # Remember - If masts are at 0 the only possible action is shot
        if data['roundRecord'][role]['masts'] == 0:
            combat_record.update_round_record(role, 'actions', ['shot'])


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

    # print(data['roundRecord'])

    return JsonResponse(data, safe=False)
