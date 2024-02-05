// BOARD
const boardContainer = document.getElementById('board-container');
const helperElementBoard = boardContainer.querySelector('.helper-board');
const tspansBoard = helperElementBoard.querySelectorAll('.tspan-board');
const allElementsBoard = boardContainer.querySelectorAll('[name]');
const polygons = boardContainer.querySelectorAll('polygon[name]');

boardContainer.addEventListener('mousemove', function(event) {
    var mouseX = parseInt(event.clientX - boardContainer.getBoundingClientRect().left);
    var mouseY = parseInt(event.clientY - boardContainer.getBoundingClientRect().top);
    tspansBoard.forEach(function(tspan, index) {
        tspan.setAttribute('x', mouseX + 5);
        tspan.setAttribute('y', mouseY  + 35 + index * 14);
    });
    tspansBoard[0].innerHTML = 'poz. ' + mouseX + ' ' + mouseY;
})

// WYŚWIETLENIE OKNA POMOCY DLA NAJECHANEGO ELEMENTU
boardContainer.addEventListener('mousemove', function (event) {
    if (['ellipse', 'circle', 'polygon', 'rect', 'use', 'path'].includes(event.target.tagName.toLowerCase())) {
        var name = event.target.getAttribute('name');
        tspansBoard[1].textContent = name;
    }
});
boardContainer.addEventListener('mouseout', function () {
    tspansBoard[1].textContent = '';
});






// PLAYER BOARD
const playerBoardContainer = document.getElementById('player-active-board-container');
const helperElementPlayerBoard = playerBoardContainer.querySelector('.helper-player-board');
const tspansPlayerBoard = helperElementPlayerBoard.querySelectorAll('.tspan-player-board');
const allElementsPlayerBoard = playerBoardContainer.querySelectorAll('[name]');
playerBoardContainer.addEventListener('mousemove', function(event) {
    var mouseX = parseInt(event.clientX - playerBoardContainer.getBoundingClientRect().left);
    var mouseY = parseInt(event.clientY - playerBoardContainer.getBoundingClientRect().top);
    tspansPlayerBoard.forEach(function(tspan, index) {
        tspan.setAttribute('x', mouseX + 5);
        tspan.setAttribute('y', mouseY  + 35 + index * 14);
    });
    tspansPlayerBoard[0].innerHTML = 'poz. ' + mouseX + ' ' + mouseY;
})

// WYŚWIETLENIE OKNA POMOCY DLA NAJECHANEGO ELEMENTU
playerBoardContainer.addEventListener('mousemove', function (event) {
    if (['ellipse', 'circle', 'polygon', 'rect', 'use', 'path'].includes(event.target.tagName.toLowerCase())) {
        var name = event.target.getAttribute('name');
        tspansPlayerBoard[1].textContent = name;
    }
});
playerBoardContainer.addEventListener('mouseout', function () {
    tspansPlayerBoard[1].textContent = '';
});

