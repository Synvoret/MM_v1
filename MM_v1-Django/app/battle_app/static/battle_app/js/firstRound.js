function firstRound(roundNumber, aggressor, defender) {

    battleLocalStorage(issue='update', key='round', value=roundNumber+1, side=null);
    declarationSide(roundNumber, aggressor);
    createP(roundNumber, 'Shoot');
    battleLocalStorage(issue='update', key='declarations', value=true, side=aggressor);
    declarationSide(roundNumber, defender);
    createP(roundNumber, 'Shoot');
    battleLocalStorage(issue='update', key='declarations', value=true, side=defender);

};
