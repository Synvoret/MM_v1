// NEW PLAYER BOARD
function newPlayerBoard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('player-board-blue').setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'player_board', true);
    xhr.send();
};







// PLAYER HIT LOCATIONs, PUT CUBEs
function playerHitLocation(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('player-hit-location-image').setAttribute('href', response.cubeImage);
            let hull = response.hullHit;
            let cargo = response.cargoHit;
            let masts = response.mastsHit;
            let crew = response.crewHit;
            let cannons = response.cannonsHit;
            document.getElementById('hull-' + hull + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('cargo-' + cargo + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('masts-' + masts + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('crew-' + crew + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
            document.getElementById('cannons-' + cannons + '-player-hit-location').setAttribute('href', '#player-hit-location-image');
        }
    };
    xhr.open('GET', 'playerHitLocation?colour=' + colour, true);
    xhr.send();
};

// AMOUNT PLAYER GOLDs
function playerGolds(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('coin-image').setAttribute('href', response.coinImage);
            document.getElementById('player-coin-amount').textContent = response.amountGolds;
        }
    };
    xhr.open('GET', 'playerGoldsTrack?colour=' + colour, true);
    xhr.send();
};
























// Pobierz element polygon
var polygon = document.querySelector('polygon[name="sea-zone-basse-terre"]');

// Stwórz okrąg
var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
circle.setAttribute("r", "10");
circle.setAttribute("fill", "red"); // Możesz dostosować kolor wypełnienia
circle.setAttribute("cx", getRandomInt(polygon.getBBox().x, polygon.getBBox().x + polygon.getBBox().width));
circle.setAttribute("cy", getRandomInt(polygon.getBBox().y, polygon.getBBox().y + polygon.getBBox().height));

// Dodaj okrąg do polygonu
polygon.parentNode.appendChild(circle);

// Funkcja do generowania losowej liczby całkowitej w zadanym zakresie
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}