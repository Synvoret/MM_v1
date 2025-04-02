async function startRound(roundRecord) {

    await declarationSide(roundRecord, 'aggressor');
    await statBoard(roundRecord, 'aggressor');
    await createP(roundRecord, roundRecord.aggressor.declaration);
    await declarationSide(roundRecord, 'defender');
    await statBoard(roundRecord, 'defender');
    await createP(roundRecord, roundRecord.defender.declaration);

};