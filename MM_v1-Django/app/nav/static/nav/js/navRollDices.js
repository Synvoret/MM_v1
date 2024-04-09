function navRollDices(when, amountActions=false) {

    if (when === 'testOk' && amountActions === true) {
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    } else if (when === 'testOk' && amountActions === false) {
        document.querySelector(".nav-button.nav-button-back").disabled = false;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    };

    // let amountActions = true
    if (when === 'testCancel' && amountActions === true) {
        document.querySelector(".nav-button.nav-button-back").disabled = true;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    } else if (when === 'testCancel' && amountActions === false) {
        document.querySelector(".nav-button.nav-button-back").disabled = false;
        document.querySelector(".nav-button.nav-button-end-turn").disabled = false;
    }

};
