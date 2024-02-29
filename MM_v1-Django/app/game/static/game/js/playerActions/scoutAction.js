// SCOUT ACTIONs - consume one action
function scoutAction(type_request) {


    if (type_request === 'scout') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

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
                response.playerHaveDestroyedHitLocation

                document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';

                document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = '';
                if (response.playerHaveDestroyedHitLocation) {
                    document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = false;
                };

                document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = '';
                if (response.playerIsPirate) {
                    document.querySelector(".nav-button.nav-button-scout-merchant-trade").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scout-merchant-trade").disabled = false;
                };

                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = false;

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
                updatePlayerBounties(colour);
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
                // DICES
                rollDices(
                    type ='create', 
                    amountDices = response.playerCaptainSeamanshipValue, 
                    storageValuesID = 'merchant-raid-amount-success',
                    parentID = "merchant-raid-action", 
                    x = 210, 
                    y = 635, 
                    colour = colour, 
                    );
                // cargo Cards Images (local storage in browser)
                localStorage.setItem('cargoCard1Value', parseInt(response.cargoCard1Value));
                localStorage.setItem('cargoCard2Value', parseInt(response.cargoCard2Value));
                localStorage.setItem('cargoCard3Value', parseInt(response.cargoCard3Value));
                localStorage.setItem('cargoCard1Hit', response.cargoCard1Hit);
                localStorage.setItem('cargoCard2Hit', response.cargoCard2Hit);
                localStorage.setItem('cargoCard3Hit', response.cargoCard3Hit);
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
                document.getElementById('merchant-raid-ship-maneuverability').innerHTML = response.shipManeuverability;
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
        for (let i = 1; i <= 9; i++) {
            localStorage.removeItem(`cargoCard${i}Value`);
            localStorage.removeItem(`cargoCard${i}Hit`);
        }
        // const keys = Object.keys(localStorage);
        // const patternValue = /^cargoCard\d+Value$/;
        // const patternHit = /^cargoCard\d+Hit$/;
        // keys.forEach(key => {
        //     if (patternValue.test(key)) {
        //         localStorage.removeItem(key);
        //     }
        //     if (patternHit.test(key)) {
        //         localStorage.removeItem(key);
        //     }
        // });
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request.includes('frame')) { // mark a frame over cargo card
        let frameStyles = window.getComputedStyle(document.getElementById(type_request));
        let mainRect = window.getComputedStyle(document.getElementById('merchant-raid-action-main-rect'));

        if (type_request.includes('raid')) {
            mainRect = window.getComputedStyle(document.getElementById('merchant-raid-action-main-rect'));
        } else if (type_request.includes('trade')) {
            mainRect = window.getComputedStyle(document.getElementById('merchant-trade-action-main-rect'));
        };

        let playerColour = mainRect.stroke;

        if (frameStyles.stroke === 'none') {
            for (let i = 1; i <= 3; i++) {
                if (type_request.includes(`merchant-trade-card-${i}-frame`)) {
                    document.getElementById(type_request).style.stroke = 'darkorange';
                    return;
                } else {
                    document.getElementById(type_request).style.stroke = playerColour; // merchant-raid-card-X-frame
                }
            }
        } else {
            document.getElementById(type_request).style.removeProperty('stroke'); // merchant-raid-card-X-frame
        };

    };


    if (type_request.includes('spend special weapon')) {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                rollDices(type='reroll to success', amountDices=1, storageValuesID='merchant-raid-amount-success');

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
                if (document.getElementById(`merchant-raid-card-12-image`).getAttribute('href') !== "") {
                    return;
                }
                let i = 1;
                while (i <= 12) {
                    let imageID = `merchant-raid-card-${i}-image`;
                    if (document.getElementById(imageID).getAttribute('href') === "") {
                        document.getElementById(imageID).setAttribute('href', response.cargoCardDrawImageUrl);
                        document.getElementById(imageID).style.pointerEvents = 'auto';
                        localStorage.setItem(`cargoCard${i}Value`, parseInt(response.cargoCardPlunderValue));
                        localStorage.setItem(`cargoCard${i}Hit`, response.cargoCardHits);
                        break;
                    };
                    i++;
                };

                let gold = parseInt(document.getElementById('merchant-raid-value-result').textContent);
                gold += parseInt(response.cargoCardPlunderValue);
                document.getElementById('merchant-raid-value-result').innerHTML = gold;

                let hitLocationValue = parseInt(document.getElementById(`merchant-raid-${response.cargoCardHits}-span`).textContent);
                hitLocationValue += 1;
                document.getElementById(`merchant-raid-${response.cargoCardHits}-span`).innerHTML = hitLocationValue;

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


    if (type_request === 'merchant raid discard card') {

        let amountSuccess = parseInt(document.getElementById('merchant-raid-amount-success').textContent);
        if (amountSuccess === 0) {
            return;
        }

        let i = 1;
        let amountStroke = 0;
        let cardToDiscard = 0;

        while (i <= 12) {
            let frameID = document.getElementById(`merchant-raid-card-${i}-frame`);
            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                amountStroke++;
                cardToDiscard = i
            };
            i++;
        };

        if (amountStroke > 1) {
            return;
        } else if (amountStroke === 1) {
            document.getElementById(`merchant-raid-card-${cardToDiscard}-frame`).style.removeProperty('stroke');
            document.getElementById(`merchant-raid-card-${cardToDiscard}-image`).style.pointerEvents = 'none';
            document.getElementById(`merchant-raid-card-${cardToDiscard}-image`).setAttribute('href', '');
            let valueResult = parseInt(document.getElementById('merchant-raid-value-result').textContent);
            valueResult -= parseInt(localStorage.getItem(`cargoCard${cardToDiscard}Value`))
            document.getElementById('merchant-raid-value-result').innerHTML = valueResult;
            let hitLocation = localStorage.getItem(`cargoCard${cardToDiscard}Hit`);
            let hitResult = parseInt(document.getElementById(`merchant-raid-${hitLocation}-span`).textContent);
            hitResult--;
            document.getElementById(`merchant-raid-${hitLocation}-span`).innerHTML = hitResult;
            // local storage
            localStorage.removeItem(`cargoCard${cardToDiscard}Value`);
            localStorage.removeItem(`cargoCard${cardToDiscard}Hit`);

            amountSuccess--;
            document.getElementById('merchant-raid-amount-success').innerHTML = amountSuccess;
        } else {
            return;
        }
    };


    if (type_request === 'merchant raid exchange card') {
        // check posibility
        let amountSuccess = parseInt(document.getElementById('merchant-raid-amount-success').textContent);
        if (amountSuccess === 0) {
            return;
        }
        // remove marked card
        let i = 1;
        let amountStroke = 0;
        let cardToDiscard = 0;
        while (i <= 12) {
            let frameID = document.getElementById(`merchant-raid-card-${i}-frame`);
            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                amountStroke++;
                cardToDiscard = i
            };
            i++;
        };
        if (amountStroke > 1) {
            return;
        } else if (amountStroke === 1) {
            document.getElementById(`merchant-raid-card-${cardToDiscard}-frame`).style.removeProperty('stroke');
            document.getElementById(`merchant-raid-card-${cardToDiscard}-image`).style.pointerEvents = 'none';
            document.getElementById(`merchant-raid-card-${cardToDiscard}-image`).setAttribute('href', '');
            let valueResult = parseInt(document.getElementById('merchant-raid-value-result').textContent);
            valueResult -= parseInt(localStorage.getItem(`cargoCard${cardToDiscard}Value`))
            document.getElementById('merchant-raid-value-result').innerHTML = valueResult;
            let hitLocation = localStorage.getItem(`cargoCard${cardToDiscard}Hit`);
            let hitResult = parseInt(document.getElementById(`merchant-raid-${hitLocation}-span`).textContent);
            hitResult--;
            document.getElementById(`merchant-raid-${hitLocation}-span`).innerHTML = hitResult;
            // local storage
            localStorage.removeItem(`cargoCard${cardToDiscard}Value`);
            localStorage.removeItem(`cargoCard${cardToDiscard}Hit`);

            // amountSuccess--;
            // document.getElementById('merchant-raid-amount-success').innerHTML = amountSuccess;
        } else {
            return;
        }
        // draw new card in this same place from where removed
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                let i = 1;
                while (i <= 12) {
                    let imageID = `merchant-raid-card-${i}-image`;
                    if (document.getElementById(imageID).getAttribute('href') === "") {
                        document.getElementById(imageID).setAttribute('href', response.cargoCardDrawImageUrl);
                        document.getElementById(imageID).style.pointerEvents = 'auto';
                        localStorage.setItem(`cargoCard${i}Value`, parseInt(response.cargoCardPlunderValue));
                        localStorage.setItem(`cargoCard${i}Hit`, response.cargoCardHits);
                        break;
                    };
                    i++;
                };

                let gold = parseInt(document.getElementById('merchant-raid-value-result').textContent);
                gold += parseInt(response.cargoCardPlunderValue);
                document.getElementById('merchant-raid-value-result').innerHTML = gold;

                let hitLocationValue = parseInt(document.getElementById(`merchant-raid-${response.cargoCardHits}-span`).textContent);
                hitLocationValue += 1;
                document.getElementById(`merchant-raid-${response.cargoCardHits}-span`).innerHTML = hitLocationValue;

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


    if (type_request === 'merchant raid accept') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                console.log(response.resultMerchantRaid, 'RESULT MERCHANT RAID')
                updateGloryTrack(colour)
                updatePlayerGolds(colour);
                updatePlayerHitLocation(colour);
                endCurrentAction(colour);
            };
        };
        let getGold = parseInt(document.getElementById('merchant-raid-value-result').textContent);
        let getHullHit = parseInt(document.getElementById('merchant-raid-hull-span').textContent);
        let getCargoHit = parseInt(document.getElementById('merchant-raid-cargo-span').textContent);
        let getMastsHit = parseInt(document.getElementById('merchant-raid-masts-span').textContent);
        let getCrewHit = parseInt(document.getElementById('merchant-raid-crew-span').textContent);
        let getCannonsHit = parseInt(document.getElementById('merchant-raid-cannons-span').textContent);
        let getEscapeHit = parseInt(document.getElementById('merchant-raid-escape-span').textContent);
        let getManeuverability = parseInt(document.getElementById('merchant-raid-ship-maneuverability').textContent);
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&getGold=' + encodeURIComponent(getGold);
        data += '&getHullHit=' + encodeURIComponent(getHullHit);
        data += '&getCargoHit=' + encodeURIComponent(getCargoHit);
        data += '&getMastsHit=' + encodeURIComponent(getMastsHit);
        data += '&getCrewHit=' + encodeURIComponent(getCrewHit);
        data += '&getCannonsHit=' + encodeURIComponent(getCannonsHit);
        if (getEscapeHit >= getManeuverability) {
            data += '&getEscapeHit=' + encodeURIComponent(true);
        } else {
            data += '&getEscapeHit=' + encodeURIComponent(false);
        };
        xhr.send(data);
        for (let i = 1; i <= 12; i++) {
            localStorage.removeItem(`cargoCard${i}Value`);
            localStorage.removeItem(`cargoCard${i}Hit`);
        };
        
        rollDices('destroy');

    };


    // TRADE TRADE TRADE TRADE TRADE TRADE 
    if (type_request === 'merchant trade') {
        console.log('TRADE with MERCHANT');
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                console.log(response, 'TRADE MERCHANT')
                let colour = response.playerColour;
                document.getElementById('merchant-trade-action-use').style.display = '';
                // turn off buttons
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-raid").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-trade").disabled = true;
                document.querySelector(".nav-button.nav-button-scouting.nav-button-scout-merchant-escort").disabled = true;
                document.querySelector(".nav-button.nav-button-back").disabled = true;
                document.querySelector(".nav-button.nav-button-end-turn").disabled = true;
                // cargo Cards Images (local storage in browser)
                document.getElementById("merchant-trade-card-1-image").setAttribute('href', response.merchantCargoCard1ImageUrl);
                document.getElementById("merchant-trade-card-2-image").setAttribute('href', response.merchantCargoCard2ImageUrl);
                document.getElementById("merchant-trade-card-3-image").setAttribute('href', response.merchantCargoCard3ImageUrl);
                document.getElementById("merchant-trade-card-1-image").style.pointerEvents = 'auto';
                document.getElementById("merchant-trade-card-2-image").style.pointerEvents = 'auto';
                document.getElementById("merchant-trade-card-3-image").style.pointerEvents = 'auto';
                for (let i = 1; i <= 7; i++) {
                    let playerCargoCardImageID = `merchant-trade-card-${i + 3}-image`;
                    if (response[`playerCargoCard${i}ImageUrl`]) {
                        document.getElementById(playerCargoCardImageID).setAttribute('href', response[`playerCargoCard${i}ImageUrl`]);
                        document.getElementById(playerCargoCardImageID).style.pointerEvents = 'auto';
                    } else {
                        document.getElementById(playerCargoCardImageID).setAttribute('href', '');
                        document.getElementById(playerCargoCardImageID).style.pointerEvents = 'none';
                    }
                };
                // DICES
                rollDices(
                    type ='create', 
                    amountDices = response.playerCaptainInfluenceValue,
                    storageValuesID = 'merchant-trade-amount-success',
                    parentID = "merchant-trade-action", 
                    x = 210, 
                    y = 635, 
                    colour = colour, 
                    );
                // stroke colour
                document.getElementById("merchant-trade-action-main-rect").style.stroke = colour;
                document.getElementById("merchant-trade-action-result-text").style.stroke = colour;
                document.getElementById("merchant-trade-action-draw-roll-text").style.stroke = colour;
                document.getElementById("merchant-trade-action-exchange-card-text").style.stroke = colour;
                document.getElementById("merchant-trade-action-ok-text").style.fill = colour;
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'merchant trade exchange cards') {
        // check success
        let amountSuccess = parseInt(document.getElementById('merchant-trade-amount-success').textContent);
        if (amountSuccess === 0) {
            return;
        }
        // check marked cards
        let i = 1;
        let amountStroke = 0;

        let merchantCardsMarked = 0;
        console.log(localStorage);
        while (i <= 3) {
            let frameID = document.getElementById(`merchant-trade-card-${i}-frame`);
            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                merchantCardsMarked++;
            };
            i++;
        };

        let playerCardsMarked = 0;
        while (i <= 10) {
            let frameID = document.getElementById(`merchant-trade-card-${i}-frame`);
            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                amountStroke++;
                // cardToDiscard = i
            };
            i++;
        };
        // if (amountStroke > 1) {
        //     return;
        // } else if (amountStroke === 1) {
        //     document.getElementById(`merchant-trade-card-${cardToDiscard}-frame`).style.removeProperty('stroke');
        //     document.getElementById(`merchant-trade-card-${cardToDiscard}-image`).style.pointerEvents = 'none';
        //     document.getElementById(`merchant-trade-card-${cardToDiscard}-image`).setAttribute('href', '');
        // } else {
        //     return;
        // };
        // exchange marked cards
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.colour;

                amountSuccess--;
                document.getElementById('merchant-trade-amount-success').innerHTML = amountSuccess;
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&amountSuccess=' + encodeURIComponent(amountSuccess);
        xhr.send(data);
    }


    if (type_request === 'merchant trade accept') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                console.log(response.resultMerchantRaid, 'RESULT MERCHANT TRADE')
                updatePlayerCargoCards(colour);
                endCurrentAction(colour);
            };
        };
        // let getGold = parseInt(document.getElementById('merchant-raid-value-result').textContent);
        // let getHullHit = parseInt(document.getElementById('merchant-raid-hull-span').textContent);
        // let getCargoHit = parseInt(document.getElementById('merchant-raid-cargo-span').textContent);
        // let getMastsHit = parseInt(document.getElementById('merchant-raid-masts-span').textContent);
        // let getCrewHit = parseInt(document.getElementById('merchant-raid-crew-span').textContent);
        // let getCannonsHit = parseInt(document.getElementById('merchant-raid-cannons-span').textContent);
        // let getEscapeHit = parseInt(document.getElementById('merchant-raid-escape-span').textContent);
        // let getManeuverability = parseInt(document.getElementById('merchant-raid-ship-maneuverability').textContent);
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        // data += '&getGold=' + encodeURIComponent(getGold);
        // data += '&getHullHit=' + encodeURIComponent(getHullHit);
        // data += '&getCargoHit=' + encodeURIComponent(getCargoHit);
        // data += '&getMastsHit=' + encodeURIComponent(getMastsHit);
        // data += '&getCrewHit=' + encodeURIComponent(getCrewHit);
        // data += '&getCannonsHit=' + encodeURIComponent(getCannonsHit);
        // if (getEscapeHit >= getManeuverability) {
        //     data += '&getEscapeHit=' + encodeURIComponent(true);
        // } else {
        //     data += '&getEscapeHit=' + encodeURIComponent(false);
        // };
        xhr.send(data);
        // for (let i = 1; i <= 12; i++) {
        //     localStorage.removeItem(`cargoCard${i}Value`);
        //     localStorage.removeItem(`cargoCard${i}Hit`);
        // };

        rollDices('destroy');

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
        document.getElementById('merchant-trade-action-use').style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-raid").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-trade").style.display = 'none';

        document.querySelector(".nav-button.nav-button-scout-merchant-escort").style.display = 'none';


        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-scouting-buttons").style.display = 'none';
        document.querySelector(".step.player-actions").innerHTML = 'Player Actions'
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;

        // RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID RAID 
        // RAID cleaning cargo cards
        let i = 1;
        while (i <= 12) {
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
        
        // TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE 
        // TRADE cleaning cargo cards
        i = 1;
        while (i <= 7) {
            let frame = `merchant-trade-card-${i}-frame`;
            document.getElementById(frame).style.removeProperty('stroke');
            let image = `merchant-trade-card-${i}-image`;
            document.getElementById(image).setAttribute('href', "");
            document.getElementById(image).style.pointerEvents = 'none';
            i++;
        };
    };


};
