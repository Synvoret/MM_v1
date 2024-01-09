import random
from django.http import JsonResponse
from dataset.models import EventCard
from dataset.utils.dataset import events
from game.models import StackEventsCards
from game.models import Game


def drawEventCard(request):
    """Endpoint return a draw new Event Card."""

    # empty data dict for all events utils.
    response_data = {}

    # PRIMARY RANDOM CARD from EVENT DECK
    # cards = EventCard.objects.all()
    # random_card = random.choice(cards)
    random_card = EventCard.objects.get(card="Volatile Markets")

    event_util = getattr(events, random_card.card.lower().replace(" ", "_") )()
    response_data.update(event_util)

    game = Game.objects.get(pk=1)
    game.round = game.round + 1
    game.save()

    stack = StackEventsCards(game_number=game, game_round=game.round, event_card=random_card)
    stack.save()

    response_data["eventCardImage"] = random_card.awers.url

    return JsonResponse(response_data)
