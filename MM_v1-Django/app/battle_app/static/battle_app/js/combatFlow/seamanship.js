async function seamanship(roundRecord) {
    await createP(roundRecord, 'Seamanship test');
    await dices(roundRecord, 'aggressor', 'seamanship', roundRecord.aggressor.seamanship);
    await dices(roundRecord, 'defender', 'seamanship', roundRecord.defender.seamanship);
}
