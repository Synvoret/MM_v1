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
                if (response.sellGoods) {
                    document.querySelector(".nav-button.nav-button-sell-goods").disabled = true;
                    localStorage.setItem('sellGoods', 'sold');
                } else {
                    document.querySelector(".nav-button.nav-button-sell-goods").disabled = false;
                };
                document.querySelector(".nav-button.nav-button-buy-goods").style.display = '';
                if (response.buyGoods) {
                    document.querySelector(".nav-button.nav-button-buy-goods").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-buy-goods").disabled = false;
                };
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
                if (response.captainHomePort) {
                    document.querySelector('.nav-button.nav-button-stash-gold').disabled = false;
                    localStorage.setItem('captainHomePort', 'inHome');
                } else {
                    document.querySelector('.nav-button.nav-button-stash-gold').disabled = true;
                };
                document.querySelector(".nav-button.nav-button-raise-loyality").style.display = '';
                if (response.cantChangeLoyality) {
                    document.querySelector(".nav-button.nav-button-raise-loyality").disabled = true;
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

    // sell goods or buy goods
    if (when === 'sell goods' || when === 'buy goods') {
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
        localStorage.setItem('sellGoods', 'sold');
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


    // visit shipyard
    if (when === 'ship' || when === 'special weapon' || when === 'repair' || when === 'modifications') {
        document.querySelector('.nav-button.nav-button-buy-sell-ship').disabled = true;
        document.querySelector('.nav-button.nav-button-buy-sell-special-weapon').disabled = true;
        document.querySelector('.nav-button.nav-button-repair').disabled = true;
        document.querySelector('.nav-button.nav-button-buy-sell-ship-modification').disabled = true;

        document.querySelector('.nav-button.nav-button-back').disabled = true;
        document.querySelector('.nav-button.nav-button-end-turn').disabled = true;
    };


    if (when === 'recruit') {
        document.querySelector(`.nav-button.nav-button-sell-goods`).disabled = true;
        document.querySelector(`.nav-button.nav-button-buy-goods`).disabled = true;
        document.querySelector(`.nav-button.nav-button-visit-shipyard`).disabled = true;
        document.querySelector(`.nav-button.nav-button-recruit`).disabled = true;
        document.querySelector(`.nav-button.nav-button-acquire-rumor`).disabled = true;
        document.querySelector(`.nav-button.nav-button-claim-mission`).disabled = true;
        document.querySelector(`.nav-button.nav-button-stash-gold`).disabled = true;
        document.querySelector(`.nav-button.nav-button-raise-loyality`).disabled = true;
        document.querySelector(`.nav-button.nav-button-get-favour`).disabled = true;

        document.querySelector(`.nav-button.nav-button-back`).disabled = true;
        document.querySelector(`.nav-button.nav-button-end-turn`).disabled = true;
    };

    // raise loyality
    if (when === 'raise loyality') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                if (response.cantChangeLoyality) {
                    document.querySelector(".nav-button.nav-button-raise-loyality").disabled = true;
                    localStorage.setItem('loyalityUpdated', 'changed');
                } else {
                    document.querySelector(".nav-button.nav-button-raise-loyality").disabled = false;
                };
            };
        };
        xhr.open('GET', 'navPortActions?when=' + when, true);
        xhr.send();
    };

    // get favour
    if (when === 'get favour') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                if (response.cantGetFavour) {
                    document.querySelector(".nav-button.nav-button-get-favour").disabled = true;
                    localStorage.setItem('cantGetFavour', true);
                } else {
                    document.querySelector(".nav-button.nav-button-get-favour").disabled = false;
                };
            };
        };
        xhr.open('GET', 'navPortActions?when=' + when, true);
        xhr.send();
    };


    if (when === 'back to shipyard') {
        document.querySelector('.nav-button.nav-button-buy-sell-ship').disabled = false;
        document.querySelector('.nav-button.nav-button-buy-sell-special-weapon').disabled = false;
        document.querySelector('.nav-button.nav-button-repair').disabled = false;
        document.querySelector('.nav-button.nav-button-buy-sell-ship-modification').disabled = false;

        document.querySelector('.nav-button.nav-button-back').disabled = false;
        document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back to port')");
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
    };

    // back to port
    if (when === 'back to port') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.querySelector(".nav-actions-buttons").style.display = 'none';
                document.querySelector(".nav-port-buttons").style.display = '';
                document.querySelector(".nav-shipyard-buttons").style.display = 'none';
                document.querySelector(".step.nav-player-actions").innerHTML = 'Port Actions';

                // restoring buttons
                if (response.sellGoods) {
                    document.querySelector(".nav-button.nav-button-sell-goods").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-sell-goods").disabled = false;
                };
                if (response.buyGoods) {
                    document.querySelector(".nav-button.nav-button-buy-goods").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-buy-goods").disabled = false;
                };
                document.querySelector(".nav-button.nav-button-visit-shipyard").disabled = false;
                document.querySelector(".nav-button.nav-button-recruit").disabled = false;
                document.querySelector(".nav-button.nav-button-acquire-rumor").disabled = false;
                if (localStorage.getItem('missionInPort') === 'inPort') {
                    document.querySelector(".nav-button.nav-button-claim-mission").disabled = false;
                } else {
                    document.querySelector(".nav-button.nav-button-claim-mission").disabled = true;
                };
                if (localStorage.getItem('captainHomePort') === 'inHome') {
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
        };
        xhr.open('GET', 'navPortActions?when=' + when, true);
        xhr.send();
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