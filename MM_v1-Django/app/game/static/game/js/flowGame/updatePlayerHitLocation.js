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
            if (hull > 0) {
                document.getElementById('hull-' + hull + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
                hull += 1;
                document.getElementById('hull-' + hull + '-player-hit-location').setAttribute('href', '');
            } else {
                document.getElementById('hull-1-player-hit-location').setAttribute('href', '');
            };
            if (cargo > 0) {
                document.getElementById('cargo-' + cargo + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
                cargo += 1;
                document.getElementById('cargo-' + cargo + '-player-hit-location').setAttribute('href', '');
            } else {
                document.getElementById('cargo-1-player-hit-location').setAttribute('href', '');
            };
            if (masts > 0) {
                document.getElementById('masts-' + masts + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
                masts += 1;
                document.getElementById('masts-' + masts + '-player-hit-location').setAttribute('href', '');
            } else {
                document.getElementById('masts-1-player-hit-location').setAttribute('href', '');
            };
            if (crew > 0) {
                document.getElementById('crew-' + crew + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
                crew += 1;
                document.getElementById('crew-' + crew + '-player-hit-location').setAttribute('href', '');
            } else {
                document.getElementById('crew-1-player-hit-location').setAttribute('href', '');
            };
            if (cannons > 0) {
                document.getElementById('cannons-' + cannons + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
                cannons += 1;
                document.getElementById('cannons-' + cannons + '-player-hit-location').setAttribute('href', '');
            } else {
                document.getElementById('cannons-1-player-hit-location').setAttribute('href', '');
            };
        }
    };
    xhr.open('GET', 'playerHitLocation?colour=' + colour, true);
    xhr.send();
};
