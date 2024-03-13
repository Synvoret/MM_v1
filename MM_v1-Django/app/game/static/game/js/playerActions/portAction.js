function portAction(type_request) {

    if (type_request === 'port') {
        navPortActions(type_request);
    };


    if (type_request.includes('frame')) {

        let frameStyles = window.getComputedStyle(document.getElementById(type_request));
        let mainRect = window.getComputedStyle(document.getElementById('port-sell-goods-action-main-rect'));

        if (type_request.includes('sell')) {
            mainRect = window.getComputedStyle(document.getElementById('port-sell-goods-action-main-rect'));
        };

        let playerColour = mainRect.stroke;

        if (frameStyles.stroke === 'none') {
            document.getElementById(type_request).style.stroke = playerColour;
        } else {
            document.getElementById(type_request).style.removeProperty('stroke'); 
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
                    drawDemandToken(response.port) // draw demand token if player sold demand good for 6 gold
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


    if (type_request === 'visit shipyard') {
        navPortActions(type_request);
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
                    localStorage.setItem('loyalityUpdated', 'changed');
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
                };

            };
        };
        xhr.open('POST', 'portAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);

        xhr.send(data);
    };


    if (type_request === 'back to port') {
        // back after sell goods
        document.getElementById('port-sell-goods-action-use').style.display = 'none';

        navPortActions('back to port');
    };


    if (type_request === 'back') {
        navPortActions('back');
        endCurrentAction(localStorage.getItem('colourPlayerActive'));
        localStorage.removeItem('colourPlayerActive');
    };

    console.log(localStorage);

};
