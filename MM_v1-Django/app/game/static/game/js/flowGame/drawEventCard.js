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

            if (response.function1) {
                window[response.function1](response.arg1)

            };
            
        }
    };
    xhr.open('GET', 'drawEventCard', true);
    xhr.send();
};
