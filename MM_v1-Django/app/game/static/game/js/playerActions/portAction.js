function portAction(type_request, id=null) {


    if (type_request === 'port') {
        navPortActions(type_request);
    };


    if (type_request.includes('frame')) {

        let frameStyles = window.getComputedStyle(document.getElementById(type_request));
        let mainRect = Object()

        if (type_request.includes('sell')) {
            mainRect = window.getComputedStyle(document.getElementById('port-sell-goods-action-main-rect'));
        } else if (type_request.includes('buy')) {
            mainRect = window.getComputedStyle(document.getElementById('port-buy-goods-action-main-rect'));
        };

        let playerColour = mainRect.stroke;

        let number = type_request.split("-")[4];
        if (frameStyles.stroke === 'none') {
            document.getElementById(type_request).style.stroke = playerColour;
            document.getElementById(`port-buy-goods-cargo-card-${number}-cost-text`).style.stroke = playerColour;
            document.getElementById(`port-buy-goods-cargo-card-${number}-cost-text`).style.display = '';
        } else {
            document.getElementById(type_request).style.removeProperty('stroke');
            document.getElementById(`port-buy-goods-cargo-card-${number}-cost-text`).style.display = 'none';
            document.getElementById(`port-buy-goods-cargo-card-${number}-cost-text`).style.removeProperty('stroke');
        };

    };


    if (type_request === 'sell goods') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                // disabled buttons (nav)
                navPortActions(type_request);

                document.getElementById('port-sell-goods-action-use').style.display = '';
                // stroke colour
                document.getElementById("port-sell-goods-action-main-rect").style.stroke = colour;
                document.getElementById("port-sell-goods-action-result-text").style.stroke = colour;
                document.getElementById("port-sell-goods-action-gold-text").style.stroke = colour;
                document.getElementById("port-sell-goods-action-glory-text").style.stroke = colour;
                document.getElementById("port-sell-goods-action-ok-text").style.stroke = colour;
                document.getElementById("port-sell-goods-action-sell-marked-goods-text").style.stroke = colour;

                // setting text
                document.getElementById('port-sell-goods-value-result').innerHTML = 0;
                document.getElementById("port-sell-goods-glory-result").innerHTML = 0;

                // cargo Cards Images (local storage in browser)
                for (let i = 1; i <= 8; i++) {
                    if (response[`playerCargoCard${i}ImageUrl`] !== undefined) {
                        document.getElementById(`port-sell-goods-card-${i}-image`).style.removeProperty('stroke');
                        document.getElementById(`port-sell-goods-card-${i}-image`).setAttribute('href', response[`playerCargoCard${i}ImageUrl`]);
                        document.getElementById(`port-sell-goods-card-${i}-image`).setAttribute('name', response[`playerCargo${i}`]);
                        document.getElementById(`port-sell-goods-card-${i}-image`).style.pointerEvents = 'auto';
                    } else {
                        document.getElementById(`port-sell-goods-card-${i}-image`).style.removeProperty('stroke');
                        document.getElementById(`port-sell-goods-card-${i}-image`).setAttribute('href', '');
                        document.getElementById(`port-sell-goods-card-${i}-image`).style.pointerEvents = 'none';
                        document.getElementById(`port-sell-goods-card-${i}-image`).removeAttribute('name');
                    }
                };
                
                // setting demand token image
                document.getElementById('port-sell-goods-demand-token-in-port').setAttribute('name', response.demanTokenInPort);
                document.getElementById('port-sell-goods-demand-token-in-port').setAttribute('href', response.demanTokenInPortImageUrl);
            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'sell marked goods') {

        let goldID = parseInt(document.getElementById('port-sell-goods-value-result').textContent);
        let gloryID = parseInt(document.getElementById("port-sell-goods-glory-result").textContent);
        let demandName = document.getElementById("port-sell-goods-demand-token-in-port").getAttribute('name');
        let gloryPoint = 0;
        let demandGoodSold = false; // if demnad good was sell, remove demand token, after accept sell goods, replace demand token on board

        for (let i = 1; i <= 8; i++) {
            let frameID = document.getElementById(`port-sell-goods-card-${i}-frame`);
            let imageID = document.getElementById(`port-sell-goods-card-${i}-image`);

            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                frameID.style.removeProperty('stroke');
                imageID.setAttribute('href', '');
                imageID.style.pointerEvents = 'none';

                if (demandName === imageID.getAttribute('name')) {
                    demandGoodSold = true;
                    goldID += 6;
                    gloryPoint += 1;
                    if (gloryPoint >= 3) {
                        gloryID = 1;
                    };
                } else {
                    goldID += 3;
                };

            };
        };

        if (demandGoodSold) {
            document.getElementById("port-sell-goods-demand-token-in-port").setAttribute('href', '');
            document.getElementById("port-sell-goods-demand-token-in-port").removeAttribute('name');
        };
        document.getElementById('port-sell-goods-value-result').innerHTML = goldID;
        document.getElementById("port-sell-goods-glory-result").innerHTML = gloryID;

    };


    if (type_request === 'sell goods accept') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                navPortActions(type_request);

                updatePlayerCargoCards(colour);
                updatePlayerGolds(colour);
                updateGloryTrack(colour);

                if (document.getElementById('port-sell-goods-demand-token-in-port').getAttribute('name') === null) {
                    drawDemandToken(response.port); // draw demand token if player sold demand good for 6 gold
                };

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);

        let numbers = [];
        for (let i = 1; i <= 8; i++) {
            let imageID = document.getElementById(`port-sell-goods-card-${i}-image`);
            if (imageID.getAttribute('href') === '') {
                numbers.push(i);
            };
        };
        data += '&numbers=' + encodeURIComponent(JSON.stringify(numbers));

        let golds = parseInt(document.getElementById('port-sell-goods-value-result').textContent);
        data += '&golds=' + encodeURIComponent(golds);

        let glory = parseInt(document.getElementById('port-sell-goods-glory-result').textContent);
        data += '&glory=' + encodeURIComponent(glory);
        xhr.send(data);
    };


    let amount_cargo = 6; // for buy goods
    if (type_request ==='buy goods') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response)

                // disabled buttons (nav)
                navPortActions(type_request);

                document.getElementById('port-buy-goods-action-use').style.display = '';
                // stroke colour
                document.getElementById("port-buy-goods-action-main-rect").style.stroke = colour;
                document.getElementById("port-buy-goods-action-result-text").style.stroke = colour;
                document.getElementById("port-buy-goods-action-gold-text").style.stroke = colour;
                document.getElementById("port-buy-goods-action-ok-text").style.stroke = colour;
                document.getElementById("port-buy-goods-action-buy-marked-goods-text").style.stroke = colour;

                // setting text
                document.getElementById('port-buy-goods-value-result').innerHTML = response[`playerGolds`];

                // cargo Cards Images (local storage in browser)
                let cost_cargo = {}
                // setting prices
                for (let i = 1; i <= amount_cargo; i++) {
                    if (cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]]) {
                        cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]] -= 1
                        if (cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]] === 0) {
                            cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]] = 1;
                        };
                    } else {
                        cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]] = 3;
                    };
                };

                for (let i = 1; i <= amount_cargo; i++) {
                    document.getElementById(`port-buy-goods-card-${i}-frame`).style.removeProperty('stroke');
                    document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text`).style.display = 'none';
                    document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text`).style.removeProperty('stroke');
                    if (response[`cargoCard${i}ToBuy`] !== undefined) {
                        document.getElementById(`port-buy-goods-card-${i}-image`).style.removeProperty('stroke');
                        document.getElementById(`port-buy-goods-card-${i}-image`).setAttribute('href', response[`cargoCard${i}ToBuy`][`awers`]);
                        document.getElementById(`port-buy-goods-card-${i}-image`).setAttribute('name', response[`cargoCard${i}ToBuy`][`id`]);
                        document.getElementById(`port-buy-goods-card-${i}-image`).style.pointerEvents = 'auto';
                        document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text-value`).innerHTML = cost_cargo[response[`cargoCard${i}ToBuy`][`cargo`]];
                    } else {
                        document.getElementById(`port-buy-goods-card-${i}-image`).style.removeProperty('stroke');
                        document.getElementById(`port-buy-goods-card-${i}-image`).setAttribute('href', '');
                        document.getElementById(`port-buy-goods-card-${i}-image`).removeAttribute('name');
                        document.getElementById(`port-buy-goods-card-${i}-image`).style.pointerEvents = 'none';
                        document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text-value`).innerHTML = 0;
                    };
                };

                // player Cargo Cards
                let freeSpaceOnHold = response[`freeSpaceInShipHold`];
                for (let i = 1; i <= 8; i++) {
                    document.getElementById(`port-buy-goods-player-card-${i}-frame`).style.removeProperty('stroke'); // free space in hold
                    if (response[`playerCargoCard${i}`] !== undefined) {
                        document.getElementById(`port-buy-goods-player-card-${i}-image`).setAttribute('href', response[`playerCargoCard${i}`][`awers`]);
                    } else {
                        document.getElementById(`port-buy-goods-player-card-${i}-image`).setAttribute('href', '');
                        if (freeSpaceOnHold > 0) {
                            document.getElementById(`port-buy-goods-player-card-${i}-frame`).style.stroke = colour;  // free space in hold
                            freeSpaceOnHold -= 1;
                        };
                    };
                };

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'buy marked goods') {

        let goldID = parseInt(document.getElementById('port-buy-goods-value-result').textContent);

        // cargo cards
        for (let i = 1; i <= amount_cargo; i++) {
            let frameID = document.getElementById(`port-buy-goods-card-${i}-frame`);
            let imageID = document.getElementById(`port-buy-goods-card-${i}-image`);
            let textID = document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text`);
            if (window.getComputedStyle(frameID).getPropertyValue('stroke') !== 'none') {
                goldID -= parseInt(document.getElementById(`port-buy-goods-cargo-card-${i}-cost-text-value`).textContent);
                // free space on ship hold
                for (let j = 1; j <= 8; j++) {
                    // if (document.getElementById(`port-buy-goods-player-card-${j}-image`).getAttribute('href') === '') {
                    if (window.getComputedStyle(document.getElementById(`port-buy-goods-player-card-${j}-frame`)).stroke !== 'none') {
                        document.getElementById(`port-buy-goods-player-card-${j}-image`).setAttribute('href', imageID.getAttribute('href'));
                        document.getElementById(`port-buy-goods-player-card-${j}-frame`).style.removeProperty('stroke');
                        frameID.style.removeProperty('stroke');
                        imageID.setAttribute('href', '');
                        imageID.style.pointerEvents = 'none';
                        textID.style.display = 'none';
                        document.getElementById('port-buy-goods-value-result').innerHTML = goldID;
                        break;
                    };
                };
            };
        };
    };


    if (type_request === 'buy goods accept') {
        let xhr = new XMLHttpRequest();
        let numbers = [];
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                navPortActions(type_request);

                updatePlayerCargoCards(colour);
                updatePlayerGolds(colour);
            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        for (let i = 1; i <= amount_cargo; i++) {
            let imageID = document.getElementById(`port-buy-goods-card-${i}-image`);
            if (imageID.getAttribute('href') === '') {
                numbers.push(parseInt(imageID.getAttribute('name')));
            };
        };
        data += '&numbers=' + encodeURIComponent(JSON.stringify(numbers));
        let golds = parseInt(document.getElementById('port-buy-goods-value-result').textContent);
        data += '&golds=' + encodeURIComponent(golds);

        xhr.send(data);
    };


    if (type_request === 'visit shipyard') {
        navPortActions(type_request);
    };


    if (type_request === 'ship') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response)

                // disabled buttons (nav)
                navPortActions(type_request);
                document.getElementById('port-visit-shipyard-ship-action-use').style.display = '';
                // stroke colour on g tag element
                document.getElementById("port-visit-shipyard-ship-action").style.stroke = colour;
                // remove all frames
                document.querySelectorAll('.frame').forEach(function(element) {
                    element.remove();
                });

                // setting golds
                document.getElementById('player-coin-amount').innerHTML = response[`playerGolds`];

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'ship sell buy') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response);

                document.getElementById(`player-ship-sell-buy`).style.display = '';

                document.getElementById(`port-visit-shipyard-player-ship-sell`).setAttribute('href', response.playerShipImageUrl);

                let imageBuyShip = document.getElementById(id).getAttribute('href');
                document.getElementById(`port-visit-shipyard-player-ship-buy`).setAttribute('href', imageBuyShip);
                document.getElementById(`ship-buy-cost`).innerHTML = response.unitBuyCost;
                document.getElementById(`summary-buy-cost`).innerHTML = response.unitBuyCost;
                document.getElementById(`ship-sell-profit`).innerHTML = response.unitSellCost;
                document.getElementById(`damages-sell-profit`).innerHTML = response.damagesPlayerUnit;
                document.getElementById(`modifications-sell-profit`).innerHTML = response.modificationsPlayerUnit;
                let summary = parseInt(document.getElementById(`ship-sell-profit`).innerHTML) - parseInt(document.getElementById(`damages-sell-profit`).innerHTML) + parseInt(document.getElementById(`modifications-sell-profit`).innerHTML);
                document.getElementById(`summary-sell-profit`).innerHTML = summary;

                document.getElementById(`port-visit-shipyard-player-ship-sell-ship-unit-text`).innerHTML = response.unitSellShip;
                document.getElementById(`port-visit-shipyard-player-ship-buy-ship-unit-text`).innerHTML = response.unitBuyShip;

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request + '&unitID=' + id, true);
        xhr.send();
    };


    if (type_request === 'ship sell buy accept' ) {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.getElementById(`player-ship-sell-buy`).style.display = 'none';

                updatePlayerGolds(response.playerColour);
                updatePlayerShipModifications(response.playerColour);
                updatePlayerHitLocation(response.playerColour);
                maxValues(response.playerColour);
                drawPlayerShipCard(response.playerColour);

                putShipPlastic(response.newShip, response.playerColour, response.localisation, true);

            };
        };
        let newUnit = document.getElementById(`port-visit-shipyard-player-ship-buy-ship-unit-text`).innerHTML;
        let profitForSell = parseInt(document.getElementById(`summary-sell-profit`).innerHTML);
        let costForBuy = parseInt(document.getElementById(`summary-buy-cost`).innerHTML);
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&newUnit=' + encodeURIComponent(newUnit);
        data += '&profitForSell=' + encodeURIComponent(profitForSell);
        data += '&costForBuy=' + encodeURIComponent(costForBuy);
        xhr.send(data);
    };


    if (type_request === 'special weapon') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response);

                // disabled buttons (nav)
                navPortActions(type_request);
                document.getElementById('port-visit-shipyard-special-weapons-action-use').style.display = '';
                // stroke colour
                document.getElementById("port-visit-shipyard-special-weapons-action-main-rect").style.stroke = colour;

                // setting colour on texts
                document.querySelectorAll('.special-weapons-text').forEach(function(element) {
                    element.style.stroke = colour;
                });

                // setting golds
                document.getElementById('player-coin-amount').innerHTML = response[`playerGolds`];
                // setting special weapons for buy
                // document.querySelectorAll('.buy-special-weapon').forEach(function(element) {
                    
                // });
                // setting special weapons for sell
                if (response.forSellChainShot !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-chain-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-chain-shot').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-chain-shot').setAttribute('href', response.forSellChainShot);
                    document.getElementById('port-visit-shipyard-player-special-weapons-chain-shot').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-chain-shot').setAttribute('href', response.forBuyChainShot);
                    document.getElementById('port-visit-shipyard-special-weapons-chain-shot').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-chain-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-chain-shot').removeAttribute('onclick');
                };

                if (response.forSellGrapeshot !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-grapeshot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-grapeshot').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grapeshot').setAttribute('href', response.forSellGrapeshot);
                    document.getElementById('port-visit-shipyard-player-special-weapons-grapeshot').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-grapeshot').setAttribute('href', response.forBuyGrapeshot);
                    document.getElementById('port-visit-shipyard-special-weapons-grapeshot').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-grapeshot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grapeshot').removeAttribute('onclick');
                };

                if (response.forSellGrapplingHooks !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-grappling-hooks').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-grappling-hooks').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grappling-hooks').setAttribute('href', response.forSellGrapplingHooks);
                    document.getElementById('port-visit-shipyard-player-special-weapons-grappling-hooks').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-grappling-hooks').setAttribute('href', response.forBuyGrapplingHooks);
                    document.getElementById('port-visit-shipyard-special-weapons-grappling-hooks').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-grappling-hooks').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grappling-hooks').removeAttribute('onclick');
                };

                if (response.forSellDoubleShot !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-double-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-double-shot').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-double-shot').setAttribute('href', response.forSellDoubleShot);
                    document.getElementById('port-visit-shipyard-player-special-weapons-double-shot').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-double-shot').setAttribute('href', response.forBuyDoubleShot);
                    document.getElementById('port-visit-shipyard-special-weapons-double-shot').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-double-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-double-shot').removeAttribute('onclick');
                };

                if (response.forSellCaltrops !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-caltrops').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-caltrops').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-caltrops').setAttribute('href', response.forSellCaltrops);
                    document.getElementById('port-visit-shipyard-player-special-weapons-caltrops').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-caltrops').setAttribute('href', response.forBuyCaltrops);
                    document.getElementById('port-visit-shipyard-special-weapons-caltrops').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-caltrops').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-caltrops').removeAttribute('onclick');
                };

                if (response.forSellHeatedShot !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-heated-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-heated-shot').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-heated-shot').setAttribute('href', response.forSellHeatedShot);
                    document.getElementById('port-visit-shipyard-player-special-weapons-heated-shot').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-heated-shot').setAttribute('href', response.forBuyHeatedShot);
                    document.getElementById('port-visit-shipyard-special-weapons-heated-shot').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-heated-shot').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-heated-shot').removeAttribute('onclick');
                };

                if (response.forSellGrenade !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-grenade').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-grenade').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grenade').setAttribute('href', response.forSellGrenade);
                    document.getElementById('port-visit-shipyard-player-special-weapons-grenade').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-grenade').setAttribute('href', response.forBuyGrenade);
                    document.getElementById('port-visit-shipyard-special-weapons-grenade').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-grenade').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-grenade').removeAttribute('onclick');
                };

                if (response.forSellPremiumRum !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-premium-rum').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-premium-rum').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-premium-rum').setAttribute('href', response.forSellPremiumRum);
                    document.getElementById('port-visit-shipyard-player-special-weapons-premium-rum').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-premium-rum').setAttribute('href', response.forBuyPremiumRum);
                    document.getElementById('port-visit-shipyard-special-weapons-premium-rum').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-premium-rum').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-premium-rum').removeAttribute('onclick');
                };

                if (response.forSellExplosiveShell !== undefined) {
                    document.getElementById('port-visit-shipyard-special-weapons-explosive-shell').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-special-weapons-explosive-shell').removeAttribute('onclick');
                    document.getElementById('port-visit-shipyard-player-special-weapons-explosive-shell').setAttribute('href', response.forSellExplosiveShell);
                    document.getElementById('port-visit-shipyard-player-special-weapons-explosive-shell').setAttribute('onclick', "portAction('special weapon sell', this.getAttribute('name')); portAction('special weapon')");
                } else {
                    document.getElementById('port-visit-shipyard-special-weapons-explosive-shell').setAttribute('href', response.forBuyExplosiveShell);
                    document.getElementById('port-visit-shipyard-special-weapons-explosive-shell').setAttribute('onclick', "portAction('special weapon buy', this.getAttribute('name')); portAction('special weapon')");
                    document.getElementById('port-visit-shipyard-player-special-weapons-explosive-shell').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-player-special-weapons-explosive-shell').removeAttribute('onclick');
                };

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'special weapon buy' || type_request === 'special weapon sell') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                updatePlayerGolds(response.playerColour);
                updatePlayerSpecialWeapons(response.playerColour);

            };
        };

        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&weapon=' + encodeURIComponent(id);
        xhr.send(data);
    };


    if (type_request === 'repair') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response)

                // disabled buttons (nav)
                navPortActions(type_request);

                document.getElementById('port-visit-shipyard-repair-action-use').style.display = '';

                // stroke colour
                document.getElementById("port-visit-shipyard-repair-action-main-rect").style.stroke = colour;

                // cleanning cubes
                document.querySelectorAll('.repair-location').forEach(function(element) {
                    element.setAttribute('href', '');
                });

                // setting colour on texts
                document.querySelectorAll('.repair-text').forEach(function(element) {
                    element.style.stroke = colour;
                });

                // setting golds
                document.getElementById('player-coin-amount').innerHTML = response[`playerGolds`];

                // show cube and cube max
                // max value
                document.getElementById(`port-visit-shipyard-repair-hull-${response.playerHullMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-visit-shipyard-repair-cargo-${response.playerCargoMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-visit-shipyard-repair-masts-${response.playerMastsMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-visit-shipyard-repair-crew-${response.playerCrewMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-visit-shipyard-repair-cannons-${response.playerCannonsMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                // value
                if (response.playerHullValue !== 0) {
                    document.getElementById(`port-visit-shipyard-repair-hull-${response.playerHullValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCargoValue !== 0) {
                    document.getElementById(`port-visit-shipyard-repair-cargo-${response.playerCargoValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerMastsValue !== 0) {
                    document.getElementById(`port-visit-shipyard-repair-masts-${response.playerMastsValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCrewValue !== 0) {
                    document.getElementById(`port-visit-shipyard-repair-crew-${response.playerCrewValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCannonsValue !== 0) {
                    document.getElementById(`port-visit-shipyard-repair-cannons-${response.playerCannonsValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request.includes('repair location')) {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                updatePlayerGolds(response.playerColour);
                updatePlayerHitLocation(response.playerColour);

            };
        };

        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'modifications') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response)

                // disabled buttons (nav)
                navPortActions(type_request);

                document.getElementById('port-visit-shipyard-modifications-action-use').style.display = '';

                // stroke colour
                document.getElementById("port-visit-shipyard-modifications-action-main-rect").style.stroke = colour;

                // setting colour on texts
                document.querySelectorAll('.modifications-text').forEach(function(element) {
                    element.style.stroke = colour;
                });

                // setting golds
                document.getElementById('player-coin-amount').innerHTML = response[`playerGolds`];

                // for BUY
                if (response.forBuy !== undefined) {
                    document.getElementById('port-visit-shipyard-modifications').setAttribute('href', response['forBuy']);
                    document.getElementById('port-visit-shipyard-modifications').setAttribute('name', response['portModification']);
                    document.getElementById(`port-visit-shipyard-modifications`).setAttribute('onclick', "portAction('modification buy', this.getAttribute('name')); portAction('modifications')");
                    // flip token on port
                    document.getElementById(`ship-modification-${response.tokenFlip}-image`).setAttribute('href', response.forBuy);
                } else {
                    document.getElementById('port-visit-shipyard-modifications').setAttribute('href', '');
                    document.getElementById('port-visit-shipyard-modifications').removeAttribute('name');
                    document.getElementById(`port-visit-shipyard-modifications`).removeAttribute('onclick');
                    document.getElementById(`ship-modification-${response.tokenFlip}-image`).setAttribute('href', '');
                };

                // cleanning FOR SALE
                document.querySelectorAll('.sell-modifications').forEach(function(element) {
                    element.remove();
                });
                let i = 0;
                for (let key in response) {
                    let x = 20;
                    let y = 460;
                    if (key.startsWith('forSell')) {
                        let name = key.replace(/forSell/, '');
                        // create element <image>
                        var imageElement = document.createElementNS("http://www.w3.org/2000/svg", "image");
                        // imageElement.setAttribute("id", `port-visit-shipyard-player-modifications-${}`);
                        imageElement.setAttribute("name", name);
                        imageElement.setAttribute("class", "port-visit-shipyard-modifications sell-modifications");
                        imageElement.setAttribute("x", x + i * 100);
                        imageElement.setAttribute("y", y);
                        imageElement.setAttribute("width", "100");
                        imageElement.setAttribute("href", response[key]);
                        imageElement.setAttribute('onclick', "portAction('modification sell', this.getAttribute('name')); portAction('modifications')");
                        // gain tag <g> about id "player-modifications-for-sale"
                        var gElement = document.getElementById("player-modifications-for-sale");
                        // add element <image> to tag <g>
                        gElement.appendChild(imageElement);
                        i++;
                    };
                };

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'modification buy' || type_request === 'modification sell') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                updatePlayerShipModifications(response.playerColour);
                updatePlayerGolds(response.playerColour);

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        data += '&modification=' + encodeURIComponent(id);
        xhr.send(data);
    };


    if (type_request === 'recruit') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                console.log(response);

                // disabled buttons (nav)
                navPortActions(type_request);

                document.getElementById('port-recruit-action-use').style.display = '';

                // stroke colour
                document.getElementById("port-recruit-action-main-rect").style.stroke = colour;

                // cleanning cubes
                document.querySelectorAll('.recruit-location').forEach(function(element) {
                    element.setAttribute('href', '');
                });

                // setting colour on texts
                document.querySelectorAll('.recruit-text').forEach(function(element) {
                    element.style.stroke = colour;
                });

                // setting golds
                document.getElementById('player-coin-amount').innerHTML = response[`playerGolds`];

                // show cube and cube max
                // max value
                document.getElementById(`port-recruit-hull-${response.playerHullMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-recruit-cargo-${response.playerCargoMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-recruit-masts-${response.playerMastsMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-recruit-crew-${response.playerCrewMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                document.getElementById(`port-recruit-cannons-${response.playerCannonsMaxValue}`).setAttribute('href', response['playerCubeMaxImageUrl']);
                // value
                if (response.playerHullValue !== 0) {
                    document.getElementById(`port-recruit-hull-${response.playerHullValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCargoValue !== 0) {
                    document.getElementById(`port-recruit-cargo-${response.playerCargoValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerMastsValue !== 0) {
                    document.getElementById(`port-recruit-masts-${response.playerMastsValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCrewValue !== 0) {
                    document.getElementById(`port-recruit-crew-${response.playerCrewValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };
                if (response.playerCannonsValue !== 0) {
                    document.getElementById(`port-recruit-cannons-${response.playerCannonsValue}`).setAttribute('href', response['playerCubeImageUrl']);
                };

                if (response.recruitCrew) {
                    // console.log('NIE TWORZĘ ROLL DICE');
                } else {
                    // restart amount success
                    document.getElementById('recruit-amount-success').innerHTML = 0;
                    // DICES
                    rollDices(
                        type ='create', 
                        amountDices = response.playerCaptainLeadershipValue, 
                        // amountDices = 2, 
                        storageValuesID = 'recruit-amount-success',
                        parentID = "port-recruit-action", 
                        x = 640, 
                        y = 415, 
                        colour = colour, 
                        );
                };

            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'recruit crew') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                updatePlayerGolds(response.playerColour);
                updatePlayerHitLocation(response.playerColour);
            };
        };

        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        let leadershipSuccess = document.getElementById('recruit-amount-success').innerHTML;
        data += '&leadershipSuccess=' + encodeURIComponent(leadershipSuccess);
        xhr.send(data);
    };


    if (type_request === 'recruit done') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                
                document.getElementById('port-recruit-action-use').style.display = 'none';
                rollDices('destroy');

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'stash gold') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                updateLoyalityTrack(response.playerColour);
                updatePlayerGolds(response.playerColour);

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request ===  'raise loyality') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                if (response.cantChangeLoyality) {
                    return;
                } else {
                    updateLoyalityTrack(response.playerColour);
                    updatePlayerGolds(response.playerColour);
                    navPortActions(type_request);
                    // localStorage.setItem('loyalityUpdated', 'changed');
                };

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'get favour') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                if (response.cantGetFavour) {
                    return;
                } else {
                    updateFavorsTrack(response.playerColour);
                    updatePlayerGolds(response.playerColour);
                    navPortActions(type_request);
                };

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);

        xhr.send(data);
    };




    if (type_request === 'back to shipyard') {
        navPortActions(type_request);
        document.getElementById('port-visit-shipyard-special-weapons-action-use').style.display = 'none';
        document.getElementById('port-visit-shipyard-repair-action-use').style.display = 'none';
        document.getElementById('port-visit-shipyard-modifications-action-use').style.display = 'none';
        document.getElementById('port-visit-shipyard-ship-action-use').style.display = 'none';
        document.getElementById(`player-ship-sell-buy`).style.display = 'none';
    };


    if (type_request === 'back to port') {
        // back after sell goods
        document.getElementById('port-sell-goods-action-use').style.display = 'none';
        document.getElementById('port-buy-goods-action-use').style.display = 'none';

        navPortActions('back to port');
    };


    if (type_request === 'back') {
        navPortActions('back');
        endCurrentAction(localStorage.getItem('colourPlayerActive'));
        localStorage.removeItem('colourPlayerActive');
    };

    // console.log(localStorage);

};
