// Function inserts a selected element inside the second selected element, 
// trying not to exceed the edge of the second one with the edge of the first one.

function randomInsidePosition(unit, colour, localisation, port) {
    // GET EXTERNAL FIGURE (SeaZone, port or other), neccessary "localisation" argument
    var figureExternal = {};
    if (port) {
        figureExternal = document.getElementById(`${localisation}-port-zone`);
    } else {
        figureExternal = document.querySelector(`.${localisation}-zone`);
    };

    // GET SHIP PLASTIC FROM board.html(only frontend)
    // console.log(`${unit}-ship-plastic-rect`, localisation)
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

};
