from django.http import JsonResponse


def endAllActions(request):
    """Endpoint finishing after all action by player and moving on to selected next one."""

    data = {}

    return JsonResponse(data)
