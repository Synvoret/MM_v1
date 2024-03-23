function navEndTurnButton(when) {

    // 'get' from fishing action
    if (when === 'getFishingAction') {
        document.querySelector('.nav-button.nav-button-end-turn').disabled = true;
    };

    // 'post' from fishing action
    if (when === 'postFishingAction') {
        document.querySelector('.nav-button.nav-button-end-turn').disabled = false;
    };

};
