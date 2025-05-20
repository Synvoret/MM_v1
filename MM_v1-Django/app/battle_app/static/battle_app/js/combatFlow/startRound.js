async function startRound(reason=null, endBattle=false) {

    const roundRecord = await combatFlow();

    if (endBattle) {
        document.getElementById(`round-section-${roundRecord.round}`).appendChild(await createP(`${reason}`));
        document.getElementById(`round-section-${roundRecord.round}`).appendChild(await createP(`Battle End after ${roundRecord.round} rounds`));
        return;
    } else if (reason === 'next_round') {
        // await combatFlow(req='POST', side=null, parameter=null, value=null, next_round=true);
        await seaBattle();
    }

}
