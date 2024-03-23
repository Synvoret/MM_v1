ALLOWEDDESTINATIONS= [
    'Basse-Terre',
    'Bridgetown',
    'Caracas',
    'Cartagena',
    'Curacao',
    'Gulf City',
    'Havana',
    'Nassau',
    'Old Providence',
    'Petite Goave',
    'Port Royal',
    'San Juan',
    'Santo Domingo',
    'St John',
    'St Maarten',
    'The Caribbean Sea',
    'Tortuga',
    'Trinidad',
]

BOUNTIES = [
    'Dutch',
    'English',
    'French',
    'Spanish',
    'Small Pirate',
    'Large Pirate',
]

CARGO = [
    ('Cocoa', 'Cocoa'),
    ('Food', 'Food'),
    ('Rum', 'Rum'),
    ('Spices', 'Spices'),
    ('Sugar', 'Sugar'),
    ('Tobacco', 'Tobacco'),
    ('Textiles', 'Textiles'),
    ('Wood', 'Wood'),
]

COLOUR = [
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Dutch', 'Dutch'),
    ('English', 'English'),
    ('French', 'French'),
    ('Green', 'Green'),
    ('Large Pirate', 'Large Pirate'),
    ('Pirate', 'Pirate'),
    ('Red', 'Red'),
    ('Small Pirate', 'Small Pirate'),
    ('Spanish', 'Spanish'),
    ('Yellow', 'Yellow'),
    ('Treasure', 'Treasure'),
]

DESTINATION_PORT = [
    ('Basse-Terre', 'Basse-Terre'),
    ('Bridgetown', 'Bridgetown'),
    ('Caracas', 'Caracas'),
    ('Cartagena', 'Cartagena'),
    ('Curacao', 'Curacao'),
    ('Gulf City', 'Gulf City'),
    ('Havana', 'Havana'),
    ('Nassau', 'Nassau'),
    ('Old Providence', 'Old Providence'),
    ('Petite Goave', 'Petite Goave'),
    ('Port Royal', 'Port Royal'),
    ('San Juan', 'San Juan'),
    ('Santo Domingo', 'Santo Domingo'),
    ('St John', 'St John'),
    ('St Maarten', 'St Maarten'),
    ('The Caribbean Sea', 'The Caribbean Sea'),
    ('Tortuga', 'Tortuga'),
    ('Trinidad', 'Trinidad'),
]

DIRECTION = [
    ('N', 'North'),
    ('NE', 'Northeast'),
    ('E', 'East'),
    ('SE', 'Southeast'),
    ('S', 'South'),
    ('SW', 'Southwest'),
    ('W', 'West'),
    ('NW', 'Northwest'),
]

DISPOSABLE_ACTIONS = [
    'sellGoods', # after sell goods in port, always as first action in port
    'buyGoods', # after buy goods in port
    'raiseLoyality', # after raise loyality track
    'getFavour', # after get favour in port, always as last action in port
]

HITS = [
    ('Hull', 'Hull'),
    ('Cargo', 'Cargo'),
    ('Masts', 'Masts'),
    ('Crew', 'Crew'),
    ('Cannons', 'Cannons'),
    ('Escape', 'Escape'),
]

HIT_LOCATIONS = [
    'hull', 
    'cargo', 
    'masts', 
    'crew',
    'cannons',
]

EXPANSION = [
    ('Seas of Glory', 'Seas of Glory'),
    ('Colors of War', 'Colors of War'),
]

LOYALITY = [
    ('Fierce Loyality', 'Fierce Loyality'),
    ('Happy', 'Happy'),
    ('Pleased', 'Pleased'),
    ('Content', 'Content'),
    ('Restless', 'Restless'),
    ('Unhappy', 'Unhappy'),
    ('Angry', 'Angry'),
    ('Mutiny', 'Mutiny'),
]

LOYALITIES = [
    'Fierce Loyality',
    'Happy',
    'Pleased',
    'Content',
    'Restless',
    'Unhappy',
    'Angry',
    'Mutiny',
]

NATIONALITY = [
    ('Dutch', 'Dutch'),
    ('French', 'French'),
    ('English', 'English'),
    ('Spanish', 'Spanish'),
]

PLAYER_COLOURS = [
    ('blue', 'blue'),
    ('green', 'green'),
    ('red', 'red'),
    ('yellow', 'yellow'),
]

PORT = [
    ('Basse-Terre', 'Basse-Terre'),
    ('Bridgetown', 'Bridgetown'),
    ('Caracas', 'Caracas'),
    ('Cartagena', 'Cartagena'),
    ('Curacao', 'Curacao'),
    ('Havana', 'Havana'),
    ('Nassau', 'Nassau'),
    ('Old Providence', 'Old Providence'),
    ('Petite Goave', 'Petite Goave'),
    ('Port Royal', 'Port Royal'),
    ('San Juan', 'San Juan'),
    ('Santo Domingo', 'Santo Domingo'),
    ('St John', 'St John'),
    ('St Maarten', 'St Maarten'),
    ('Tortuga', 'Tortuga'),
    ('Trinidad', 'Trinidad'),
]

SEAZONES = [
    ('Basse-Terre', 'Basse-Terre'),
    ('Bridgetown', 'Bridgetown'),
    ('Caracas', 'Caracas'),
    ('Cartagena', 'Cartagena'),
    ('Curacao', 'Curacao'),
    ('Gulf City', 'Gulf City'),
    ('Havana', 'Havana'),
    ('Nassau', 'Nassau'),
    ('Old Providence', 'Old Providence'),
    ('Petite Goave', 'Petite Goave'),
    ('Port Royal', 'Port Royal'),
    ('San Juan', 'San Juan'),
    ('Santo Domingo', 'Santo Domingo'),
    ('St John', 'St John'),
    ('St Maarten', 'St Maarten'),
    ('The Caribbean Sea', 'The Caribbean Sea'),
    ('Tortuga', 'Tortuga'),
    ('Trinidad', 'Trinidad'),
]

SHIPS = [
    ('Brig', 'Brig'),
    ('Flute', 'Flute'),
    ('Frigate', 'Frigate'),
    ('Galleon', 'Galleon'),
    ('Man-o-War', 'Man-o-War'),
    ('Sloop', 'Sloop'),
]

SHIPSLOCALIZATIONS = [
    'blue_ship',
    'blue_in_port',
    'green_ship',
    'green_in_port',
    'red_ship',
    'red_in_port',
    'yellow_ship',
    'yellow_in_port',
    'merchants_ship',
    'dutch_ship',
    'english_ship',
    'french_ship',
    'spanish_ship',
    'small_pirate_ship',
    'large_pirate_ship',
]

SKILL = [
    ('Scouting', 'Scouting'),
    ('Influence', 'Influence'),
]

SPECIALWEAPONS = [
    'Chain Shot',
    'Grapeshot',
    'Grappling Hooks',
    'Double Shot',
    'Caltrops',
    'Heated Shot',
    'Grenade',
    'Premium Rum',
    'Explosive Shell',
]

# def choices(cls):
#     """
#     Decorator for adding choices to a class.

#     CARGO, DESTINATION_PORT, EXPANSION, HITS, SEAZONES
#     """

#     cls.CARGO = CARGO
#     cls.DESTINATION_PORT = DESTINATION_PORT
#     cls.EXPANSION = EXPANSION
#     cls.HITS = HITS
#     cls.LOYALITY = LOYALITY
#     cls.PORT = PORT
#     cls.SEAZONES = SEAZONES
#     cls.SHIPS = SHIPS
#     cls.SKILL = SKILL

#     return cls




def choices(cls):
    class NewModel(cls):
        CARGO = CARGO
        COLOUR = COLOUR
        DESTINATION_PORT = DESTINATION_PORT
        DIRECTION = DIRECTION
        EXPANSION = EXPANSION
        HITS = HITS
        LOYALITY = LOYALITY
        NATIONALITY = NATIONALITY
        PLAYER_COLOURS = PLAYER_COLOURS
        SEAZONES = SEAZONES
        SHIPS = SHIPS
        SKILL = SKILL

        class Meta:
            proxy = True

    return NewModel
