// DRAW ONE EVENT CARD
function drawEventCard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            const demandTokenIDImage = "event-card-image"
            document.getElementById(demandTokenIDImage).setAttribute('href', response.eventCardImage)

            if (response.function1 && response.arg1) {
                window[response.function1](response.arg1)
            };
        }
    };
    xhr.open('GET', 'drawEventCard', true);
    xhr.send();
};
