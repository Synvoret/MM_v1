// NEW PLAYER
// colour - player colour
function newPlayer(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            // console.log(response)

            document.getElementById('new-player-use').style.display = "block";

            document.getElementById('new-player-main-rect').style.stroke = colour;
            document.getElementById('new-captain-1-frame').style.removeProperty('stroke');
            document.getElementById('new-captain-2-frame').style.removeProperty('stroke');
            document.getElementById('new-ship-sloop-frame').style.removeProperty('stroke');
            document.getElementById('new-ship-flute-frame').style.removeProperty('stroke');
            document.getElementById('new-captain-ship-get-text').style.removeProperty('fill');
            document.getElementById('new-captain-ship-get-text').removeAttribute('onclick');

            document.getElementById('new-captain-1-image').setAttribute('href', response.captain1Image);
            document.getElementById('new-captain-1-frame').setAttribute('name', response.captain1Name);
            document.getElementById('new-captain-2-image').setAttribute('href', response.captain2Image);
            document.getElementById('new-captain-2-frame').setAttribute('name', response.captain2Name);
            document.getElementById('new-ship-sloop-image').setAttribute('href', response.shipSloopImage);
            document.getElementById('new-ship-flute-image').setAttribute('href', response.shipFluteImage);

        };
    };
    xhr.open('GET', 'newPlayer?colour=' + colour, true);
    xhr.send();
};


// SELECTED CAPTAIN AND SHIP
function selectNewCaptainShip(id) {

    let colour = (document.getElementById('new-player-main-rect')).style.stroke;

    let cap1 = document.getElementById('new-captain-1-frame');
    let cap2 = document.getElementById('new-captain-2-frame');
    let sloop = document.getElementById('new-ship-sloop-frame');
    let flute = document.getElementById('new-ship-flute-frame');

    // let frameElement = document.getElementById(id);

    if (id === 'new-captain-1-frame') {
        cap1.style.stroke = colour;
        cap2.style.removeProperty('stroke');
    }  else if (id === 'new-captain-2-frame') {
        cap2.style.stroke = colour;
        cap1.style.removeProperty('stroke');
    };

    if (id === 'new-ship-sloop-frame') {
        sloop.style.stroke = colour;
        flute.style.removeProperty('stroke');
    }  else if (id === 'new-ship-flute-frame') {
        flute.style.stroke = colour;
        sloop.style.removeProperty('stroke');
    };

    if ((cap1.style.stroke || cap2.style.stroke) && (sloop.style.stroke || flute.style.stroke)) {
        document.getElementById('new-captain-ship-get-text').style.fill = colour
        document.getElementById('new-captain-ship-get-text').setAttribute('onclick', 'sendToServerSelectedNewCaptainShip()');
    };
};


// SAVE DATA ON SERVER
function sendToServerSelectedNewCaptainShip() {

    let xhr = new XMLHttpRequest();

    xhr.open('POST', 'saveToServerSelectedNewCaptainShip', true);

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    let colour = (document.getElementById('new-player-main-rect')).style.stroke;
    let cap1 = document.getElementById('new-captain-1-frame');
    let cap2 = document.getElementById('new-captain-2-frame');
    let sloop = document.getElementById('new-ship-sloop-frame');
    let flute = document.getElementById('new-ship-flute-frame');

    let selectedCaptain = '';

    if (cap1.style.stroke) {
        selectedCaptain = cap1.getAttribute('name');
    } else if (cap2.style.stroke) {
        selectedCaptain = cap2.getAttribute('name');
    };

    let selectedShip = '';

    if (sloop.style.stroke) {
        selectedShip = 'sloop';
    } else if (flute.style.stroke) {
        selectedShip = 'flute';
    };

    document.getElementById('new-player-use').style.display = "None";

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.querySelector('.player-amount').innerHTML = response.amountPlayers;
            if (response.amountPlayers > 0) {
                document.querySelector('.nav-button-player-start').removeAttribute('disabled');
                document.querySelector('.nav-button-player-start').setAttribute('onclick', 'goGame()');
            };
        };
    };

    let data = 'colour=' + encodeURIComponent(colour) +
                '&selectedCaptain=' + encodeURIComponent(selectedCaptain) +
                '&selectedShip=' + encodeURIComponent(selectedShip);

    let addedBlock = document.querySelector(`.player-${colour}-added`);
    addedBlock.style.display = 'block';

    xhr.send(data);

};


