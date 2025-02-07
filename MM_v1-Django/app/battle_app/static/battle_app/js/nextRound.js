function nextRound(parsedBattleLog) {

    battleLocalStorage(issue='update', key='declarations', value=false, side="player");
    battleLocalStorage(issue='update', key='declarations', value=false, side="npc");
    battleLocalStorage(issue='update', key='player', value=[], side="seamanship_result");
    battleLocalStorage(issue='update', key='npc', value=[], side="seamanship_result");

    return true;

};
