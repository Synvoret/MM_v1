// updateLocalStorage function
function battleLocalStorage(issue, key, value, side) {

    const parsedBattleLog = JSON.parse(localStorage.getItem('battleLog'));

    if (issue === 'create') {

        localStorage.setItem('battleLog', JSON.stringify(START_PLAYERvNPC_BATTLE_SETTINGS));

    } else if (issue === 'get') {

        return parsedBattleLog[key];

    } else if (issue === 'update') {

        if (key === 'round') {

            parsedBattleLog[key] = value;

        } else if (key === 'declarations') {

            parsedBattleLog[key][side] = value;

        } else if (key === 'Player' || key === 'NPC') {

            parsedBattleLog[key][side] = value;

        };

        localStorage.setItem('battleLog', JSON.stringify(parsedBattleLog));

    };

};