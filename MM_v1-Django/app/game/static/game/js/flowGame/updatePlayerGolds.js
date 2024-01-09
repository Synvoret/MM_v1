// UPDATE PLAYER GOLDs
function updatePlayerGolds(colour, kol) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('coin-image').setAttribute('href', response.coinImage);
            document.getElementById('player-coin-amount').textContent = response.amountGolds;
            document.getElementById('player-coin-amount').setAttribute('stroke', colour);
        }
    };
    xhr.open('GET', 'updatePlayerGolds?colour=' + colour, true);
    xhr.send();
};
