// DRAW ONE EVENT CARD
function drawEventCard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            console.log(response);
            if (response.npcCaptainNationality !== undefined) {
                // if event is a CAPTAIN

                // captain card
                const eventCaptainCardIDImage = `event-${response.npcCaptainNationality}-captain-image`;
                document.getElementById(eventCaptainCardIDImage).setAttribute('href', response.npcCaptainImage);

                // ship plastic for captain
                let ship = response.npcCaptainShip.toLowerCase();
                let colour = response.npcCaptainNationality
                let localisation = response.npcCaptainSeaZoneStart

                putShipPlastic(ship, colour, localisation, false)

            };
            
            const eventCardIDImage = "event-image";
            document.getElementById(eventCardIDImage).setAttribute('href', response.eventCardImage);

            if (response.moving !== undefined) {
                // if event has a moving NPC ships

                if (response.dutch_movement !== undefined) {
                    // lok = 'old-providence'
                    putShipPlastic(response.shipDutch, 'dutch', response.dutch_movement, false)
                };
                if (response.english_movement !== undefined) {
                    // lok = 'old-providence'
                    putShipPlastic(response.shipEnglish, 'english', response.english_movement, false)
                };
                if (response.french_movement !== undefined) {
                    // lok = 'santo-domingo'
                    putShipPlastic(response.shipFrench, 'french', response.french_movement, false)
                };
                if (response.spanish_movement !== undefined) {
                    // lok = 'santo-domingo'
                    putShipPlastic(response.shipSpanish, 'spanish', response.spanish_movement, false)
                };
                if (response.large_pirate_movement !== undefined) {
                    // lok = 'santo-domingo'
                    putShipPlastic(response.shipLargePirate, 'large-pirate', response.large_pirate_movement, false)
                };
                if (response.small_pirate_movement !== undefined) {
                    // lok = 'santo-domingo'
                    putShipPlastic(response.shipSmallPirate, 'small-pirate', response.small_pirate_movement, false)
                };

            };

            if (response.function1) {
                window[response.function1](response.arg1)

            };
            
        }
    };
    xhr.open('GET', 'drawEventCard', true);
    xhr.send();
};
