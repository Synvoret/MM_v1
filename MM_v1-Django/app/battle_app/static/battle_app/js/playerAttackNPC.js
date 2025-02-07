// function start battle between Player vs NPC (Non-Player Captain)
function playerAttackNPC() {


    // get battle-log storage from localStore
    let battleLog = localStorage.getItem('battleLog');
    if (!battleLog) {
        battleLocalStorage(issue='create');
        battleLog = localStorage.getItem('battleLog');
    };

    let player = battleLocalStorage(issue='get', key='Player');
    let npc = battleLocalStorage(issue='get', key='NPC');
    let round = battleLocalStorage(issue='get', key='round');
    let declerations = battleLocalStorage(issue='get', key='declarations');
    let actions = battleLocalStorage(issue='get', key='actions');

    if (!declerations.player && !declerations.npc) {
        roundSection(round);
        roundCounter(round);
    };


    // IF FIRST ROUND
    if (round === 1) {

        firstRound(round, 'Player', 'NPC');

        // dices for Seamanship
        createP(round, 'Roll Seamanship');
        battleDiceRoll(round, 'seamanship', 'Player');
        battleDiceRoll(round, 'seamanship', 'NPC');

        // if (nextRound()) {
        //     playerAttackNPC()
        // };


    // NEXT ROUNDS
    } else if (round > 1) {

        console.log(`next rounds ${round}`);

        // if (!declerations.player) {
        //     declarationSide('Player');
        //     for (action of actions) {
        //         createActionButton(action, "Player");
        //     };
        // } else if (!declerations.npc) {
        //     declarationSide('NPC');
        //     for (action of actions) {
        //         createActionButton(action, "NPC");
        //     };
        // } else {
        //     if (nextRound()) {
        //         battleLocalStorage(issue='update', key='round', value=round+1, side=null);
        //         playerAttackNPC();
        //     };
        // };

    };

    battleAppHiddenMainList();

};
