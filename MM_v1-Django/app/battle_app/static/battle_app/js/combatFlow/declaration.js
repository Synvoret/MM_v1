async function declaration(roundRecord, side, actions) {
    await declarationSide(roundRecord, side);
    await statBoard(roundRecord, side);
    for (act of actions) {
        await createActionButton(roundRecord, act, side);
    };
}