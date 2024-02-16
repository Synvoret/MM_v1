// after choose captains and ships and amount players
function goGame() {
    document.getElementById('add-players-div').style.display = "none";

    // PUTT ALL PLASTIC SHIPS FOR PLAYERS
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            // document.getElementById('title-players-div').style.display = '';

            if (response.player_blueCaptainHomePort !== undefined) {
                document.querySelector('.title-player-blue').style.display = '';
                putShipPlastic(response.player_blueShip, 'blue', response.player_blueCaptainHomePort, true)
            };

            if (response.player_greenCaptainHomePort !== undefined) {
                document.querySelector('.title-player-green').style.display = '';
                putShipPlastic(response.player_greenShip, 'green', response.player_greenCaptainHomePort, true)
            };

            if (response.player_redCaptainHomePort !== undefined) {
                document.querySelector('.title-player-red').style.display = '';
                putShipPlastic(response.player_redShip, 'red', response.player_redCaptainHomePort, true)
            };

            if (response.player_yellowCaptainHomePort !== undefined) {
                document.querySelector('.title-player-yellow').style.display = '';
                putShipPlastic(response.player_yellowShip, 'yellow', response.player_yellowCaptainHomePort, true)
            };

        }
    };
    xhr.open('GET', 'goGame', true);
    xhr.send();

    startRound();

};
