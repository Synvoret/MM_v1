// DRAW GLORY CARD
function drawGloryCard(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-glory-card-1-image').setAttribute('href', response.gloryCardImage);
        }
    };
    xhr.open('GET', 'drawGloryCard?colour=' + colour, true);
    xhr.send();
};