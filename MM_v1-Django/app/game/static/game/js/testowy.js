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
const playerBoardContainer = document.getElementById('player-board-container');
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





































// GRAB AND MOVE SHIPs
function enableDrag(element) {
    let isDragging = false;
    let offset = { x: 0, y: 0 };

    element.addEventListener("mousedown", function (e) {
        isDragging = true;

        // Calculate the offset of the mouse click relative to the element's position
        offset.x = e.clientX - element.getAttribute("x");
        offset.y = e.clientY - element.getAttribute("y");
        });

        document.addEventListener("mousemove", function (e) {
        if (!isDragging) return;

        // Update the element's position based on the mouse movement
        const newX = e.clientX - offset.x;
        const newY = e.clientY - offset.y;

        element.setAttribute("x", newX);
        element.setAttribute("y", newY);
        });

        document.addEventListener("mouseup", function () {
        isDragging = false;
        });
    }

    // Get all SVG elements with 'use' tag
    const svgElements = document.querySelectorAll(".player-ship-plastic");
    // Enable drag for each SVG element
    svgElements.forEach(enableDrag);
