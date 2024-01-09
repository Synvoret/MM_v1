// SHIP PLASTIC
function putShipPlastic(unit, colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let imageID = unit + "-" + colour + "-ship-plastic-image";
            document.getElementById(imageID).setAttribute('href', xhr.response);
            let unitID = document.getElementById("ship-plastic-" + colour)
            unitID.setAttribute('href', '#' + unit + "-" + colour +'-ship-plastic-image');
            unitID.setAttribute('x', "997");
            unitID.setAttribute('y', "510");	
        }
    };
    xhr.open('GET', 'ship?unit=' + unit + '&colour=' + colour, true);
    xhr.send();
};
