function navLocationActions(when) {

    // location
    if (when === 'location') {
        document.querySelector('.nav-actions-buttons').style.display = 'none';
        document.querySelector('.nav-location-buttons').style.display = '';
        document.querySelector(".step.nav-player-actions").innerHTML = 'Location Actions';

        document.querySelector(".nav-button.nav-button-back").disabled = false;
        document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "locationAction('back')");
    };

    // back
    if (when === 'back') {
        document.querySelector('.nav-actions-buttons').style.display = '';
        document.querySelector('.nav-location-buttons').style.display = 'none';
        document.querySelector(".step.nav-player-actions").innerHTML = 'Player Actions';

        document.querySelector(".nav-button.nav-button-back").disabled = true;
    };

};
