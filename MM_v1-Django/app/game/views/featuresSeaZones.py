from django.http import JsonResponse
from board.models import SeaZone


def featuresSeaZones(request):
    """Endpoint back text with features for Sea Zone."""

    data = {}

    sea_zone = (request.GET.get('sea_zone')).replace('-', " ").title()
    feature = SeaZone.objects.get(sea_zone_name=sea_zone)

    data['featureImage'] = feature.feature_image.url

    return JsonResponse(data)
