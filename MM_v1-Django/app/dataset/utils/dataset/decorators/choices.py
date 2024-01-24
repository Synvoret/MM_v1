CARGO = [
    ('Cacao', 'Cacao'),
    ('Food', 'Food'),
    ('Rum', 'Rum'),
    ('Spieces', 'Spieces'),
    ('Sugar', 'Sugar'),
    ('Tabacco', 'Tabacco'),
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
    ('The Carribean Sea', 'The Carribean Sea'),
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

HITS = [
    ('Hull', 'Hull'),
    ('Cargo', 'Cargo'),
    ('Masts', 'Masts'),
    ('Crew', 'Crew'),
    ('Cannons', 'Cannons'),
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

NATIONALITY = [
    ('DU', 'Dutch'),
    ('FR', 'French'),
    ('EN', 'English'),
    ('SP', 'Spanich'),
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
    ('st John', 'st John'),
    ('st Maarten', 'st Maarten'),
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
    ('The Carribean Sea', 'The Carribean Sea'),
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

SKILL = [
    ('Scouting', 'Scouting'),
    ('Influence', 'Influence'),
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
        SKILL = [
            ('Scouting', 'Scouting'),
            ('Influence', 'Influence'),
        ]

        class Meta:
            proxy = True

    return NewModel
