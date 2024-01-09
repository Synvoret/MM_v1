// PLAYER HIT LOCATIONs, PUT CUBEs
function updatePlayerHitLocation(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-hit-location-image').setAttribute('href', response.cubeImage);
            let hull = response.hullHit;
            let cargo = response.cargoHit;
            let masts = response.mastsHit;
            let crew = response.crewHit;
            let cannons = response.cannonsHit;
            document.getElementById('hull-' + hull + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('cargo-' + cargo + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('masts-' + masts + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('crew-' + crew + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('cannons-' + cannons + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
        }
    };
    xhr.open('GET', 'playerHitLocation?colour=' + colour, true);
    xhr.send();
};
