from board.models import SeaZone


def movement_directions(event: object = None, ships_localisations_object: object = None) -> dict:
    """
    Function returns all ship movements from the current event.
    
    event: Event Card object.
    ships_localisations_object: Ships Localisations object.
    """

    move_directions = {
        'dutch_direction': None,
        'english_direction': None,
        'french_direction': None,
        'spanish_direction': None,
        'large_pirate_direction': None,
        'small_pirate_direction': None,
    }
    for direction in move_directions.keys():
        move_directions[direction] = getattr(event, direction)
    # print(move_directions)

    ships_localisations = {
        'blue_ship': None,
        'green_ship': None,
        'red_ship': None,
        'yellow_ship': None,

        'dutch_ship': None,
        'english_ship': None,
        'french_ship': None,
        'spanish_ship': None,

        'small_pirate_ship': None,
        'large_pirate_ship': None,
    }
    for ship_localisation in ships_localisations.keys():
        ships_localisations[ship_localisation] = getattr(ships_localisations_object, ship_localisation)
    print(ships_localisations)




























    # # STARE
    # event_card = EventCard.objects.get(card=event.card)
    # print("jestem w movement_directions", "++++++++++++++++++++++++++++++++")
    # ships_localisations = ShipsLocalisations.objects.get(pk=3)

    # # sea_zones = SeaZone.objects.all()

    # # print(sea_zones.)

    # unit_movements = {}

    # units = (
    #     'dutch_direction',
    #     'english_direction',
    #     'french_direction',
    #     'spanish_direction',
    #     'large_pirate_direction',
    #     'small_pirate_direction',
    #     )

    # for unit in units:
    #     unit_movements[unit] = getattr(event_card, unit)

    # print(unit_movements)

    # return unit_movements
