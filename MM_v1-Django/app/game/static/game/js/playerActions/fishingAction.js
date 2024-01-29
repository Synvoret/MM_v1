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
                document.querySelector('.nav-button.nav-button-scout').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-port').disabled = true;
                document.querySelector('.nav-button.nav-button-port').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-fishing').disabled = true;
                document.querySelector('.nav-button.nav-button-fishing').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-location').disabled = true;
                document.querySelector('.nav-button.nav-button-location').removeAttribute('onclick');
                document.querySelector('.nav-button.nav-button-end-turn').disabled = true;
                document.querySelector('.nav-button.nav-button-end-turn').removeAttribute('onclick');

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
        document.querySelector('.nav-button.nav-button-move-ship').removeAttribute('onclick');
        document.querySelector('.nav-button.nav-button-scout').disabled = false;
        document.querySelector('.nav-button.nav-button-scout').removeAttribute('onclick');
        document.querySelector('.nav-button.nav-button-port').disabled = false;
        document.querySelector('.nav-button.nav-button-port').removeAttribute('onclick');
        document.querySelector('.nav-button.nav-button-fishing').disabled = false;
        document.querySelector('.nav-button.nav-button-fishing').setAttribute('onclick', "fishingAction('get')");
        document.querySelector('.nav-button.nav-button-location').disabled = false;
        document.querySelector('.nav-button.nav-button-location').removeAttribute('onclick');
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
        document.querySelector('.nav-button.nav-button-end-turn').removeAttribute('onclick');

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let colour = xhr.responseText;
                updatePlayerGolds(colour);
                updateCaptainActions(colour);
            };
        };
        xhr.open('POST', 'fishingAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        // let data = 'colour=' + encodeURIComponent('SHIT');
                // '&selectedCaptain=' + encodeURIComponent(selectedCaptain) +
                // '&selectedShip=' + encodeURIComponent(selectedShip);

        // xhr.send(data);
        xhr.send();

    };
};
