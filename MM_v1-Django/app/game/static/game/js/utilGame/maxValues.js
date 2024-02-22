// Function responsible for providing the maximum values for the player allows you to display the maximum values for: hull, cargo, masts, crew, cannons, actions,

function maxValues(colour) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            // let colour = response.playerColour
            console.log(response, colour, 'MAX VALUES')
            console.log(`captain-actions-${response.playerMaxAmountActions}`)

            document.getElementById('player-hit-location-max-value-image').setAttribute('href', response.playerCubeMaxImage);

            // max hull
            if (document.getElementById(`hull-${response.playerMaxAmountHull}-player-hit-location`).getAttribute('href') === "") {
                document.getElementById(`hull-${response.playerMaxAmountHull}-player-hit-location`).setAttribute('href', '#player-hit-location-max-value-image');
            };
            
            // max cargo
            if (document.getElementById(`cargo-${response.playerMaxAmountCargo}-player-hit-location`).getAttribute('href') === "") {
                document.getElementById(`cargo-${response.playerMaxAmountCargo}-player-hit-location`).setAttribute('href', '#player-hit-location-max-value-image');
            };

            // max masts
            if (document.getElementById(`masts-${response.playerMaxAmountMasts}-player-hit-location`).getAttribute('href') === "") {
                document.getElementById(`masts-${response.playerMaxAmountMasts}-player-hit-location`).setAttribute('href', '#player-hit-location-max-value-image');
            };

            // max crew
            if (document.getElementById(`crew-${response.playerMaxAmountCrew}-player-hit-location`).getAttribute('href') === "") {
                document.getElementById(`crew-${response.playerMaxAmountCrew}-player-hit-location`).setAttribute('href', '#player-hit-location-max-value-image');
            };

            // max cannons
            if (document.getElementById(`cannons-${response.playerMaxAmountCannons}-player-hit-location`).getAttribute('href') === "") {
                document.getElementById(`cannons-${response.playerMaxAmountCannons}-player-hit-location`).setAttribute('href', '#player-hit-location-max-value-image');
            };

            // max actions
            document.getElementById('captain-max-value-actions-image').setAttribute('href', response.playerCubeMaxImage);
            document.getElementById(`captain-actions-${response.playerMaxAmountActions}`).setAttribute('href', '#captain-max-value-actions-image');
        };
        
    };
    xhr.open('GET', 'maxValues', true);
    xhr.send();
};
