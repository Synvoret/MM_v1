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

    name_dices = ['one', 'two', 'three', 'four', 'skull5', 'skull6']

    if request.method == 'GET': # only show dice with 1
        dice1 = Dice.objects.get(name='one')
        data["dice1Image"] = dice1.image.url

    if request.method == 'POST': # dicesRoll.js
        request_data = json.loads(request.body)
        # print(request_data)
        side = request_data['side']
        test = request_data['test']
        amount = request_data['amountDices']
        dices = Dice.objects.all()
        combat_flow = CombatFlow.objects.first()
        for i in range(0, amount):

            dice = dices.get(name=random.choice(name_dices))

            if dice.name == 'skull5' or dice.name == 'skull6':
                data[f"dice{i + 1}Image"] = dice.image.url
            else:
                data[f"dice{i + 1}Image"] = dice.image.url

            combat_flow.update_round_record(side, test, dice.value)

        data['aggressorResults'] = combat_flow.combat[-1]['aggressor'][f'{test}_roll_result']
        data['defenderResults'] = combat_flow.combat[-1]['defender'][f'{test}_roll_result']
        data['aggressorDeclaration'] = combat_flow.combat[-1]['aggressor']['declaration']
        data['defenderDeclaration'] = combat_flow.combat[-1]['defender']['declaration']
        data['aggressor'] = combat_flow.combat[-1]['aggressor']
        data['defender'] = combat_flow.combat[-1]['defender']


    return JsonResponse(data)
