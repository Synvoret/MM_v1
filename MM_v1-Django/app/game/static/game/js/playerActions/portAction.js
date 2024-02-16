function portAction(type_request) {


    if (type_request === 'port') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                console.log(response)

                document.querySelector(".step.player-actions").innerHTML = 'Port Actions';
                document.querySelector(".nav-actions-buttons").style.display = 'none';
                document.querySelector(".nav-port-buttons").style.display = '';

                document.querySelector(".nav-button.nav-button-sell-goods").style.display = '';
                document.querySelector(".nav-button.nav-button-buy-goods").style.display = '';
                document.querySelector(".nav-button.nav-button-visit-shipyard").style.display = '';
                document.querySelector(".nav-button.nav-button-reqruit").style.display = '';
                document.querySelector(".nav-button.nav-button-acquire-rumor").style.display = '';
                document.querySelector(".nav-button.nav-button-claim-mission").style.display = '';
                document.querySelector(".nav-button.nav-button-stash-gold").style.display = '';
                document.querySelector(".nav-button.nav-button-gain-loyality").style.display = '';
                document.querySelector(".nav-button.nav-button-get-favour").style.display = '';

                document.querySelector(".nav-button.nav-button-back").disabled = false;
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "portAction('back')")
            };
        };
        xhr.open('GET', 'portAction?type_request=' + type_request, true);
        xhr.send();
    };



    if (type_request === 'visit shipyard') {
        document.querySelector(".step.player-actions").innerHTML = 'Port Shipyard';
        document.querySelector(".nav-port-buttons").style.display = 'none';
        document.querySelector(".nav-shipyard-buttons").style.display = '';
    };



    if (type_request === 'back') {
        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-port-buttons").style.display = 'none';
        document.querySelector(".nav-shipyard-buttons").style.display = 'none';
        document.querySelector(".step.player-actions").innerHTML = 'Player Actions';
        document.querySelector(".nav-button.nav-button-back").disabled = true;
    };

};
