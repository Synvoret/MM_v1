function navPortActions(when) {

    // port
    if (when === 'port') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                localStorage.setItem('colourPlayerActive', response.playerColour);

                document.querySelector(".step.nav-player-actions").innerHTML = 'Port Actions';
                document.querySelector(".nav-actions-buttons").style.display = 'none';
                document.querySelector(".nav-port-buttons").style.display = '';

                document.querySelector(".nav-button.nav-button-sell-goods").style.display = '';
                document.querySelector(".nav-button.nav-button-sell-goods").disabled = false;
                document.querySelector(".nav-button.nav-button-buy-goods").style.display = '';
                document.querySelector(".nav-button.nav-button-buy-goods").disabled = false;
                document.querySelector(".nav-button.nav-button-visit-shipyard").style.display = '';
                document.querySelector(".nav-button.nav-button-visit-shipyard").disabled = false;
                document.querySelector(".nav-button.nav-button-recruit").style.display = '';
                document.querySelector(".nav-button.nav-button-recruit").disabled = false;
                document.querySelector(".nav-button.nav-button-acquire-rumor").style.display = '';
                document.querySelector(".nav-button.nav-button-acquire-rumor").disabled = false;
                document.querySelector(".nav-button.nav-button-claim-mission").style.display = '';
                if (response.missionInPort) {
                    document.querySelector(".nav-button.nav-button-claim-mission").disabled = false;
                    localStorage.setItem('missionInPort', 'inPort');
                } else {
                    document.querySelector(".nav-button.nav-button-claim-mission").disabled = true;
                };
                document.querySelector('.nav-button.nav-button-stash-gold').style.display = '';
                if (response.playerHomePort) {
                    document.querySelector('.nav-button.nav-button-stash-gold').disabled = false;
                    localStorage.setItem('playerHomePort', 'inHome');
                } else {
                    document.querySelector('.nav-button.nav-button-stash-gold').disabled = true;
                };
                document.querySelector(".nav-button.nav-button-raise-loyality").style.display = '';
                if (response.cantChangeLoyality) {
                    document.querySelector(".nav-button.nav-button-raise-loyality").disabled = true;
                    localStorage.setItem('loyalityUpdated', 'changed');
                } else {
                    document.querySelector(".nav-button.nav-button-raise-loyality").disabled = false;
                };
                document.querySelector(".nav-button.nav-button-get-favour").style.display = '';
                if (response.cantGetFavour) {
                    document.querySelector('.nav-button.nav-button-get-favour').disabled = true;
                    localStorage.setItem('cantGetFavour', true);
                } else {
                    document.querySelector('.nav-button.nav-button-get-favour').disabled = false;
                };

                document.querySelector(".nav-button.nav-button-back").disabled = false;
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back')");
            };
        };
        xhr.open('GET', 'navPortActions?when=' + when, true);
        xhr.send();
    };

    // sell goods
    if (when === 'sell goods') {
        document.querySelector(".nav-button.nav-button-sell-goods").disabled = true;
        document.querySelector(".nav-button.nav-button-buy-goods").disabled = true;
        document.querySelector(".nav-button.nav-button-visit-shipyard").disabled = true;
        document.querySelector(".nav-button.nav-button-recruit").disabled = true;
        document.querySelector(".nav-button.nav-button-acquire-rumor").disabled = true;
        document.querySelector(".nav-button.nav-button-claim-mission").disabled = true;
        document.querySelector(".nav-button.nav-button-stash-gold").disabled = true;
        document.querySelector(".nav-button.nav-button-raise-loyality").disabled = true;
        document.querySelector(".nav-button.nav-button-get-favour").disabled = true;
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back to port')");
        document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
    };

    // sell goods accept
    if (when === 'sell goods accept') {
        document.querySelector('.nav-button.nav-button-sell-goods').disabled = true;
    };

    // visit shipyard
    if (when === 'visit shipyard') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                
                document.querySelector(".step.nav-player-actions").innerHTML = 'Port Shipyard';
                document.querySelector(".nav-port-buttons").style.display = 'none';
                document.querySelector(".nav-shipyard-buttons").style.display = '';

                document.querySelector(".nav-button.nav-button-back").disabled = false;
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back to port')");
            };
        };
        xhr.open('GET', 'navPortActions?when=' + when, true);
        xhr.send();
    };

    // back to port
    if (when === 'back to port') {
        document.querySelector(".nav-actions-buttons").style.display = 'none';
        document.querySelector(".nav-port-buttons").style.display = '';
        document.querySelector(".nav-shipyard-buttons").style.display = 'none';
        document.querySelector(".step.nav-player-actions").innerHTML = 'Port Actions';

        // restoring buttons
        document.querySelector(".nav-button.nav-button-sell-goods").disabled = true; // always TRUE after port action
        document.querySelector(".nav-button.nav-button-buy-goods").disabled = false;
        document.querySelector(".nav-button.nav-button-visit-shipyard").disabled = false;
        document.querySelector(".nav-button.nav-button-recruit").disabled = false;
        document.querySelector(".nav-button.nav-button-acquire-rumor").disabled = false;
        if (localStorage.getItem('missionInPort') === 'inPort') {
            document.querySelector(".nav-button.nav-button-claim-mission").disabled = false;
        } else {
            document.querySelector(".nav-button.nav-button-claim-mission").disabled = true;
        };
        if (localStorage.getItem('playerHomePort') === 'inHome') {
            document.querySelector('.nav-button.nav-button-stash-gold').disabled = false;
        } else {
            document.querySelector('.nav-button.nav-button-stash-gold').disabled = true;
        };
        if (localStorage.getItem('loyalityUpdated') === 'changed') {
            document.querySelector(".nav-button.nav-button-raise-loyality").disabled = true;
        } else {
            document.querySelector(".nav-button.nav-button-raise-loyality").disabled = false;
        };
        if (localStorage.getItem('cantGetFavour')) {
            document.querySelector(".nav-button.nav-button-get-favour").disabled = true;
        } else {
            document.querySelector(".nav-button.nav-button-get-favour").disabled = false;
        };

        document.querySelector(".nav-button.nav-button-back").disabled = false;
        document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back')");
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    };

    // back
    if (when === 'back') {
        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-port-buttons").style.display = 'none';
        document.querySelector(".nav-shipyard-buttons").style.display = 'none';
        document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions';

        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    }
};