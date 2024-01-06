import random
from django.http import HttpResponse
from dataset.models import EventCard
from game.models import StackEventsCards
from game.models import Game


def drawEventCard(request):
    """Endpoint return a draw new Event Card."""

    cards = EventCard.objects.all()
    random_card = random.choice(cards)

    game = Game.objects.get(pk=1)
    game.round = game.round + 1
    game.save()
    stack = StackEventsCards(game_number=game, game_round=game.round, event_card=random_card)
    stack.save()

    return HttpResponse(random_card.awers.url)
