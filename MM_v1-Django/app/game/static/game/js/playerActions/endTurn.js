function endTurn() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            
            let response = JSON.parse(xhr.responseText);
            let colour = response.playerColour;
            resetNav('during actions');

            // start player actions only player want or players used all actions
            if (response.endRound) {
                startRound();
            } else {
                navEndTurn(response.playerColourEndingTurn);
                startPlayerTurn();
            };

            
            localStorage.clear();
        };
    };
    xhr.open('POST', 'endTurn', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();


};
