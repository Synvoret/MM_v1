function navScoutActions(when) {

    // scout
    if (when === 'scout') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.querySelector('.nav-actions-buttons').style.display = 'none';
                document.querySelector(".nav-scouting-buttons").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = 'none';
                document.querySelector(".step.nav-player-actions").innerHTML = 'Scouting';
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
        xhr.open('GET', 'navScoutActions?when=' + when, true);
        xhr.send();
    };

    // merchant
    if (when === 'merchant') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                response.playerHaveDestroyedHitLocation

                document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';

                document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = '';
                // raid
                if (response.playerHaveDestroyedHitLocation) {
                    document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = false;
                };
                // trade 
                if (response.playerIsPirate) {
                    document.querySelector(".nav-button.nav-button-scout-merchant-trade").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scout-merchant-trade").disabled = false;
                };
                // escort 
                if (response.playerHaveDestroyedHitLocation || response.playerIsPirate) {
                    document.querySelector(".nav-button.nav-button-scout-merchant-escort").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scout-merchant-escort").disabled = false;
                }

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

            };
        };
        xhr.open('GET', 'navScoutActions?when=' + when, true);
        xhr.send();
    };

    // merchant raid
    if (when === 'merchant raid') {
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
    };

    // merchant trade
    if (when === 'merchant trade') {
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
    };

    // merchant escort
    if (when === 'merchant escort') {
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
        document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
    };

    // back
    if (when === 'back') {
        document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = 'none';
        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-scouting-buttons").style.display = 'none';
        document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions'
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    };
};
