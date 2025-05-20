async function combatFlow(req=null, side=null, parameter=null, value=null, phase=null, next_round=false) {

    // only GET request
    if (req == 'GET' || req == null) {
        const response = await fetch (`combatFlow`, { method: "GET" });
        const data = await response.json();
        return data.roundRecord;


    // only POST request
    } else {
        const dataToSend = {
            "side": side,
            "parameter": parameter,
            'value': value,
            'phase': phase,
            'next_round': next_round,
        };
        const response = await fetch(`combatFlow`, {
            method: req,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dataToSend),
        });
        const data = await response.json();
        // console.log(data.roundRecord);


        return data.roundRecord;
    }

}
