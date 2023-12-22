import random
from django.http import HttpResponse
from dataset.models import LocationTokens


def putLocationToken(request):
    """Function return new randomly location token."""

    all_tokens = LocationTokens.objects.all()
    random_token = random.choice(all_tokens)

    return HttpResponse(random_token.awers.url)
