// function start battle between Player vs NPC (Non-Player Captain)
function playerAttackNPC() {

    // get battle-log storage from localStore
    let battleLog = localStorage.getItem('battleLog');
    if (!battleLog) {
        localStorage.setItem('battleLog', JSON.stringify(START_BATTLE_SETTINGS));
        battleLog = localStorage.getItem('battleLog');
    };

    // parsed battleLog from localStore
    const parsedBattleLog = JSON.parse(battleLog);

    // declarations from parsed battleLog
    let declerations = parsedBattleLog.DECLARATIONS;
    // if all declarations are null, start new round
    if (!declerations.aggresor && !declerations.defender) {
        roundCounter(parsedBattleLog.ROUND);
    };

    // if (round === 1) {
    //     declarationSide("Player");
    //     createActionButton("Shoot", "Player");
    // } else {
    //     declarationSide("NPC");
    //     createActionButton("Shoot", "NPC");
    // };

    battleAppHiddenMainList();

};
