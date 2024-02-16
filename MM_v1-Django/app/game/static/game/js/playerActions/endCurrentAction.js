function endCurrentAction(colour) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            // console.log(response, response.amountActions, 'ILOSC AKCJI')


            document.getElementById('captain-actions-image').setAttribute('href', response.cubeImage);
            if (response.currentAction !== undefined) {
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
            };

            // NEXT PLAYER AFTER END TURN CLICK
            if (response.nextPlayer) {
                resetNav('after all actions');
                document.querySelector(`.title-value-player-${colour}`).innerHTML = 'DONE';
                return;
            };

        };
    };
    xhr.open('GET', 'endCurrentAction?colour=' + colour, true);
    xhr.send();

};



