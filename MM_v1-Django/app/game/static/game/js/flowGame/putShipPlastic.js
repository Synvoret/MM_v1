// SHIP PLASTIC
function putShipPlastic(unit, colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let imageID = unit + "-" + colour + "-ship-plastic-image";
            document.getElementById(imageID).setAttribute('href', xhr.response);
            let unitID = "ship-plastic-" + colour;
            document.getElementById(unitID).setAttribute('href', '#' + unit + "-" + colour +'-ship-plastic-image');
        }
    };
    xhr.open('GET', 'ship?unit=' + unit + '&colour=' + colour, true);
    xhr.send();
};