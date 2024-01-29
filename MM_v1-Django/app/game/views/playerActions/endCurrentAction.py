from django.http import JsonResponse


def endCurrentAction(request):
    """Endpoint finishing currently performed action by player and moving on to selected next one."""

    data = {}

    return JsonResponse(data)
