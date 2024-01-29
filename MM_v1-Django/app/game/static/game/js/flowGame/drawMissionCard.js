// DRAW ONE MISSION CARD
function drawMissionCard(poz) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('mission-' + poz + '-card-image').setAttribute('href', response.cardImage);
            document.getElementById('mission-' + poz + '-sign-image').setAttribute('href', response.signMission);
            document.getElementById('mission-sign-' + response.portMission).setAttribute('href', '#mission-' + poz + '-sign-image');
        };
    };
    xhr.open('GET', 'drawMissionCard?mission_number=' + poz, true);
    xhr.send();
};
