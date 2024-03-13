function startRound() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            navStartRound();

            document.getElementById("player-active-board-container").style.display = 'none';

        };
    };
    xhr.open('POST', 'startRound', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();

};
