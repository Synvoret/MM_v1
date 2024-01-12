// Function inserts a selected element inside the second selected element, 
// trying not to exceed the edge of the second one with the edge of the first one.

function randomInsidePosition(unit, colour, localisation, port) {
    // GET EXTERNAL FIGURE (SeaZone, port or other), neccessary "localisation" argument
    var figureExternal = {};
    if (port) {
        figureExternal = document.getElementById(`${localisation}-port-zone`);
    } else {
        figureExternal = document.querySelector(`.${localisation}-zone`);
        console.log(document.querySelector(`.${localisation}-zone`))
    };

    // GET SHIP PLASTIC FROM board.html(only frontend)
    const shipPlasticRect = document.getElementById(`${unit}-ship-plastic-rect`);
    let shipPlasticRectWidth = parseInt(shipPlasticRect.getAttribute('width'), 10);
    let shipPlasticRectHeight = parseInt(shipPlasticRect.getAttribute('height'), 10);
    let posX = getRandomInt(figureExternal.getBBox().x, figureExternal.getBBox().x + figureExternal.getBBox().width - shipPlasticRectWidth);
    let posY = getRandomInt(figureExternal.getBBox().y, figureExternal.getBBox().y + figureExternal.getBBox().height - shipPlasticRectHeight);

    // GET SHIP PLASTIC USE FROM board.html(only frontend)
    const shipPlasticUse = document.getElementById(`ship-plastic-${colour}`);
    shipPlasticUse.setAttribute("x", posX);
    shipPlasticUse.setAttribute("y", posY);

    // function to generate random integer number in scope
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    };

    // console.log(unit, colour, localisation);

    // CREATE RANDOMLY CIRCLE
    // let r = 35
    // let circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    // circle.setAttribute("class", "ship-plastic");
    // circle.setAttribute("r", r);
    // circle.setAttribute("fill", "blue");
    // var circleX = getRandomInt(figureExternal.getBBox().x + r, figureExternal.getBBox().x + figureExternal.getBBox().width - r);
    // var circleY = getRandomInt(figureExternal.getBBox().y + r, figureExternal.getBBox().y + figureExternal.getBBox().height - r);
    // circle.setAttribute("cx", circleX);
    // circle.setAttribute("cy", circleY);
    // figureExternal.parentNode.appendChild(circle);

    // CREATE RANDOMLY RECTANGLE
    // let width = 80;
    // let height = 60;
    // let rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    // rect.setAttribute("class", "ship-plastic");
    // rect.setAttribute("width", width);
    // rect.setAttribute("height", height);
    // rect.setAttribute("fill", "blue");
    // var rectX = getRandomInt(figureExternal.getBBox().x + width, figureExternal.getBBox().x + figureExternal.getBBox().width - width);
    // var rectY = getRandomInt(figureExternal.getBBox().y + height, figureExternal.getBBox().y + figureExternal.getBBox().height - height);
    // rect.setAttribute("x", rectX);
    // rect.setAttribute("y", rectY);
    // figureExternal.parentNode.appendChild(rect);

};
