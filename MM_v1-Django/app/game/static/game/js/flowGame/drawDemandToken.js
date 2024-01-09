// DRAW RANDOMLY DEMAND TOKEN
async function drawDemandToken(port) {
    try {
        let response;

        if (port === "all") {
            const seaZonesList = [
                "basse-terre",
                "bridgetown",
                "caracas",
                "cartagena",
                "curacao",
                // 'gulf-city',
                "nassau",
                "havana",
                "old-providence",
                "petite-goave",
                "port-royal",
                "san-juan",
                "santo-domingo",
                "st-john",
                "st-maarten",
                "trinidad",
                "tortuga",
            ];

            for (const seaZone of seaZonesList) {
                if (seaZone !== "the-caribbean-sea") {
                    await drawDemandToken(seaZone);
                }
            }
        } else {
            const demandTokenIDImage = `demand-${port}-image`;
            const url = `drawDemandToken?port=${port}`;
            
            const fetchResponse = await fetch(url, {
                method: 'GET',
            });

            response = await fetchResponse.json();
            document.getElementById(demandTokenIDImage).setAttribute('href', response.demandTokenImage);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
};
