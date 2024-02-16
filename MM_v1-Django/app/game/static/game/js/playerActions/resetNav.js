function resetNav(when) {

    if (when == 'after all actions') {
        document.querySelector(".step.player-actions").innerHTML = 'Player Actions';
        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-moves-buttons").style.display = 'none';
        document.querySelector(".nav-directions-buttons").style.display = 'none';
        document.querySelector(".nav-scouting-buttons").style.display = 'none';
        document.querySelector(".nav-port-buttons").style.display = 'none';

        document.querySelector(".nav-button.nav-button-move-ship").disabled = true;
        document.querySelector(".nav-button.nav-button-scout").disabled = true;
        document.querySelector(".nav-button.nav-button-port").disabled = true;
        document.querySelector(".nav-button.nav-button-fishing").disabled = true;
        document.querySelector(".nav-button.nav-button-location").disabled = true;

        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
    };


    if (when === 'during actions') {
        console.log('KONIEC RUNDY W TRTAKCIE AKKCJI')
        document.querySelector(".step.player-actions").innerHTML = 'Player Actions';
        document.querySelector(".nav-actions-buttons").style.display = '';
        document.querySelector(".nav-moves-buttons").style.display = 'none';
        document.querySelector(".nav-directions-buttons").style.display = 'none';
        document.querySelector(".nav-scouting-buttons").style.display = 'none';
        document.querySelector(".nav-port-buttons").style.display = 'none';

        // document.querySelector(".nav-button.nav-button-move-ship").disabled = false;
        // document.querySelector(".nav-button.nav-button-scout").disabled = false;
        // document.querySelector(".nav-button.nav-button-port").disabled = false;
        // document.querySelector(".nav-button.nav-button-fishing").disabled = false;
        // document.querySelector(".nav-button.nav-button-location").disabled = false;

        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
    }

};
