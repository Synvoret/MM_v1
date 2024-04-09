function endCurrentAction(colour, afterTest=false) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('captain-actions-image').setAttribute('href', response.cubeImage);

            if (response.amountActions !== undefined && afterTest === true) { // after test that consumes action point, e.g. Scouting.
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
            } else if (response.amountActions === undefined && afterTest === true) {
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
                let okText = document.getElementById("ok-text").getAttribute('onclick');
                okText = okText.replace("navRollDices('testOk');", "navRollDices('testOk', amountActions=true);")
                console.log(okText)
                document.getElementById("ok-text").setAttribute('onclick', okText);
                document.getElementById("cancel-text").setAttribute('onclick', `navRollDices(when='testCancel', amountActions=true); rollDices(type='destroy')`)
                document.querySelector('.nav-button.nav-button-back').disabled = true;
                document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
            };
            
            if (response.nextPlayer && afterTest === false) { // NEXT PLAYER AFTER END TURN CLICK
                resetNav('after all actions');
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
                document.querySelector(`.nav-title-value-player-${colour}`).innerHTML = 'DONE';
                return;
            } else if (response.currentAction !== undefined && afterTest === false) { // reset DURING ACTIONS (between player actions)
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
                resetNav('during actions');
            };
            
            // // reset DURING ACTIONS (between player actions)
            // if (response.currentAction !== undefined && afterTest === false) {
            //     document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
            //     resetNav('during actions');
            // };

            // // NEXT PLAYER AFTER END TURN CLICK
            // if (response.nextPlayer && afterTest === false) {
            //     resetNav('after all actions');
            //     document.querySelector(`.nav-title-value-player-${colour}`).innerHTML = 'DONE';
            //     return;
            // };

        };
    };
    xhr.open('GET', 'endCurrentAction?colour=' + colour, true);
    xhr.send();

};



