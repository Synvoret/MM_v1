function navSendToServerSelectedNewCaptainShip() {
    document.querySelector('.nav-button-player-start').removeAttribute('disabled');
    document.querySelector('.nav-button-player-start').setAttribute('onclick', 'goGame()');
}