function updateCaptainActions(colour) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            console.log(response);
            let amountActions = response.amountActions;
            if (response.nextPlayer) {
                playerBoard();
                console.log('NASTĘPNY GRACZ IF EXIST')
                return
            };
            document.getElementById('captain-actions-image').setAttribute('href', response.cubeImage);
            document.getElementById('captain-actions-first').setAttribute('href', '#captain-actions-image');
            };
        };
    xhr.open('GET', 'updateCaptainActions?colour=' + colour, true);
    xhr.send();

};
