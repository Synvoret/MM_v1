from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import HIT_LOCATIONS
from dataset.models import CaptainCard
from dataset.models import ShipCard
from game.models import Game
from game.models import PlayersCaptainsCards, PlayersShipsCards
from game.models import ShipsLocalisations
from game.models import TrackPlayerHitLocations


@csrf_exempt
def saveToServerSelectedNewCaptainShip(request):
    """Save new Captain and ship for player before start game.."""

    if request.method == 'POST':

        data = {}
        game = Game.objects.get(number=100)

        player_colour = request.POST.get('colour')
        selected_captain = request.POST.get('selectedCaptain')
        selected_ship = (request.POST.get('selectedShip')).title()

        captain_card = CaptainCard.objects.get(captain=selected_captain)
        home_port = (captain_card.home_port).title()
        starting_location = ShipsLocalisations.objects.get(game_number=game)
        player_captain = PlayersCaptainsCards.objects.get(game_number=game)
        player_ship = PlayersShipsCards.objects.get(game_number=game)
        player_hit_locations = TrackPlayerHitLocations.objects.get(game_number=game, player_colour=player_colour.lower())
        # update player hit locations track in db

        if player_colour == 'blue':
            player_captain.change_captain(player_colour, selected_captain)
            player_ship.change_ship_unit(player_colour, selected_ship)
            if not game.player_blue_play:
                game.player_blue_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'green':
            player_captain.change_captain(player_colour, selected_captain)
            player_ship.change_ship_unit(player_colour, selected_ship)
            if not game.player_green_play:
                game.player_green_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'red':
            player_captain.change_captain(player_colour, selected_captain)
            player_ship.change_ship_unit(player_colour, selected_ship)
            if not game.player_red_play:
                game.player_red_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'yellow':
            player_captain.change_captain(player_colour, selected_captain)
            player_ship.change_ship_unit(player_colour, selected_ship)
            if not game.player_yellow_play:
                game.player_yellow_play = True
                game.amount_players += 1
                game.save()

        setattr(starting_location, f"{player_colour}_ship", home_port)
        setattr(starting_location, f"{player_colour}_in_port", True)
        starting_location.save()

        for location in HIT_LOCATIONS:
            player_hit_locations.set_location_value(player_colour, location)

    data['amountPlayers'] = game.amount_players

    return JsonResponse(data)
