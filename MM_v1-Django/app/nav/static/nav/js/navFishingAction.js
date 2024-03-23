function navFishingAction(when) {

    if (when === 'get') {
        document.querySelector('.nav-button.nav-button-move-ship').disabled = true;
        document.querySelector('.nav-button.nav-button-scout').disabled = true;
        document.querySelector('.nav-button.nav-button-fishing').disabled = true;
        document.querySelector('.nav-button.nav-button-location').disabled = true;
        navEndTurnButton('getFishingAction');
    };

    if (when === 'post') {
        document.querySelector('.nav-button.nav-button-move-ship').disabled = false;
        document.querySelector('.nav-button.nav-button-scout').disabled = false;
        document.querySelector('.nav-button.nav-button-fishing').disabled = false;
        document.querySelector('.nav-button.nav-button-location').disabled = false;
        navEndTurnButton('postFishingAction');
    };

};