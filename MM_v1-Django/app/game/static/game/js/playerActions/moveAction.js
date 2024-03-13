// MOVE ACTIONs - consume one action point
function moveAction(type_request) {


    if (type_request === 'moves') {
        navMoveActions(type_request);
    };


    if (type_request === 'to port') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, true);
                navMoveActions(type_request);
                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'moveAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'from port') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, false);
                navMoveActions(type_request);
                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'moveAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'to sea zone') {
        navMoveActions(type_request);
    };


    const allowedDestinations = [
        'Basse-Terre',
        'Bridgetown',
        'Caracas',
        'Cartagena',
        'Curacao',
        'Gulf City',
        'Havana',
        'Nassau',
        'Old Providence',
        'Petite Goave',
        'Port Royal',
        'San Juan',
        'Santo Domingo',
        'St John',
        'St Maarten',
        'The Caribbean Sea',
        'Tortuga',
        'Trinidad',
    ];
    if (allowedDestinations.includes(type_request)) {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;

                randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, false)

                if (response.lastAction === undefined) {
                    moveAction('to sea zone');
                };

                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'moveAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let data = 'type_request=' + encodeURIComponent(type_request);
        xhr.send(data);
    };


    if (type_request === 'back') {
        navMoveActions(type_request);
    };

};
