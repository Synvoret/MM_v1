function endTurn() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            
            let response = JSON.parse(xhr.responseText);

            console.log(response, ' PO ZAKOŃCZENIU TURY PRZEZ GRACZA')
            // let colour = response.playerColour;
            resetNav('during actions');

            // start player actions only player want or players used all actions
            if (response.endRound) {
                startRound();
            } else {
                document.querySelector(`.title-value-player-${response.playerColourEndingTurn}`).innerHTML = 'DONE';
                startPlayerActions();
            };
            

        };
    };
    xhr.open('POST', 'endTurn', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    // let data = 'colour=' + encodeURIComponent(colour);
    // xhr.send(data);
    xhr.send();


};
