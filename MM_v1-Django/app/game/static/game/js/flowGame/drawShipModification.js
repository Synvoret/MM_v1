// DRAW RANDOMLY SHIP MODIFICATION TOKEN
async function drawShipModification(port) {
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
                    await drawShipModification(seaZone);
                }
            }
        } else {
            const shipModificationImageID = `ship-modification-${port}-image`;
            const url = `drawShipModification?port=${port}`;
            
            const fetchResponse = await fetch(url, {
                method: 'GET',
            });

            response = await fetchResponse.json();
            document.getElementById(shipModificationImageID).setAttribute('href', response.shipModificationImage);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
};
