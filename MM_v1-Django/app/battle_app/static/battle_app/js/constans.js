// battle PlayerVnpc initial settings
const START_PLAYERvNPC_BATTLE_SETTINGS = {
    'actions': ['Shoot', 'Board', 'Flee'],
    'player': {
        'seamanship': 3, // amount dices
        'seamanship_result': [], // result of dices
        'ship': 'sloop', 
    },
    'npc': {
        'seamanship': 6, // amount dices
        'seamanship_result': [], // result of dices
        'ship': 'sloop', 
    },
    'declarations': {'player': false, 'npc': false},
    'round': 1,
    'sides': ['Player', 'NPC', 'Location', 'Fort'],
};
