from django.http import JsonResponse
from dataset.models import SpecialWeapon
from game.models import Game
from game.models import TrackPlayerSpecialWeapons


def updatePlayerSpecialWeapons(request):
    """Endpoint update Player Special Weapons Token on player board."""

    data = {}

    player_colour = request.GET.get('colour')
    game = Game.objects.get(number=100)
    special_weapons_track = TrackPlayerSpecialWeapons.objects.get(game_number=game)

    for special_weapon in getattr(special_weapons_track, f"player_{player_colour}"):
        special_weapon_image = SpecialWeapon.objects.get(name=special_weapon)
        data[f"{special_weapon.title().replace('-', '').replace(' ', '')}Image"] = special_weapon_image.image.url

    return JsonResponse(data)
