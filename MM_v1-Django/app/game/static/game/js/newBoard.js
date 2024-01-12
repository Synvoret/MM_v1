// NEW BOARD
function newBoard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('board-game').setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'board', true);
    xhr.send();
};

// DRAW ONE EVENT CARD
function newEventCard(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'drawEventCard', true);
    xhr.send();
};

// DRAW RANDOMLY DEMAND TOKEN
function drawDemandToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'drawDemandToken', true);
    xhr.send();
}

// DRAW RANDOMLY SHIP MODIFICATION TOKEN
function drawShipModification(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'drawShipModification', true);
    xhr.send();
}

// DRAW RANDOMLY MERCHANT TOKEN
function drawMerchantToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'drawMerchantToken', true);
    xhr.send();
}

// PUT CUBEs on TRACK GLORY POINTs
function gloryTrackCube(id, colour, point) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', "gloryTrackCube?colour=" + colour, true);
    xhr.send();
}

// PUT CUBEs on TRACK ENEMY HIT LOCATIONs
function enemyHitLocation(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', "enemyHitLocation", true);
    xhr.send();
}

// PUT LOCATION TOKENs
function putLocationToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', "putLocationToken", true);
    xhr.send();
}

// NEW BOARD
newBoard();
newEventCard('event-card-image')
// STARTING DRAW DEMAND TOKENs
drawDemandToken("demand-basse-terre-image")
drawDemandToken("demand-bridgetown-image")
drawDemandToken("demand-caracas-image")
drawDemandToken("demand-cartagena-image")
drawDemandToken("demand-curacao-image")
drawDemandToken("demand-nassau-image")
drawDemandToken("demand-havana-image")
drawDemandToken("demand-old-providence-image")
drawDemandToken("demand-petite-goave-image")
drawDemandToken("demand-port-royal-image")
drawDemandToken("demand-san-juan-image")
drawDemandToken("demand-santo-domingo-image")
drawDemandToken("demand-st-john-image")
drawDemandToken("demand-st-maarten-image")
drawDemandToken("demand-trinidad-image")
drawDemandToken("demand-tortuga-image")
// STARTING DRAW SHIP MODIFICATIONs
drawShipModification("ship-modification-basse-terre-image")
drawShipModification("ship-modification-bridgetown-image")
drawShipModification("ship-modification-caracas-image")
drawShipModification("ship-modification-cartagena-image")
drawShipModification("ship-modification-curacao-image")
drawShipModification("ship-modification-nassau-image")
drawShipModification("ship-modification-havana-image")
drawShipModification("ship-modification-old-providence-image")
drawShipModification("ship-modification-petite-goave-image")
drawShipModification("ship-modification-port-royal-image")
drawShipModification("ship-modification-san-juan-image")
drawShipModification("ship-modification-santo-domingo-image")
drawShipModification("ship-modification-st-john-image")
drawShipModification("ship-modification-st-maarten-image")
drawShipModification("ship-modification-trinidad-image")
drawShipModification("ship-modification-tortuga-image")
// STARTING DRAW MERCHANT TOKENs
drawMerchantToken("merchant-token-basse-terre-image")
drawMerchantToken("merchant-token-bridgetown-image")
drawMerchantToken("merchant-token-caracas-image")
drawMerchantToken("merchant-token-cartagena-image")
drawMerchantToken("merchant-token-curacao-image")
drawMerchantToken("merchant-token-nassau-image")
drawMerchantToken("merchant-token-havana-image")
drawMerchantToken("merchant-token-old-providence-image")
drawMerchantToken("merchant-token-petite-goave-image")
drawMerchantToken("merchant-token-port-royal-image")
drawMerchantToken("merchant-token-san-juan-image")
drawMerchantToken("merchant-token-santo-domingo-image")
drawMerchantToken("merchant-token-st-john-image")
drawMerchantToken("merchant-token-st-maarten-image")
drawMerchantToken("merchant-token-the-caribbean-sea-image")
drawMerchantToken("merchant-token-trinidad-image")
drawMerchantToken("merchant-token-tortuga-image")
// PUT CUBEs ON TRACK GLORY POINTs
gloryTrackCube('blue-cube-image', 'blue')
gloryTrackCube('green-cube-image', 'green')
gloryTrackCube('red-cube-image', 'red')
gloryTrackCube('yellow-cube-image', 'yellow')
// PUT CUBEs ON TRACK ENEMY HIT LOCATIONs
enemyHitLocation('brown-cube-enemy-hit-location-image')
// PUT LOCATION TOKENs
putLocationToken('location-token-basse-terre-image')
putLocationToken('location-token-bridgetown-image')
putLocationToken('location-token-caracas-image')
putLocationToken('location-token-cartagena-image')
putLocationToken('location-token-curacao-image')
putLocationToken('location-token-havana-image')
putLocationToken('location-token-nassau-image')
putLocationToken('location-token-old-providence-image')
putLocationToken('location-token-petite-goave-image')
putLocationToken('location-token-port-royal-image')
putLocationToken('location-token-san-juan-image')
putLocationToken('location-token-santo-domingo-image')
putLocationToken('location-token-st-john-image')
putLocationToken('location-token-st-maarten-image')
putLocationToken('location-token-trinidad-image')
putLocationToken('location-token-tortuga-image')































const xxx = document.getElementById('eventCard');
let isDragging = false;
let offsetX, offsetY;
xxx.addEventListener('mousedown', (e) => {
    if (e.target === xxx) {
        isDragging = true;
        offsetX = e.clientX - xxx.getBoundingClientRect().left;
        offsetY = e.clientY - xxx.getBoundingClientRect().top;
    }
});
document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    var mouseX = parseInt(e.clientX - boardContainer.getBoundingClientRect().left);
    var mouseY = parseInt(e.clientY - boardContainer.getBoundingClientRect().top);
    xxx.setAttribute('x', mouseX);
    xxx.setAttribute('y', mouseY);
});
document.addEventListener('mouseup', () => {
    isDragging = false;
});






('board-game', 'board')