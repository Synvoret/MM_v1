function endCurrentAction(colour) {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            console.log(response)
            if (response.nextPlayer) {
                startPlayerActions();
                console.log('NASTĘPNY GRACZ IF EXIST')
                return;
            };
            document.getElementById('captain-actions-image').setAttribute('href', response.cubeImage);
            if (response.currentAction !== undefined) {
                document.getElementById(`captain-actions-${response.currentAction}`).setAttribute('href', '#captain-actions-image');
            };
        };
    };
    xhr.open('GET', 'endCurrentAction?colour=' + colour, true);
    xhr.send();

};



