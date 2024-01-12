import random
from django.http import JsonResponse
from dataset.models import LocationTokens


def putLocationToken(request):
    """Function return new randomly location token."""

    all_tokens = LocationTokens.objects.all()
    random_token = random.choice(all_tokens)

    data = {
        "locationTokenImage": random_token.awers.url,
    }

    return JsonResponse(data)
