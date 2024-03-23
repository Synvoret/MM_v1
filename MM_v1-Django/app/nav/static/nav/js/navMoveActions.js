function navMoveActions(when) {

    // moves
    if (when === 'moves') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.querySelector(".step.nav-player-actions").innerHTML = 'Select Destination'
                document.querySelector('.nav-actions-buttons').style.display = 'none';
                document.querySelector('.nav-moves-buttons').style.display = '';
                if (response.playerInPort) {
                    document.querySelector(".nav-button.nav-button-to-port").disabled = true;
                    document.querySelector(".nav-button.nav-button-from-port").disabled = false;
                    document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;
                } else {
                    if (response.isInTheCaribbeanSea) {
                        document.querySelector(".nav-button.nav-button-to-port").disabled = true;
                    } else {
                        document.querySelector(".nav-button.nav-button-to-port").disabled = false;
                    };
                    document.querySelector(".nav-button.nav-button-from-port").disabled = true;
                    document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = false;
                };
                document.querySelector(".nav-button.nav-button-back").disabled = false;
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "moveAction('back')");
            };
        };
        xhr.open('GET', 'navMoveActions?when=' + when, true);
        xhr.send();
    };

    // to port
    if (when === 'to port') {
        document.querySelector(".nav-button.nav-button-to-port").style.display = '';
            document.querySelector(".nav-button.nav-button-to-port").disabled = true;
            document.querySelector(".nav-button.nav-button-from-port").style.display = '';
            document.querySelector(".nav-button.nav-button-from-port").disabled = false;
            document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
            document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;
            document.querySelector(".nav-button.nav-button-back").disabled = false;
    };

    // from port
    if (when === 'from port') {
        document.querySelector(".nav-button.nav-button-to-port").style.display = '';
        document.querySelector(".nav-button.nav-button-to-port").disabled = false;
        document.querySelector(".nav-button.nav-button-from-port").style.display = '';
        document.querySelector(".nav-button.nav-button-from-port").disabled = true;
        document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
        document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = false;
        document.querySelector(".nav-button.nav-button-back").disabled = false;
    };

    // to sea zone
    if (when === 'to sea zone') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.querySelector(".nav-moves-buttons").style.display = 'none';
                document.querySelector(".nav-directions-buttons").style.display = '';

                if (response.n !== undefined) {
                    document.querySelector(".nav-button.nav-button-n-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-n-direction").innerHTML = `N - ${response.n}`;
                    document.querySelector(".nav-button.nav-button-n-direction").setAttribute('onclick', `moveAction('${response.n}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-n-direction").style.display = 'none';
                };
                if (response.ne !== undefined) {
                    document.querySelector(".nav-button.nav-button-ne-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-ne-direction").innerHTML = `NE - ${response.ne}`;
                    document.querySelector(".nav-button.nav-button-ne-direction").setAttribute('onclick', `moveAction('${response.ne}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-ne-direction").style.display = 'none';
                };
                if (response.e !== undefined) {
                    document.querySelector(".nav-button.nav-button-e-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-e-direction").innerHTML = `E - ${response.e}`;
                    document.querySelector(".nav-button.nav-button-e-direction").setAttribute('onclick', `moveAction('${response.e}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-e-direction").style.display = 'none';
                };
                if (response.se !== undefined) {
                    document.querySelector(".nav-button.nav-button-se-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-se-direction").innerHTML = `SE - ${response.se}`;
                    document.querySelector(".nav-button.nav-button-se-direction").setAttribute('onclick', `moveAction('${response.se}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-se-direction").style.display = 'none';
                };
                if (response.s !== undefined) {
                    document.querySelector(".nav-button.nav-button-s-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-s-direction").innerHTML = `S - ${response.s}`;
                    document.querySelector(".nav-button.nav-button-s-direction").setAttribute('onclick', `moveAction('${response.s}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-s-direction").style.display = 'none';
                };
                if (response.sw !== undefined) {
                    document.querySelector(".nav-button.nav-button-sw-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-sw-direction").innerHTML = `SW - ${response.sw}`;
                    document.querySelector(".nav-button.nav-button-sw-direction").setAttribute('onclick', `moveAction('${response.sw}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-sw-direction").style.display = 'none';
                };
                if (response.w !== undefined) {
                    document.querySelector(".nav-button.nav-button-w-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-w-direction").innerHTML = `W - ${response.w}`;
                    document.querySelector(".nav-button.nav-button-w-direction").setAttribute('onclick', `moveAction('${response.w}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-w-direction").style.display = 'none';
                };
                if (response.nw !== undefined) {
                    document.querySelector(".nav-button.nav-button-nw-direction").style.display = '';
                    document.querySelector(".nav-button.nav-button-nw-direction").innerHTML = `NW - ${response.nw}`;
                    document.querySelector(".nav-button.nav-button-nw-direction").setAttribute('onclick', `moveAction('${response.nw}')`);
                } else {
                    document.querySelector(".nav-button.nav-button-nw-direction").style.display = 'none';
                };

                document.querySelector(".nav-button.nav-button-back").disabled = false;

            };
        };
        xhr.open('POST', 'navMoveActions', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'when=' + encodeURIComponent(when);
        xhr.send(data);
    };

    // back
    if (when === 'back') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour
                // console.log(response)
                document.querySelector('.nav-actions-buttons').style.display = '';
                document.querySelector('.nav-moves-buttons').style.display = 'none';
                document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions'
                document.querySelector('.nav-directions-buttons').style.display = 'none';
                if (response.playerInPort) {
                    document.querySelector('.nav-button.nav-button-scout').disabled = true;
                    document.querySelector('.nav-button.nav-button-port').disabled = false;
                    document.querySelector('.nav-button.nav-button-fishing').disabled = true;
                    document.querySelector('.nav-button.nav-button-location').disabled = true;
                } else {
                    document.querySelector('.nav-button.nav-button-scout').disabled = false;
                    document.querySelector('.nav-button.nav-button-port').disabled = true;
                    document.querySelector('.nav-button.nav-button-fishing').disabled = false;
                    if (response.isInTheCaribbeanSea) {
                        document.querySelector('.nav-button.nav-button-location').disabled = true;
                    } else {
                        document.querySelector('.nav-button.nav-button-location').disabled = false;
                    }
                    document.querySelector('.nav-button.nav-button-stash-gold').disabled = true;
                };

                document.querySelector(".nav-button.nav-button-move-ship").disabled = false;
                document.querySelector(".nav-button.nav-button-back").disabled = true;

            };
        };
        xhr.open('GET', 'navMoveActions?when=' + when, true);
        xhr.send();
    }
}