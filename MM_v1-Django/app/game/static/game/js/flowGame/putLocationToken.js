// PUT LOCATION TOKENs
async function putLocationToken(seaZone) {
    try {
        let response;

        if (seaZone === "all") {
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
                    await putLocationToken(seaZone);
                }
            }
        } else {
            const locationTokenIDImage = `location-token-${seaZone}-image`;
            const url = `putLocationToken?seaZone=${seaZone}`;
            
            const fetchResponse = await fetch(url, {
                method: 'GET',
            });

            response = await fetchResponse.json();
            document.getElementById(locationTokenIDImage).setAttribute('href', response.locationTokenImage);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
};
