function playerBoard(colour) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-board').setAttribute('href', response.playerBoardImage);
            document.getElementById("player-active-board-container").style.display = '';

            // let colour = response.playerColour;
            resetPlayerBoard();

            updateLoyalityTrack(colour);
            updateFavorsTrack(colour);
            updatePlayerBounties(colour);
            updatePlayerCargoCards(colour);
            updatePlayerHitLocation(colour);
            updatePlayerGolds(colour);
            updatePlayerShipModifications(colour);
            updatePlayerSpecialWeapons(colour);
            drawPlayerCaptainCard(colour);
            drawPlayerShipCard(colour);
            maxValues(colour)
            endCurrentAction(colour);
            };
        };
    xhr.open('GET', 'playerBoard', true);
    xhr.send();

};
