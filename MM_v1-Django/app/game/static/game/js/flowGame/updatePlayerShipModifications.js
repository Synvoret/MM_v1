// SPECIAL WEAPON TRACK, PUT IMAGE on PLAYER BOARD
function updatePlayerShipModifications(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            for (let modification in response) {
                if (response.hasOwnProperty(modification)) {
                    let imageURL = response[modification];
                    document.getElementById(`player-ship-modification-${modification}`).setAttribute('href', imageURL);
                };
            };

        };
    };

    // cleanning elements
    let shipModificationElements = document.querySelectorAll('image[id^="' + "player-ship-modification" + '"]');
    for (let element of shipModificationElements) {
        element.setAttribute("href", "");
    };

    xhr.open('GET', 'updatePlayerShipModifications?colour=' + colour, true);
    xhr.send();
};