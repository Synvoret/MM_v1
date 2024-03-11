// FISHING ACTION - consume one action point
function fishingAction(type_request) {

    if (type_request === 'get') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                document.querySelector('.nav-button.nav-button-move-ship').disabled = true;
                document.querySelector('.nav-button.nav-button-move-ship').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-scout').disabled = true;
                document.querySelector('.nav-button.nav-button-fishing').disabled = true;
                document.querySelector('.nav-button.nav-button-fishing').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-location').disabled = true;
                document.querySelector('.nav-button.nav-button-location').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-end-turn').disabled = true;
                document.getElementById('fishing-action-main-rect').style.stroke = response.playerColour;
                document.getElementById('fishing-action-ok-text').style.fill = response.playerColour;
                document.getElementById('fishing-card-image').setAttribute('href', response.fishingCardImage);
                document.getElementById('fishing-action-use').style.display = 'block';
            }
        };
        xhr.open('GET', 'fishingAction', true);
        xhr.send();
    };


    if (type_request === 'post') {
        document.querySelector('.nav-button.nav-button-move-ship').disabled = false;
        document.querySelector('.nav-button.nav-button-move-ship').setAttribute('onclick', "moveAction('moves')");
        document.querySelector('.nav-button.nav-button-scout').disabled = false;
        document.querySelector('.nav-button.nav-button-fishing').disabled = false;
        document.querySelector('.nav-button.nav-button-fishing').setAttribute('onclick', "fishingAction('get')");
        document.querySelector('.nav-button.nav-button-location').disabled = false;
        document.querySelector('.nav-button.nav-button-location').removeAttribute('onclick');
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.colour;
                if (response.fishingValue) {
                    updatePlayerGolds(colour);
                };
                if (response.fishingHits) {
                    updatePlayerHitLocation(colour);
                };
                document.getElementById('fishing-action-main-rect').style.removeProperty('stroke');
                document.getElementById('fishing-action-ok-text').style.removeProperty('fill');
                document.getElementById('fishing-card-image').setAttribute('href', '');
                document.getElementById('fishing-action-use').style.display = 'none';

                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'fishingAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send();
    };
};
