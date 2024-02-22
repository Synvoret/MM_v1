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


    // RAID RAID RAID RAID RAID RAID 
    if (type_request === 'merchant raid') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                document.getElementById('merchant-raid-action-use').style.display = '';
                if (response.merchantTrack !== undefined) {
                    document.getElementById(`merchant-token-track-${response.merchantTrack}-image`).setAttribute('href', response.merchantToken);
                    document.getElementById(`merchant-token-${response.removeMerchantToken}-image`).setAttribute('href', '');
                    document.getElementById(`merchant-token-${response.removeMerchantToken}`).setAttribute('href', '');
                } else if (response.newDistributeMerchantTokens) {
                    drawMerchantToken('all')
                    document.getElementById('merchant-token-track-first-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-second-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-thrith-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-fourth-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-fivth-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-sixth-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-seventh-image').setAttribute('href', '');
                    document.getElementById('merchant-token-track-eighth-image').setAttribute('href', '');
                }
                // turn off buttons
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
                document.querySelector(".nav-button.nav-button-back").disabled = true;
                document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
                // restart amount success
                document.getElementById('merchant-raid-amount-success').innerHTML = 0;
                // cargo Cards Images
                document.getElementById("merchant-raid-card-1-image").setAttribute('href', response.cargoCard1ImageUrl);
                document.getElementById("merchant-raid-card-2-image").setAttribute('href', response.cargoCard2ImageUrl);
                document.getElementById("merchant-raid-card-3-image").setAttribute('href', response.cargoCard3ImageUrl);
                document.getElementById("merchant-raid-card-1-image").style.pointerEvents = 'auto';
                document.getElementById("merchant-raid-card-2-image").style.pointerEvents = 'auto';
                document.getElementById("merchant-raid-card-3-image").style.pointerEvents = 'auto';
                document.getElementById("merchant-raid-value-result").innerHTML = response.cargoCardValue;
                document.getElementById("merchant-raid-hull-span").innerHTML = response.hullHits;
                document.getElementById("merchant-raid-cargo-span").innerHTML = response.cargoHits;
                document.getElementById("merchant-raid-masts-span").innerHTML = response.mastsHits;
                document.getElementById("merchant-raid-crew-span").innerHTML = response.crewHits;
                document.getElementById("merchant-raid-cannons-span").innerHTML = response.cannonsHits;
                document.getElementById("merchant-raid-escape-span").innerHTML = response.escapeResult;
                // player special weapons
                for (let specialWeapon of response.playerSpecialWeapons) {
                    document.getElementById(`merchant-raid-${specialWeapon}-image`).setAttribute('href', `/media/specialWeapons/${specialWeapon}.png`);
                    document.getElementById(`merchant-raid-${specialWeapon}-image`).style.pointerEvents = 'auto';
                };
                // stroke colour
                document.getElementById("merchant-raid-action-main-rect").style.stroke = colour;
                document.getElementById("merchant-raid-action-result-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-gold-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-hits-text").style.stroke = colour;
                document.getElementById("merchant-raid-hull").style.stroke = colour;
                document.getElementById("merchant-raid-cargo").style.stroke = colour;
                document.getElementById("merchant-raid-masts").style.stroke = colour;
                document.getElementById("merchant-raid-crew").style.stroke = colour;
                document.getElementById("merchant-raid-cannons").style.stroke = colour;
                document.getElementById("merchant-raid-escape").style.stroke = colour;
                document.getElementById("merchant-raid-action-draw-roll-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-draw-spend-weapon-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-draw-card-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-discard-card-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-exchange-card-text").style.stroke = colour;
                document.getElementById("merchant-raid-action-ok-text").style.fill = colour;
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request.includes('frame')) { // mark a frame over cargo card
        let frameStyles = window.getComputedStyle(document.getElementById(type_request));
        let mainRect = window.getComputedStyle(document.getElementById('merchant-raid-action-main-rect'));
        let playerColour = mainRect.stroke;
        if (frameStyles.stroke === 'none') {
            document.getElementById(type_request).style.stroke = playerColour; // merchant-raid-card-X-frame
        } else {
            document.getElementById(type_request).style.removeProperty('stroke'); // merchant-raid-card-X-frame
        };
    };

    if (type_request.includes('spend special weapon')) {
        console.log('SPUSZCZMA BRON')
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let amountSuccess = parseInt(document.getElementById('merchant-raid-amount-success').textContent);
                amountSuccess++;
                document.getElementById('merchant-raid-amount-success').innerHTML = amountSuccess;

                document.getElementById("merchant-raid-chain-shot-image").setAttribute('href', '');
                document.getElementById("merchant-raid-grapeshot-image").setAttribute('href', '');
                document.getElementById("merchant-raid-grappling-hooks-image").setAttribute('href', '');
                document.getElementById("merchant-raid-heated-shot-image").setAttribute('href', '');
                document.getElementById("merchant-raid-double-shot-image").setAttribute('href', '');
                document.getElementById("merchant-raid-caltrops-image").setAttribute('href', '');
                document.getElementById("merchant-raid-premium-rum-image").setAttribute('href', '');
                document.getElementById("merchant-raid-grenade-image").setAttribute('href', '');
                document.getElementById("merchant-raid-explosive-shell-image").setAttribute('href', '');
                document.getElementById("merchant-raid-chain-shot-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-grapeshot-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-grappling-hooks-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-heated-shot-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-double-shot-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-caltrops-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-premium-rum-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-grenade-image").style.pointerEvents = 'none';
                document.getElementById("merchant-raid-explosive-shell-image").style.pointerEvents = 'none';
                for (let specialWeapon of response.playerSpecialWeapons) {
                    document.getElementById(`merchant-raid-${specialWeapon}-image`).setAttribute('href', `/media/specialWeapons/${specialWeapon}.png`);
                    document.getElementById(`merchant-raid-${specialWeapon}-image`).style.pointerEvents = 'auto';
                };

                updatePlayerSpecialWeapons(response.playerColour);
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        // data += '&amountSuccess=' + encodeURIComponent(amountSuccess);
        xhr.send(data);
    };


    if (type_request === 'merchant raid draw card') {
        let xhr = new XMLHttpRequest();
        let amountSuccess = parseInt(document.getElementById('merchant-raid-amount-success').textContent);
        if (amountSuccess === 0) {
            return;
        }
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                // let amountSuccess = parseInt(document.getElementById('merchant-raid-amount-success').textContent);

                let i = 1;
                while (i <= 9) {
                    let imageID = `merchant-raid-card-${i}-image`;
                    if (document.getElementById(imageID).getAttribute('href') === "") {
                        document.getElementById(imageID).setAttribute('href', response.cargoCardDrawImageUrl);
                        document.getElementById(imageID).style.pointerEvents = 'auto';
                        break;
                    };
                    i++;
                };

                let gold = parseInt(document.getElementById('merchant-raid-value-result').textContent);
                gold += parseInt(response.cargoCardPlunderValue);
                console.log(gold, typeof(gold), response.cargoCardPlunderValue, typeof(response.cargoCardPlunderValue))
                document.getElementById('merchant-raid-value-result').innerHTML = gold;

                amountSuccess--;
                document.getElementById('merchant-raid-amount-success').innerHTML = amountSuccess;
                
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&amountSuccess=' + encodeURIComponent(amountSuccess);
        xhr.send(data);
    };


    if (type_request === 'merchant raid accept') { // for MERCHANT RAID
        console.log('AKCEPTUJĘ ROZLICZENIE BITWY')
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                endCurrentAction(response.playerColour);
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        // data += '&key=' + encodeURIComponent(value);
        xhr.send(data);
    }


    // TRADE TRADE TRADE TRADE TRADE TRADE 
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


    // ESCORT ESCORT ESCORT ESCORT ESCORT
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

        // RAID cleaning cargo cards
        let i = 1;
        while (i <= 9) {
            let frame = `merchant-raid-card-${i}-frame`;
            document.getElementById(frame).style.removeProperty('stroke');
            let image = `merchant-raid-card-${i}-image`;
            document.getElementById(image).setAttribute('href', "");
            document.getElementById(image).style.pointerEvents = 'none';
            i++;
        };
        // RAID cleaning special weapons
        document.getElementById("merchant-raid-chain-shot-image").setAttribute('href', '');
        document.getElementById("merchant-raid-grapeshot-image").setAttribute('href', '');
        document.getElementById("merchant-raid-grappling-hooks-image").setAttribute('href', '');
        document.getElementById("merchant-raid-heated-shot-image").setAttribute('href', '');
        document.getElementById("merchant-raid-double-shot-image").setAttribute('href', '');
        document.getElementById("merchant-raid-caltrops-image").setAttribute('href', '');
        document.getElementById("merchant-raid-premium-rum-image").setAttribute('href', '');
        document.getElementById("merchant-raid-grenade-image").setAttribute('href', '');
        document.getElementById("merchant-raid-explosive-shell-image").setAttribute('href', '');
        document.getElementById("merchant-raid-chain-shot-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-grapeshot-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-grappling-hooks-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-heated-shot-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-double-shot-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-caltrops-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-premium-rum-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-grenade-image").style.pointerEvents = 'none';
        document.getElementById("merchant-raid-explosive-shell-image").style.pointerEvents = 'none';
    };

};
