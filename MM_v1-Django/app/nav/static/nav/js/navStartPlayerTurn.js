// navStartPlayerTurn function

// WHEN: after click DrawEventCard
function navStartPlayerTurn() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            let colour = response.playerColour;

            document.querySelector('.nav-actions-buttons').style.display = '';
            if (response.playerInPort) {
                document.querySelector('.nav-button.nav-button-move-ship').disabled = false;
                document.querySelector('.nav-button.nav-button-scout').disabled = true;
                document.querySelector('.nav-button.nav-button-port').disabled = false;
                document.querySelector('.nav-button.nav-button-fishing').disabled = true;
                document.querySelector('.nav-button.nav-button-location').disabled = true;
            } else {
                document.querySelector('.nav-button.nav-button-move-ship').disabled = false;
                document.querySelector('.nav-button.nav-button-scout').disabled = false;
                document.querySelector('.nav-button.nav-button-port').disabled = true;
                if (response.playerHaveDestroyedHitLocation) {
                    document.querySelector('.nav-button.nav-button-fishing').disabled = true;
                } else {
                    document.querySelector('.nav-button.nav-button-fishing').disabled = false;
                };
                if (response.isInTheCaribbeanSea){
                    document.querySelector('.nav-button.nav-button-location').disabled = true;
                } else {
                    document.querySelector('.nav-button.nav-button-location').disabled = false;
                };
            };

            document.getElementById('nav-draw-event-card-div').style.display = 'none';
            document.getElementById('nav-player-action-div').style.display = 'block';
            // RANDOMLY first player in round
            document.querySelector(`.nav-title-value-player-${colour}`).innerHTML = 'ACTIVE';
        };
        
    };
    xhr.open('GET', 'navStartPlayerTurn', true);
    xhr.send();

};
