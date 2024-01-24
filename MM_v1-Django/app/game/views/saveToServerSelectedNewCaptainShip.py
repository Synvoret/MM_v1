from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.models import CaptainCard
from dataset.models import ShipCard
from game.models import Game
from game.models import PlayersCaptainsCards, PlayersShipsCards
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
        ship_card = ShipCard.objects.get(ship=selected_ship)
        # update player hit locations track in db
        player_hit_locations = TrackPlayerHitLocations.objects.get(player_colour=player_colour.title())

        if player_colour == 'blue':
            PlayersCaptainsCards.player_blue = captain_card
            PlayersShipsCards.player_blue = ship_card
            if not game.player_blue_play:
                game.player_blue_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'green':
            PlayersCaptainsCards.player_green = captain_card
            PlayersShipsCards.player_green = ship_card
            if not game.player_green_play:
                game.player_green_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'red':
            PlayersCaptainsCards.player_red = captain_card
            PlayersShipsCards.player_red = ship_card
            if not game.player_red_play:
                game.player_red_play = True
                game.amount_players += 1
                game.save()
        if player_colour == 'yellow':
            PlayersCaptainsCards.player_yellow = captain_card
            PlayersShipsCards.player_yellow = ship_card
            if not game.player_yellow_play:
                game.player_yellow_play = True
                game.amount_players += 1
                game.save()

        player_hit_locations.hull = ship_card.toughness
        player_hit_locations.cargo = ship_card.cargo
        player_hit_locations.masts = ship_card.toughness
        player_hit_locations.crew = ship_card.crew
        player_hit_locations.cannons = ship_card.cannons
        player_hit_locations.save()

    data['amountPlayers'] = game.amount_players

    return JsonResponse(data)
