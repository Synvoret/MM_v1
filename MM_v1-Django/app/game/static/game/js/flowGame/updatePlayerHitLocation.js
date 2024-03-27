// PLAYER HIT LOCATIONs, PUT CUBEs
function updatePlayerHitLocation(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            // console.log(response)
            document.getElementById('player-hit-location-image').setAttribute('href', response.cubeImage);
            let hull = response.hullHit;
            let cargo = response.cargoHit;
            let masts = response.mastsHit;
            let crew = response.crewHit;
            let cannons = response.cannonsHit;

            // cleanning cubes
            document.querySelectorAll('.player-board-hit-location').forEach(function(element) {
                element.setAttribute('href', '');
            });

            maxValues(colour);

            if (hull !== 0) {
                document.getElementById('hull-' + hull + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            };
            if (cargo !== 0) {
                document.getElementById('cargo-' + cargo + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            };
            if (masts !== 0) {
                document.getElementById('masts-' + masts + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            };
            if (crew !== 0) {
                document.getElementById('crew-' + crew + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            };
            if (cannons !== 0) {
                document.getElementById('cannons-' + cannons + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            };

        };
    };
    xhr.open('GET', 'playerHitLocation?colour=' + colour, true);
    xhr.send();
};
