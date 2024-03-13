// after choose captains and ships and amount players
function goGame() {
    document.getElementById('nav-add-players-div').style.display = "none";

    // PUTT ALL PLASTIC SHIPS FOR PLAYERS
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            if (response.player_blueCaptainHomePort !== undefined) {
                navGoGame('blue');
                putShipPlastic(response.player_blueShip, 'blue', response.player_blueCaptainHomePort, true);
            };

            if (response.player_greenCaptainHomePort !== undefined) {
                navGoGame('green');
                putShipPlastic(response.player_greenShip, 'green', response.player_greenCaptainHomePort, true);
            };

            if (response.player_redCaptainHomePort !== undefined) {
                navGoGame('red');
                putShipPlastic(response.player_redShip, 'red', response.player_redCaptainHomePort, true);
            };

            if (response.player_yellowCaptainHomePort !== undefined) {
                navGoGame('yellow');
                putShipPlastic(response.player_yellowShip, 'yellow', response.player_yellowCaptainHomePort, true);
            };

        }
    };
    xhr.open('GET', 'goGame', true);
    xhr.send();

    startRound();

};
