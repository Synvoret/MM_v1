from django.http import JsonResponse
# from dataset.utils.dataset.decorators.choices import BOUNTIES
from game.models import Game
from game.models import StackPlayerCargoCards


def updatePlayerCargoCards(request):
    """Endpoint update Player Cargo Cards on player board."""

    data = {}

    if request.method == 'GET':

        player_colour = request.GET.get('colour')
        game = Game.objects.get(number=100)
        stack_player_cargo_cards_instance = StackPlayerCargoCards.objects.get(player_colour=player_colour)

        for cargo_card_number in range(1, 9):
            cargo_card = getattr(stack_player_cargo_cards_instance, f"cargo_card_{cargo_card_number}")
            if cargo_card:
                data[f"cargoCard{cargo_card_number}Image"] = cargo_card.awers.url

    return JsonResponse(data)
