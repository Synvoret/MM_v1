import random
from django.http import JsonResponse

from dataset.models import EventCard
from dataset.utils.dataset import events
from dataset.utils.dataset.utilUtil import event_movement_ships
from game.models import Game
from game.models import ShipsLocalisations
from game.models import StackEventsCards
from game.models import StackEventsNPCCaptains


def drawEventCard(request):
    """Endpoint return a draw new Event Card."""

    # EMPTY DATA DICT FOR ALL EVENTs UTILs.
    data = {}
    game = Game.objects.get(number=100)

    # CHECK LAST EVENT CARD, IF CAPTAIN, THEN MOVE CARD TO CURRENT NATIONALITY STACK
    if StackEventsCards.objects.exists():
        previous_turn_event_card = StackEventsCards.objects.get(game_round=game.rounds)
        if previous_turn_event_card.event_card_captain == True:
            captain_name = StackEventsNPCCaptains.objects.create(
                game_number=game,
                game_round=game.rounds,
                captain=previous_turn_event_card.event_card,  # instance of EventCard
                nationality=previous_turn_event_card.event_card.nationality,
                ship=previous_turn_event_card.event_card.ship
                )
            data["npcCaptainNationality"] = (captain_name.captain.nationality).lower().replace(" ", "-")
            data["npcCaptainSeaZoneStart"] = captain_name.captain.sea_zone_start.lower().replace(" ", "-")
            data["npcCaptainShip"] = captain_name.captain.ship
            data["npcCaptainImage"] = captain_name.captain.awers.url
            nat = f"{captain_name.captain.nationality}_ship".lower().replace(' ', '_')
            ShipsLocalisations.objects.update(**{nat: captain_name.captain.sea_zone_start})

    # DRAW NEW EVENT CARD
    cards = EventCard.objects.all()
    random_card = random.choice(cards)

    # MOVING NPC SHIPs if EXIST
    if random_card.moving:
        if StackEventsNPCCaptains.objects.exists():
            data['moving'] = True
            ships_localisations_object = ShipsLocalisations.objects.get(game_number=game)
            ships_type = StackEventsNPCCaptains.objects.all()
            movement_ships = event_movement_ships(random_card, ships_localisations_object, ships_type)
            data.update(movement_ships)

    # UPDATE GAME ROUND
    game.increment_rounds() # NIESTETY NIE DZIAŁA, CZASAMI POWTARZA ZAPIS
    # try:
    #     request.session['rounds'] += 1
    # except:


    data['rounds'] = game.rounds
    data["eventCardImage"] = random_card.awers.url

    # SPECIAL ACTIONs/FUNCTIONs FOR NEW EVENT CARD
    try:
        # trying all event utils, if exist, then run it
        event_util = getattr(events, random_card.card.lower().replace(" ", "_"))(random_card)
        data.update(event_util)
    except:
        pass

    # UPDATE ALL EVENTs STACKs CARDs
    if random_card.npc_name is not None:
        event_card_captain = True
    else:
        event_card_captain = False
    game_round = game.rounds
    StackEventsCards.objects.create(
        game_number=game, 
        game_round=game_round, 
        event_card=random_card,
        event_card_captain=event_card_captain,
        )

    return JsonResponse(data)
