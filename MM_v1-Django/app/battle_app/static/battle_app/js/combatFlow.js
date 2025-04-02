async function combatFlow(req=null, side=null, parameter=null, value=null, next_round=false) {

    const url = `combatFlow`;
    const dataToSend = {
        "side": side,
        "parameter": parameter,
        'value': value,
        'next_round': next_round,
    };

    // only GET request
    if (req == 'GET' || req == null) {
        const response = await fetch (url, { method: "GET" });
        const data = await response.json();
        return data.roundRecord;

    // POST request
    } else if (req == 'POST') {
        // console.log(dataToSend);
        const response = await fetch(url, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dataToSend),
        });
        const data = await response.json();
    }

}
