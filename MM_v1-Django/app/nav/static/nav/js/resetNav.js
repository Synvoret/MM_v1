function resetNav(when) {

    if (when == 'after all actions') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions';
                document.querySelector(".nav-actions-buttons").style.display = '';
                document.querySelector(".nav-moves-buttons").style.display = 'none';
                document.querySelector(".nav-directions-buttons").style.display = 'none';
                document.querySelector(".nav-scouting-buttons").style.display = 'none';
                document.querySelector(".nav-port-buttons").style.display = 'none';
                document.querySelector(".nav-location-buttons").style.display = 'none';

                document.querySelector(".nav-button.nav-button-move-ship").disabled = true;
                document.querySelector(".nav-button.nav-button-scout").disabled = true;
                document.querySelector(".nav-button.nav-button-port").disabled = true;
                document.querySelector(".nav-button.nav-button-fishing").disabled = true;
                document.querySelector(".nav-button.nav-button-location").disabled = true;

                document.querySelector(".nav-button.nav-button-back").disabled = true;
                document.querySelector('.nav-button.nav-button-end-turn').disabled = false;

            };
        };
        xhr.open('GET', 'resetNav?when=' + when, true);
        xhr.send();
    };


    if (when === 'during actions') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions';
                document.querySelector(".nav-actions-buttons").style.display = '';
                document.querySelector(".nav-moves-buttons").style.display = 'none';
                document.querySelector(".nav-directions-buttons").style.display = 'none';
                document.querySelector(".nav-scouting-buttons").style.display = 'none';
                document.querySelector(".nav-port-buttons").style.display = 'none';
                document.querySelector(".nav-shipyard-buttons").style.display = 'none';
                document.querySelector(".nav-location-buttons").style.display = 'none';


                // Scout button
                // Port button
                if (response.playerInPort) {
                    document.querySelector(".nav-button.nav-button-scout").disabled = true;
                    document.querySelector(".nav-button.nav-button-port").disabled = false;
                    document.querySelector(".nav-button.nav-button-fishing").disabled = true;
                    document.querySelector(".nav-button.nav-button-location").disabled = true;
                } else {
                    document.querySelector(".nav-button.nav-button-scout").disabled = false;
                    document.querySelector(".nav-button.nav-button-port").disabled = true;
                    // Fishing button
                    if (response.playerHaveDestroyedHitLocation) {
                        document.querySelector(".nav-button.nav-button-fishing").disabled = true;
                    } else {
                        document.querySelector(".nav-button.nav-button-fishing").disabled = false;
                    };
                    // Visit Location button
                    document.querySelector(".nav-button.nav-button-location").disabled = false;
                };

                document.querySelector(".nav-button.nav-button-back").disabled = true;
                document.querySelector('.nav-button.nav-button-end-turn').disabled = false;

            };
        };
        xhr.open('GET', 'resetNav?when=' + when, true);
        xhr.send();

    }

};
