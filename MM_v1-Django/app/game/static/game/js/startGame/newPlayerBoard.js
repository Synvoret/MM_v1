// NEW PLAYER BOARD
function newPlayerBoard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('player-board-blue').setAttribute('href', xhr.response);
        }
    };
    xhr.open('GET', 'player_board', true);
    xhr.send();
};


