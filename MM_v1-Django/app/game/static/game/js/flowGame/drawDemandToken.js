// DRAW RANDOMLY DEMAND TOKEN
function drawDemandToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response);
        }
    };
    xhr.open('GET', 'drawDemandToken', true);
    xhr.send();
};