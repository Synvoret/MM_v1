function playerBoard() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-board').setAttribute('href', response.playerBoardImage);

            let colour = response.playerColour;
            resetPlayerBoard();
            updateLoyalityTrack(colour);
            updateFavorsTrack(colour);
            updatePlayerHitLocation(colour);
            updatePlayerGolds(colour);
            drawPlayerCaptainCard(colour);
            drawPlayerShipCard(colour);
            updateCaptainActions(colour);
            };
        };
    xhr.open('GET', 'playerBoard', true);
    xhr.send();

};




