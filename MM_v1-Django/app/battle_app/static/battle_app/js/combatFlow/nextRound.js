async function nextRound(roundRecord, reason, endBattle=false) {

    if (endBattle) {
        await createP(roundRecord, `${reason}`);
        await createP(roundRecord, `Battle End after ${roundRecord.round} rounds`);
        return;
    }

    await combatFlow(req='POST', side=null, parameter=null, value=null, next_round=true);
    await seaBattle();

    // const url = `endBattle`;
    // const dataToSend = {
        // "side": side,
        // "parameter": parameter,
        // 'value': value,
        // 'next_round': next_round,
    // };

    // if (req == 'GET' || req == null) {
    //     const response = await fetch (url, { method: "GET" });
    //     const data = await response.json();
    //     return data.roundRecord;

    // } else if (req == 'POST') {
    //     console.log(dataToSend);
    //     const response = await fetch(url, {
    //         method: "POST",
    //         headers: { 'Content-Type': 'application/json' },
    //         body: JSON.stringify(dataToSend),
    //     });
    //     const data = await response.json();
    // }
}
