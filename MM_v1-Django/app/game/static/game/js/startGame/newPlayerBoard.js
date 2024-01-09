// NEW PLAYER BOARD
function newPlayerBoard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('player-board-blue').setAttribute('href', xhr.response);
        }
    };
    xhr.open('GET', 'player_board', true);
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
};
