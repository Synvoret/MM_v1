// PLAYER CAPTAIN CARD
function drawPlayerCaptainCard(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-board-captain-card-image').setAttribute('href', response.captainCardImage);
        }
    };
    xhr.open('GET', 'playerCaptainCard?colour=' + colour, true);
    xhr.send();
};