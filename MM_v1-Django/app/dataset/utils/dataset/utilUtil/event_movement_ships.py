from django.db.models import Max, F
from board.models import SeaZone


def event_movement_ships(event: object = None, ships_localisations_object: object = None, ships_type: object = None) -> dict:
    """
    Function returns all ship movements from the current event.
    
    event: Event Card object.
    ships_localisations_object: Ships Localisations object.
    ship_type: Stack Events NPC Captains.
    """

    # GET MOVING DIRECTIONs for EACH SHIP

    moving_ships = {}

    event_directions = (
        'dutch_direction',
        'english_direction',
        'french_direction',
        'spanish_direction',
        'large_pirate_direction',
        'small_pirate_direction',
        )

    nationalities = [
        'Dutch', 
        'English', 
        'French', 
        'Spanish', 
        'Large Pirate', 
        'Small Pirate'
        ]

    # get each direction from dict event_directions in event card
    for event_direction in event_directions:
        # get nationality of shiw wich one will be moving
        nationality = event_direction.replace('_direction', '').title().replace('_', ' ')
        # check event direction exist in event card
        if getattr(event, event_direction):
            direction = getattr(event, event_direction).lower() + '_direction'
            ship_position = getattr(ships_localisations_object, event_direction.replace('_direction', '_ship'))
            # check exist ship to this event direction
            if ship_position: # if ship exist
                # actualization position in db for moved ship
                ship_destination = getattr(SeaZone.objects.get(sea_zone_name=ship_position), direction)
                # check destination for ship, 
                if ship_destination: # if destination exist
                    setattr(ships_localisations_object, event_direction.replace('_direction', '_ship'), str(ship_destination))
                    ships_localisations_object.save()
                    # update moving_ships
                    # check unit ship for ship from stack npc captains event cards
                    # ships_type = ships_type.order_by('-game_round')
                    lasted_ship_for_nationality_captain = list(ships_type.filter(nationality=nationality).order_by('-game_round'))
                    unit = (lasted_ship_for_nationality_captain[0].ship).lower() # ship, ex. 'Frigate'
                    moving_ships["ship" + nationality.replace(" ", "")] = unit
                    print("ship" + nationality.replace(" ", ""))
                    movement = event_direction.replace('_direction', '_movement') # 'x_movement'
                    moving_ships[movement] = ship_destination.lower().replace(' ', '-')
                else:
                    # if doesn't exist destination
                    pass

    return moving_ships
