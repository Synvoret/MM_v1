// DRAW ONE EVENT CARD
function newEventCard(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'drawEventCard', true);
    xhr.send();
};