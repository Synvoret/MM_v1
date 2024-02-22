// PUT CUBEs on TRACK ENEMY HIT LOCATIONs
function updateEnemyHitLocation() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('brown-cube-enemy-hit-location-image').setAttribute('href', response.cubeImage);
            let hull = response.hullHit;
            let cargo = response.cargoHit;
            let masts = response.mastsHit;
            let crew = response.crewHit;
            let cannons = response.cannonsHit;
            document.getElementById('hull-' + hull + '-enemy-hit-location').setAttribute('href', '#brown-cube-enemy-hit-location-image');
            document.getElementById('cargo-' + cargo + '-enemy-hit-location').setAttribute('href', '#brown-cube-enemy-hit-location-image');
            document.getElementById('masts-' + masts + '-enemy-hit-location').setAttribute('href', '#brown-cube-enemy-hit-location-image');
            document.getElementById('crew-' + crew + '-enemy-hit-location').setAttribute('href', '#brown-cube-enemy-hit-location-image');
            document.getElementById('cannons-' + cannons + '-enemy-hit-location').setAttribute('href', '#brown-cube-enemy-hit-location-image');
        }
    };
    xhr.open('GET', "enemyHitLocation", true);
    xhr.send();
};
