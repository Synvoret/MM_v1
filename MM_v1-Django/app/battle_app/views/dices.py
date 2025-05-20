import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from battle_app.models import CombatFlow
from dataset.models import Dice

@csrf_exempt
def dices(request):
    """Endpoint return a dice image."""

    data = {}
    combat_record = CombatFlow.objects.first()
    # raw data
    data['roundRecord'] = combat_record.combat[-1]

    name_dices = ['one', 'two', 'three', 'four', 'skull5', 'skull6']
    hits = {'1': 'cargo', '2': 'masts', '3': 'crew', '4': 'cannons', 'skull': 'choice'}

    if request.method == 'GET': # ONLY SHOW DICE WITH 1
        data['roundRecord']["dice1Image"] = Dice.get_dice("one")[0].image.url

    if request.method == 'POST': # WHEN the DICES WERE ROLLED (dicesRoll.js)
        request_data = json.loads(request.body)
        side = request_data['side']
        test = request_data['test']
        amount = request_data['amountDices'] # ????????????????????????????????????????, to wie z bazy
        for i in range(0, amount):
            dice = Dice.get_dice(random.choice(name_dices))
            if dice[0].name == 'skull5' or dice[0].name == 'skull6':
                data['roundRecord'][f"dice{i + 1}Image"] = dice[0].image.url
            else:
                data['roundRecord'][f"dice{i + 1}Image"] = dice[0].image.url
            combat_record.update_round_record(side, test, dice[0].value)

        # DICE ROLL COMPARISON
        count_aggressor_results = combat_record.combat[-1]['aggressor'][f'{test}_roll_result']
        count_defender_results = combat_record.combat[-1]['defender'][f'{test}_roll_result']

        # for seamanship test, comparison results
        if test == 'seamanship' and len(count_aggressor_results) > 0 and len(count_defender_results) > 0:
            if Dice.dice_comparison(count_aggressor_results, count_defender_results) == 'no success':
                combat_record.update_round_record('aggressor', 'seamanship_result', 'no success')
                combat_record.update_round_record('defender', 'seamanship_result', 'no success')
                data['roundRecord']['seamanshipResult'] = 'no success'
                combat_record.next_round()
            elif Dice.dice_comparison(count_aggressor_results, count_defender_results) == 'draw':
                combat_record.update_round_record('aggressor', 'seamanship_result', 'draw')
                combat_record.update_round_record('defender', 'seamanship_result', 'draw')
                data['roundRecord']['seamanshipResult'] = 'draw'
                combat_record.next_round()
            elif Dice.dice_comparison(count_aggressor_results, count_defender_results) == 'winner':
                combat_record.update_round_record('aggressor', 'seamanship_result', 'winner') # won
                combat_record.update_round_record('defender', 'seamanship_result', 'loser')
            elif Dice.dice_comparison(count_aggressor_results, count_defender_results) == 'loser':
                combat_record.update_round_record('aggressor', 'seamanship_result', 'loser') 
                combat_record.update_round_record('defender', 'seamanship_result', 'winner') # won

        # for shot test
        # if test == 'shot':
        #     print('strzały')

        #     if combat_record.combat[-1][side]['seamanship_result_comparison']:
        #         for result in combat_record.combat[-1][side]["shot_roll_result"]:
        #             print(result, hits[result])
        #         # print(f' {side} seamanship wygrał i strzelił z dział, trafienia-> {hits[(combat_flow.combat[-1][side]["shot_roll_result"][0])]}')
        #             combat_record.update_round_record(side, hits[result], 1)
        #     elif combat_record.combat[-1][side]['seamanship_result_comparison'] == False:
        #         for result in combat_record.combat[-1][side]["shot_roll_result"]:
        #             print(result, hits[result])
        #             combat_record.update_round_record(side, hits[result], 1)
        #         print(f' {side} seamanship przegrał więc strzela za każdy sukces w seamnaship')
        #     # comparison results
        #     if len(count_aggressor_results) > 0 and len(count_defender_results) > 0:
        #         print(side, test, amount, f'{test}_roll_result')
        #         print('OBA STRZAŁY WYKONANE< BAZA ZAKTUALIZOWANA WIEC PRZECHODZEMY DO NASTEPNEJ RUNDY')
        #         data['hits'] = hits
        #         data['resultNextRound'] = True


    # if combat_record.combat[-1]['aggressor']['hull'] == 0 or combat_record.combat[-1]['defender']['hull'] == 0:
    #     data['shipSunk'] = True

    # data['round'] = combat_record.combat[-1]['round']
    # data['aggressor'] = combat_record.combat[-1]['aggressor']
    # data['defender'] = combat_record.combat[-1]['defender']


    return JsonResponse(data, safe=False)
