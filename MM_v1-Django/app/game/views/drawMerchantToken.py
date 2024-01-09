import random
from django.http import JsonResponse
from dataset.models import MerchantTokens

def drawMerchantToken(request):
    """Function return new randomly ship modifocation token for port."""

    all_tokens = MerchantTokens.objects.all()
    random_token = random.choice(all_tokens)

    awers_image = random_token.awers.url
    rewers_image = str(random_token.rewers)

    data = {
        "merchantTokenAwersImage": awers_image,
        "merchantTokenRewersImage": rewers_image,
    }
    return JsonResponse(data)
