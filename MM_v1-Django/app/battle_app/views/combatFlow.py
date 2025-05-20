import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow
from dataset.models import Dice


@csrf_exempt
def combatFlow(request):

    data = {}
    name_dices = ['one', 'two', 'three', 'four', 'skull5', 'skull6']
    combat_record = CombatFlow.objects.first()
    if combat_record is None: # make first record, start battle
        combat_record = CombatFlow.objects.create()
        combat_record.first_round('Sloop')
    # raw data
    data['roundRecord'] = combat_record.combat[-1]
    # DECLARATION (Captains declare their tactics for this round)
    for role in ['aggressor', 'defender']:
        # Remember - In the first round the only possible action is shot
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
            # when masts and cannons = 0, no actions to choose
            # if data['roundRecord'][role]['cannons'] == 0: 
            #     combat_record.update_round_record(role, 'actions', ['null'])
    # REQUESTs
    if request.method == 'GET':
        data['roundRecord']["dice1Image"] = Dice.get_dice("one")[0].image.url

    if request.method == 'POST':
        request_data = json.loads(request.body)
        # print(request_data)
        # datas from frontend
        side = request_data['side']
        parameter = request_data['parameter']
        # print(parameter)
        value = request_data['value']
        phase = request_data['phase']
        next_round = request_data['next_round']

        # after roll parameter/test
        if parameter == 'seamanship':
            for i in range(combat_record.combat[-1][side][parameter]):
                dice = Dice.get_dice(name=random.choice(name_dices))
                data['roundRecord'][f"dice{i + 1}Image"] = dice[0].image.url
                # update round record
                combat_record.update_round_record(side, parameter, dice[0].value)
            if len(combat_record.combat[-1]['aggressor'][f"{parameter}_roll_result"]) > 0 and len(combat_record.combat[-1]['defender'][f"{parameter}_roll_result"]) > 0:
                result = Dice.dice_comparison(combat_record.combat[-1]['aggressor'][f"{parameter}_roll_result"], combat_record.combat[-1]['defender'][f"{parameter}_roll_result"])
                if result:
                    combat_record.update_round_record('aggressor', 'seamanship_result', True)
                    combat_record.update_round_record('defender', 'seamanship_result', False)
                    data['roundRecord']['seamanshipResult'] = {'winner': 'aggressor', 'loser': 'defender'}
                elif result is False:
                    combat_record.update_round_record('defender', 'seamanship_result', True)
                    combat_record.update_round_record('aggressor', 'seamanship_result', False)
                    data['roundRecord']['seamanshipResult'] = {'winner': 'defender', 'loser': 'aggressor'}
                else:
                    data['roundRecord']['seamanshipResult'] = {'winner': 'draw', 'loser': 'draw'}

        if parameter == 'shot':
            pass

        if combat_record.combat[-1]['aggressor']['declaration'] == combat_record.combat[-1]['defender']['declaration']:
            # print('Obaj uciekają, koniec walki')
            pass

        if next_round:
            combat_record.next_round()


    # print(data['roundRecord'])

    return JsonResponse(data, safe=False)
