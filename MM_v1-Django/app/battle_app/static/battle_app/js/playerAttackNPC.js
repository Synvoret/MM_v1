// function start battle between Player vs NPC (Non-Player Captain)
function playerAttackNPC() {


    // get battle-log storage from localStore
    let battleLog = localStorage.getItem('battleLog');
    if (!battleLog) {
        battleLocalStorage(issue='create');
        battleLog = localStorage.getItem('battleLog');
    };

    let player = battleLocalStorage(issue='get', key='player');
    let npc = battleLocalStorage(issue='get', key='npc');
    let round = battleLocalStorage(issue='get', key='round');
    let declerations = battleLocalStorage(issue='get', key='declarations');
    let actions = battleLocalStorage(issue='get', key='actions');

    if (!declerations.player && !declerations.npc) {
        roundCounter(round);
    };


    // IF FIRST ROUND
    if (round === 1) {

        battleLocalStorage(issue='update', key='round', value=round+1, side=null);
        declarationSide('Player');
        createP('Shoot');
        battleLocalStorage(issue='update', key='declarations', value=true, side="player");
        declarationSide('NPC');
        createP('Shoot');
        battleLocalStorage(issue='update', key='declarations', value=true, side="npc");

        // if (player.seamanship_result.length === 0) {
        //     // console.log('brak wyników rzutów kostek dla agresora');
        //     // createActionButton('Roll Seamanship', 'player');
        // } else if (npc.seamanship_result.length === 0) {
        //     // console.log('brak wyników rzutów kostek dla npca');
        //     // createActionButton('Roll Seamanship', 'npc');
        // } else {
        if (nextRound()) {
            playerAttackNPC()
        };
        // };

    // NEXT ROUNDS
    } else if (round > 1) {

        if (!declerations.player) {
            declarationSide('Player');
            for (action of actions) {
                createActionButton(action, "player");
            };
        } else if (!declerations.npc) {
            declarationSide('NPC');
            for (action of actions) {
                createActionButton(action, "npc");
            };
        } else {
            if (nextRound()) {
                battleLocalStorage(issue='update', key='round', value=round+1, side=null);
                playerAttackNPC();
            };
        };

    };

    battleAppHiddenMainList();

};
