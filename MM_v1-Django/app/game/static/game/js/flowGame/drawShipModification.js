// DRAW RANDOMLY SHIP MODIFICATION TOKEN
function drawShipModification(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response);
        }
    };
    xhr.open('GET', 'drawShipModification', true);
    xhr.send();
};