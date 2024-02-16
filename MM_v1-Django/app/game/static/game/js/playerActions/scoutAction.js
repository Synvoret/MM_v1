// SCOUT ACTIONs - consume one action
function scoutAction(type_request) {


    if (type_request === 'scout') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                console.log(response)

                document.querySelector('.nav-actions-buttons').style.display = 'none';
                document.querySelector(".nav-scouting-buttons").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = 'none';
                document.querySelector(".step.player-actions").innerHTML = 'Scouting';
                document.querySelector(".nav-button.nav-button-back").disabled = false;
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "scoutAction('back')")

                if (response.merchantToken) {
                    document.querySelector(".nav-button.nav-button-scout-merchant").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';
                };

                if (response.dutchShip) {
                    document.querySelector(".nav-button.nav-button-scout-dutch-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-dutch-ship").style.display = 'none';
                };

                if (response.englishShip) {
                    document.querySelector(".nav-button.nav-button-scout-english-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-english-ship").style.display = 'none';
                };

                if (response.frenchShip) {
                    document.querySelector(".nav-button.nav-button-scout-french-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-french-ship").style.display = 'none';
                };

                if (response.spanishShip) {
                    document.querySelector(".nav-button.nav-button-scout-spanish-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-spanish-ship").style.display = 'none';
                };

                if (response.smallPirateShip) {
                    document.querySelector(".nav-button.nav-button-scout-small-pirate-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-small-pirate-ship").style.display = 'none';
                };

                if (response.largePirateShip) {
                    document.querySelector(".nav-button.nav-button-scout-large-pirate-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-large-pirate-ship").style.display = 'none';
                };

                if (response.bluePlayerShip) {
                    document.querySelector(".nav-button.nav-button-scout-blue-player-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-blue-player-ship").style.display = 'none';
                };

                if (response.greenPlayerShip) {
                    document.querySelector(".nav-button.nav-button-scout-green-player-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-green-player-ship").style.display = 'none';
                };

                if (response.redPlayerShip) {
                    document.querySelector(".nav-button.nav-button-scout-red-player-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-red-player-ship").style.display = 'none';
                };

                if (response.yellowPlayerShip) {
                    document.querySelector(".nav-button.nav-button-scout-yellow-player-ship").style.display = '';
                } else {
                    document.querySelector(".nav-button.nav-button-scout-yellow-player-ship").style.display = 'none';
                };

                

            };
        };
        xhr.open('GET', 'scoutAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'merchant') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                console.log('Interacting with Merchant')
                // randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, true)

                document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = false;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = false;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = false;
                document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-dutch-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-english-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-french-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-spanish-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-small-pirate-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-large-pirate-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-blue-player-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-green-player-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-red-player-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-yellow-player-ship").style.display = 'none';

                // endCurrentAction(colour);
            };
        };
        xhr.open('GET', 'scoutAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'merchant raid') {
        console.log('RAID on MERCHANT');
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                document.getElementById('merchant-raid-action-use').style.display = '';

                // turn off buttons
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
                document.querySelector(".nav-button.nav-button-back").disabled = true;
                document.querySelector(".nav-button.nav-button-end-turn").disabled = true;

                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'merchant trade') {
        console.log('TRADE with MERCHANT');
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.colour;
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'merchant escort') {
        console.log('ESCORT MERCHANT');
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.colour;
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };



    if (type_request === 'back') {

        document.getElementById('merchant-raid-action-use').style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = 'none';


        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-scouting-buttons").style.display = 'none';
        document.querySelector(".step.player-actions").innerHTML = 'Player Actions'
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    };

};
