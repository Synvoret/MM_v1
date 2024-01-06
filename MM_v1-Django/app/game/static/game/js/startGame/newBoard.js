// NEW BOARD
function newBoard() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('board-game').setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', 'board', true);
    xhr.send();
};
