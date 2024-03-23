function startPlayerTurn() {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            let colour = response.playerColour
            navStartPlayerTurn();
            playerBoard(colour);
        };
        
    };
    xhr.open('GET', 'startPlayerTurn', true);
    xhr.send();
};
