function updatePlayerCargoCards(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            for (let i = 1; i <= 8; i++) {
                if (response.hasOwnProperty(`cargoCard${i}Image`)) {
                    let cargoCardImageURL = response[`cargoCard${i}Image`];
                    document.getElementById(`player-cargo-card-${i}-image`).setAttribute('href', cargoCardImageURL);
                    document.getElementById(`player-cargo-card-use-${i}`).setAttribute('href', `#player-cargo-card-${i}-image`);
                };
            };

        };
    };

    // cleanning cargo cards
    let cargoCards = document.querySelectorAll('use[id^="' + "player-cargo-card-use" + '"]');
    for (let element of cargoCards) {
        element.setAttribute("href", "");
    };


    xhr.open('GET', 'updatePlayerCargoCards?colour=' + colour, true);
    xhr.send();
};
