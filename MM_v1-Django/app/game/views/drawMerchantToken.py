import random
from django.http import HttpResponse
from dataset.models import MerchantTokens

def drawMerchantToken(request):
    """Function return new randomly ship modifocation token for port."""

    all_tokens = MerchantTokens.objects.all()
    random_token = random.choice(all_tokens)

    awers_image = random_token.awers.url
    rewers_image = random_token.rewers

    # return HttpResponse(awers_image)
    return HttpResponse(rewers_image)
