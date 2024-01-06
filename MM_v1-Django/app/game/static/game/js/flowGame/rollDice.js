// ROLL DICE
function rollDice(cl) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.querySelector(cl).setAttribute('src', response.diceImage);
        }
    };
    xhr.open('GET', 'dice', true);
    xhr.send();
};
