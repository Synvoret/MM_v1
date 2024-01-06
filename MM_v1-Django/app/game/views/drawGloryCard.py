import random
from django.http import HttpResponse, JsonResponse
from dataset.models import GloryCard
from game.models import PlayersGloryCards
from game.models import Game


def drawGloryCard(request):
    """Endpoint return a draw new Glory Card."""

    colour = request.GET.get('colour', None)

    cards = GloryCard.objects.all()
    glory_card = random.choice(cards)
    glory_card_image = glory_card.awers.url

    stack = PlayersGloryCards.objects.get(player_colour=colour.capitalize())

    if not getattr(stack, 'glory_card_1'):
        stack.glory_card_1 = glory_card
        stack.save()

    data = {
        "gloryCardImage": glory_card_image,
    }

    return JsonResponse(data)
