// PLAYER SHIP CARD
function drawPlayerShipCard(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-ship-card-image').setAttribute('href', response.shipCardImage);
        }
    };
    xhr.open('GET', 'playerShipCard?colour=' + colour, true);
    xhr.send();
};