import random
from django.http import HttpResponse
from dataset.models import ShipModifications


def drawShipModification(request):
    """Function return new randomly ship modifocation token for port."""

    all_tokens = ShipModifications.objects.all()
    random_token = random.choice(all_tokens)

    return HttpResponse(random_token.awers.url)
