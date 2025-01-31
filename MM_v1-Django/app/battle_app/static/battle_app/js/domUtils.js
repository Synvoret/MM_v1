// initialization of statistics for equipment
function sideStats() {

};


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

        } else if (key === 'player' || key === 'npc') {

            parsedBattleLog[key][side] = value;

        };

        localStorage.setItem('battleLog', JSON.stringify(parsedBattleLog));

    };

};


// roundcounter function and displaying this
function roundCounter(roundNumber){

    const roundCounter = document.createElement('h5');
    roundCounter.className = 'roundCounter';
    roundCounter.textContent = `Round: >> ${roundNumber} <<`;
    document.getElementById('battle-logs').appendChild(roundCounter);

};


// 
function declarationSide(side) {
    const declaration = document.createElement('p');
    declaration.className = 'declaration';
    declaration.textContent = `Declaration: ${side}`;
    document.getElementById('battle-logs').appendChild(declaration);
};


// function responsible for creating ACTION buttons in row
function createActionButton(action, side) {
    let actionButtons = document.querySelector('.actionButtons');
    if (!actionButtons) {
        actionButtons = document.createElement('span');
        actionButtons.className = 'actionButtons';
        document.getElementById('battle-logs').appendChild(actionButtons);
    };
    // create button
    const element = document.createElement('button');
    element.className = `Button${action}`;
    element.textContent = action;

    element.addEventListener('click', function() {
        this.parentElement.remove();
        createP(action);
        battleLocalStorage(issue='update', key='declarations', value=true, side=side);
        playerAttackNPC();
    });

    actionButtons.appendChild(element);
};


// function responsible for displaying content
function createP(content) {
    const element = document.createElement('p');
    element.className = `description`;
    element.textContent = content;
    document.getElementById('battle-logs').appendChild(element);
};


function nextRound(parsedBattleLog) {

    battleLocalStorage(issue='update', key='declarations', value=false, side="player");
    battleLocalStorage(issue='update', key='declarations', value=false, side="npc");
    battleLocalStorage(issue='update', key='player', value=[], side="seamanship_result");
    battleLocalStorage(issue='update', key='npc', value=[], side="seamanship_result");

    return true;

};


function battleDiceRoll(amount, side) {
    let side_upper = side.toUpperCase();
    battleLocalStorage(issue='update', key=side_upper, value=[1, 2, 3, 4], side='seamanship_result');
    createP(`Rolling Seamanship ${amount}`);
};