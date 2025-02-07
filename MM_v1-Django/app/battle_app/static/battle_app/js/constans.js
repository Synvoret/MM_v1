// battle PlayerVnpc initial settings
const START_PLAYERvNPC_BATTLE_SETTINGS = {
    'actions': ['Shoot', 'Board', 'Flee'],
    'Player': {
        'seamanship': 4, // amount dices
        'seamanship_result': [], // result of dices
        'ship': 'sloop', 
    },
    'NPC': {
        'seamanship': 6, // amount dices
        'seamanship_result': [], // result of dices
        'ship': 'sloop', 
    },
    'declarations': {'player': false, 'npc': false},
    'round': 1,
    'sides': ['Player', 'NPC'],
};
