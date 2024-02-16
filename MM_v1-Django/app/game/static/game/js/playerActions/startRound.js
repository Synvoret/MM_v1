function startRound() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('draw-event-card-div').style.display = "block";
            document.getElementById('player-action-div').style.display = 'none';
            document.getElementById("player-active-board-container").style.display = 'none';

            document.querySelector(".title-value-player-blue").innerHTML = '';
            document.querySelector(".title-value-player-green").innerHTML = '';
            document.querySelector(".title-value-player-red").innerHTML = '';
            document.querySelector(".title-value-player-yellow").innerHTML = '';
        };
    };
    xhr.open('POST', 'startRound', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    // let data = 'colour=' + encodeURIComponent(colour);
    // xhr.send(data);
    xhr.send();

};
