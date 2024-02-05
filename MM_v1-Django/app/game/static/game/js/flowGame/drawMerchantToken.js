// DRAW RANDOMLY MERCHANT TOKEN
async function drawMerchantToken(seaZone) {
    try {
        let response;

        if (seaZone === "all") {
            const seaZonesList = [
                "basse-terre",
                "bridgetown",
                "caracas",
                "cartagena",
                "curacao",
                // "gulf-city",
                "nassau",
                "havana",
                "old-providence",
                "petite-goave",
                "port-royal",
                "san-juan",
                "santo-domingo",
                "st-john",
                "st-maarten",
                "the-caribbean-sea",
                "trinidad",
                "tortuga",
            ];

            for (const seaZone of seaZonesList) {
                await drawMerchantToken(seaZone)
                // if (seaZone !== "the-caribbean-sea") {
                //     await drawMerchantToken(seaZone);
                // }
            }
        } else {
            const merchantTokenIDImage = `merchant-token-${seaZone}-image`;
            const url = `drawMerchantToken?seaZone=${seaZone}`;
            
            const fetchResponse = await fetch(url, {
                method: 'GET',
            });

            response = await fetchResponse.json();
            // document.getElementById(merchantTokenIDImage).setAttribute('href', response.merchantTokenRewersImage);
            document.getElementById(merchantTokenIDImage).setAttribute('href', response.merchantTokenAwersImage);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
};
