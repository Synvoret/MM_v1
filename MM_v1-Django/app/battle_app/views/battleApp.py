from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def battleApp(request):
    """Main view with list battle possibilities"""

    return render(request, 'battle_app/battle_app.html')
