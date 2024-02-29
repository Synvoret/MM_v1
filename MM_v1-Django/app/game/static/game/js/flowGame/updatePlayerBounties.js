function updatePlayerBounties(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            // cleanning all use
            for (let i = 1; i <= 5; i++) {
                for (let j = 1; j <= 6; j++) {
                    document.getElementById(`player-bounty-${i}-${j}`).setAttribute('href', '');
                };
            };

            if (response.Dutch > 0) {
                document.getElementById(`player-bounty-dutch-image`).setAttribute('href', response.DutchImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.Dutch}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.Dutch}-${i}`).setAttribute('href', `#player-bounty-dutch-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-dutch-image`).setAttribute('href', '');
            };

            if (response.English > 0) {
                document.getElementById(`player-bounty-english-image`).setAttribute('href', response.EnglishImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.English}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.English}-${i}`).setAttribute('href', `#player-bounty-english-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-english-image`).setAttribute('href', '');
            };

            if (response.French > 0) {
                document.getElementById(`player-bounty-french-image`).setAttribute('href', response.FrenchImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.French}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.French}-${i}`).setAttribute('href', `#player-bounty-french-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-french-image`).setAttribute('href', '');
            };

            if (response.Spanish > 0) {
                document.getElementById(`player-bounty-spanish-image`).setAttribute('href', response.SpanishImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.Spanish}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.Spanish}-${i}`).setAttribute('href', `#player-bounty-spanish-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-spanish-image`).setAttribute('href', '');
            };

            if (response.SmallPirate > 0) {
                document.getElementById(`player-bounty-small-pirate-image`).setAttribute('href', response.SmallPirateImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.SmallPirate}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.SmallPirate}-${i}`).setAttribute('href', `#player-bounty-small-pirate-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-small-pirate-image`).setAttribute('href', '');
            };

            if (response.LargePirate > 0) {
                document.getElementById(`player-bounty-large-pirate-image`).setAttribute('href', response.LargePirateImage);
                for (let i = 1; i <= 6; i++) {
                    if (document.getElementById(`player-bounty-${response.LargePirate}-${i}`).getAttribute('href') === '') {
                        document.getElementById(`player-bounty-${response.LargePirate}-${i}`).setAttribute('href', `#player-bounty-large-pirate-image`);
                        break;
                    };
                };
            } else {
                document.getElementById(`player-bounty-large-pirate-image`).setAttribute('href', '');
            };

        };
    };
    xhr.open('GET', 'updatePlayerBounties?colour=' + colour, true);
    xhr.send();
};

