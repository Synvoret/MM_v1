// SCOUT ACTIONs - consume one action
function scoutAction(type_request) {


    if (type_request === 'scout') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                document.querySelector(".nav-button.nav-button-scout-merchant").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-dutch-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-english-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-french-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-spanish-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-small-pirate-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-large-pirate-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-blue-player-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-green-player-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-red-player-ship").style.display = '';
                document.querySelector(".nav-button.nav-button-scout-yellow-player-ship").style.display = '';

                document.querySelector(".step.scouting").style.display = '';
                document.querySelector(".step.scouting").innerHTML = 'Scouting';
                document.querySelector(".step.player-actions").style.display = 'none';
                document.querySelector(".nav-button.nav-button-move-ship").style.display = 'none';
                document.querySelector(".nav-button.nav-button-scout").style.display = 'none';
                document.querySelector(".nav-button.nav-button-port").style.display = 'none';
                document.querySelector(".nav-button.nav-button-fishing").style.display = 'none';
                document.querySelector(".nav-button.nav-button-location").style.display = 'none';
                document.querySelector(".nav-button.nav-button-end-turn").style.display = 'none';
                document.querySelector(".nav-button.nav-button-back").style.display = '';
                document.querySelector(".nav-button.nav-button-back").setAttribute('onclick', "scoutAction('back')")

            };
        };
        xhr.open('GET', 'scoutAction?type_request=' + type_request, true);
        xhr.send();
    };


    if (type_request === 'merchant') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                console.log('BATTLE with MERCHANT')
                // randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, true)

                // document.querySelector(".step.moves").style.display = '';
                // document.querySelector(".nav-button.nav-button-to-port").style.display = '';
                // document.querySelector(".nav-button.nav-button-to-port").disabled = true;
                // document.querySelector(".nav-button.nav-button-from-port").style.display = '';
                // document.querySelector(".nav-button.nav-button-from-port").disabled = false;
                // document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
                // document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;
                // document.querySelector(".nav-button.nav-button-back").style.display = '';

                // endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'scoutAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        let data = 'type_request=' + encodeURIComponent(type_request);

        xhr.send(data);
    };


    if (type_request === 'back') {
        // let xhr = new XMLHttpRequest();
        // xhr.onreadystatechange = function() {
        //     if (xhr.readyState == 4 && xhr.status == 200) {
        //         let response = JSON.parse(xhr.responseText);
        //         let colour = response.playerColour
        //         console.log(response)
    
        //         if (response.playerInPort) {
        //             document.querySelector('.nav-button.nav-button-scout').disabled = true;
        //             document.querySelector('.nav-button.nav-button-port').disabled = false;
        //             document.querySelector('.nav-button.nav-button-fishing').disabled = true;
        //             document.querySelector('.nav-button.nav-button-location').disabled = true;
        //         } else {
        //             document.querySelector('.nav-button.nav-button-scout').disabled = false;
        //             document.querySelector('.nav-button.nav-button-port').disabled = true;
        //             document.querySelector('.nav-button.nav-button-fishing').disabled = false;
        //             document.querySelector('.nav-button.nav-button-location').disabled = false;
        //         };
        //     };
            
        // };
        // xhr.open('GET', 'moveAction?type_request=' + type_request, true);
        // xhr.send();
        document.querySelector(".nav-button.nav-button-scout-merchant").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-dutch-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-english-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-french-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-spanish-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-small-pirate-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-large-pirate-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-blue-player-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-green-player-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-red-player-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-scout-yellow-player-ship").style.display = 'none';
        document.querySelector(".nav-button.nav-button-back").style.display = 'none';

        document.querySelector(".step.player-actions").style.display = '';
        document.querySelector(".nav-button.nav-button-move-ship").style.display = '';
        document.querySelector(".nav-button.nav-button-scout").style.display = '';
        document.querySelector(".nav-button.nav-button-port").style.display = '';
        document.querySelector(".nav-button.nav-button-port").disabled = true;
        document.querySelector(".nav-button.nav-button-fishing").style.display = '';
        document.querySelector(".nav-button.nav-button-location").style.display = '';
        document.querySelector(".nav-button.nav-button-end-turn").style.display = '';
        document.querySelector(".step.scouting").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-to-port").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-from-port").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-n-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-ne-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-e-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-se-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-s-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-sw-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-w-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-nw-direction").style.display = 'none';
        // document.querySelector(".nav-button.nav-button-back").style.display = 'none';
    };

};

// // MOVE ACTIONs - consume one action point
// function moveAction(type_request) {


//     if (type_request === 'moves') {
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);

//                 document.querySelector(".step.player-actions").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-move-ship").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-scout").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-port").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-fishing").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-location").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-end-turn").style.display = 'none';
//                 document.querySelector(".step.moves").style.display = '';

//                 if (response.unitInPort) {
//                     document.querySelector(".nav-button.nav-button-to-port").style.display = '';
//                     document.querySelector(".nav-button.nav-button-to-port").disabled = true;
//                     document.querySelector(".nav-button.nav-button-from-port").style.display = '';
//                     document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
//                     document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;
//                     document.querySelector(".nav-button.nav-button-back").style.display = '';
//                 } else {
                    
//                     document.querySelector(".nav-button.nav-button-to-port").style.display = '';
//                     document.querySelector(".nav-button.nav-button-to-port").disabled = false;
//                     document.querySelector(".nav-button.nav-button-from-port").style.display = '';
//                     document.querySelector(".nav-button.nav-button-from-port").disabled = true;
//                     document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
//                     document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = false;
//                     document.querySelector(".nav-button.nav-button-back").style.display = '';
//                 };

//             };
//         };
//         xhr.open('GET', 'moveAction?type_request=' + type_request, true);
//         xhr.send();
//     };


//     if (type_request === 'back') {
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);
//                 let colour = response.playerColour
//                 console.log(response)
    
//                 if (response.playerInPort) {
//                     document.querySelector('.nav-button.nav-button-scout').disabled = true;
//                     document.querySelector('.nav-button.nav-button-port').disabled = false;
//                     document.querySelector('.nav-button.nav-button-fishing').disabled = true;
//                     document.querySelector('.nav-button.nav-button-location').disabled = true;
//                 } else {
//                     document.querySelector('.nav-button.nav-button-scout').disabled = false;
//                     document.querySelector('.nav-button.nav-button-port').disabled = true;
//                     document.querySelector('.nav-button.nav-button-fishing').disabled = false;
//                     document.querySelector('.nav-button.nav-button-location').disabled = false;
//                 };
//             };
            
//         };
//         xhr.open('GET', 'moveAction?type_request=' + type_request, true);
//         xhr.send();

//         document.querySelector(".step.player-actions").style.display = '';
//         document.querySelector(".nav-button.nav-button-move-ship").style.display = '';
//         document.querySelector(".nav-button.nav-button-scout").style.display = '';
//         document.querySelector(".nav-button.nav-button-port").style.display = '';
//         document.querySelector(".nav-button.nav-button-fishing").style.display = '';
//         document.querySelector(".nav-button.nav-button-location").style.display = '';
//         document.querySelector(".nav-button.nav-button-end-turn").style.display = '';
//         document.querySelector(".step.moves").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-to-port").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-from-port").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-n-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-ne-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-e-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-se-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-s-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-sw-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-w-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-nw-direction").style.display = 'none';
//         document.querySelector(".nav-button.nav-button-back").style.display = 'none';
//     };


//     if (type_request === 'to port') {
//         console.log('WPŁYWAM DO PORTU');
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);
//                 let colour = response.playerColour;
//                 randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, true)

//                 document.querySelector(".step.moves").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-port").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-port").disabled = true;
//                 document.querySelector(".nav-button.nav-button-from-port").style.display = '';
//                 document.querySelector(".nav-button.nav-button-from-port").disabled = false;
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;
//                 document.querySelector(".nav-button.nav-button-back").style.display = '';

//                 endCurrentAction(colour);
//             };
//         };
//         xhr.open('POST', 'moveAction', true);
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//         let data = 'type_request=' + encodeURIComponent(type_request);

//         xhr.send(data);
//     };


//     if (type_request === 'from port') {
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);
//                 let colour = response.playerColour;
//                 randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, false)

//                 document.querySelector(".step.moves").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-port").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-port").disabled = false;
//                 document.querySelector(".nav-button.nav-button-from-port").style.display = '';
//                 document.querySelector(".nav-button.nav-button-from-port").disabled = true;
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = false;
//                 document.querySelector(".nav-button.nav-button-back").style.display = '';

//                 endCurrentAction(colour);
//             };
//         };
//         xhr.open('POST', 'moveAction', true);
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//         let data = 'type_request=' + encodeURIComponent(type_request);

//         xhr.send(data);
//     };


//     if (type_request === 'to sea zone') {
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);
//                 let colour = response.playerColour;
//                 console.log(response)

//                 document.querySelector(".step.moves").style.display = '';
//                 document.querySelector(".nav-button.nav-button-to-port").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-to-port").disabled = true;
//                 document.querySelector(".nav-button.nav-button-from-port").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-from-port").disabled = true;
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").style.display = 'none';
//                 document.querySelector(".nav-button.nav-button-to-sea-zone").disabled = true;

//                 if (response.n !== undefined) {
//                     document.querySelector(".nav-button.nav-button-n-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-n-direction").innerHTML = `N - ${response.n}`;
//                     document.querySelector(".nav-button.nav-button-n-direction").setAttribute('onclick', `moveAction('${response.n}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-n-direction").style.display = 'none';
//                 };
//                 if (response.ne !== undefined) {
//                     document.querySelector(".nav-button.nav-button-ne-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-ne-direction").innerHTML = `NE - ${response.ne}`;
//                     document.querySelector(".nav-button.nav-button-ne-direction").setAttribute('onclick', `moveAction('${response.ne}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-ne-direction").style.display = 'none';
//                 };
//                 if (response.e !== undefined) {
//                     document.querySelector(".nav-button.nav-button-e-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-e-direction").innerHTML = `E - ${response.e}`;
//                     document.querySelector(".nav-button.nav-button-e-direction").setAttribute('onclick', `moveAction('${response.e}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-e-direction").style.display = 'none';
//                 };
//                 if (response.se !== undefined) {
//                     document.querySelector(".nav-button.nav-button-se-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-se-direction").innerHTML = `SE - ${response.se}`;
//                     document.querySelector(".nav-button.nav-button-se-direction").setAttribute('onclick', `moveAction('${response.se}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-se-direction").style.display = 'none';
//                 };
//                 if (response.s !== undefined) {
//                     document.querySelector(".nav-button.nav-button-s-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-s-direction").innerHTML = `S - ${response.s}`;
//                     document.querySelector(".nav-button.nav-button-s-direction").setAttribute('onclick', `moveAction('${response.s}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-s-direction").style.display = 'none';
//                 };
//                 if (response.sw !== undefined) {
//                     document.querySelector(".nav-button.nav-button-sw-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-sw-direction").innerHTML = `SW - ${response.sw}`;
//                     document.querySelector(".nav-button.nav-button-sw-direction").setAttribute('onclick', `moveAction('${response.sw}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-sw-direction").style.display = 'none';
//                 };
//                 if (response.w !== undefined) {
//                     document.querySelector(".nav-button.nav-button-w-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-w-direction").innerHTML = `W - ${response.w}`;
//                     document.querySelector(".nav-button.nav-button-w-direction").setAttribute('onclick', `moveAction('${response.w}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-w-direction").style.display = 'none';
//                 };
//                 if (response.nw !== undefined) {
//                     document.querySelector(".nav-button.nav-button-nw-direction").style.display = '';
//                     document.querySelector(".nav-button.nav-button-nw-direction").innerHTML = `NW - ${response.nw}`;
//                     document.querySelector(".nav-button.nav-button-nw-direction").setAttribute('onclick', `moveAction('${response.nw}')`);
//                 } else {
//                     document.querySelector(".nav-button.nav-button-nw-direction").style.display = 'none';
//                 };

//                 document.querySelector(".nav-button.nav-button-back").style.display = '';

//             };
//         };
//         xhr.open('POST', 'moveAction', true);
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//         let data = 'type_request=' + encodeURIComponent(type_request);

//         xhr.send(data);

//     };


//     const allowedDestinations = [
//         'Basse-Terre',
//         'Bridgetown',
//         'Caracas',
//         'Cartagena',
//         'Curacao',
//         'Gulf City',
//         'Havana',
//         'Nassau',
//         'Old Providence',
//         'Petite Goave',
//         'Port Royal',
//         'San Juan',
//         'Santo Domingo',
//         'St John',
//         'St Maarten',
//         'The Carribean Sea',
//         'Tortuga',
//         'Trinidad',
//     ];
//     if (allowedDestinations.includes(type_request)) {
//         console.log(`płynę do ${type_request}`);
//         let xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState == 4 && xhr.status == 200) {
//                 let response = JSON.parse(xhr.responseText);
//                 let colour = response.playerColour;
//                 randomInsidePosition(response.playerShipUnit, colour, response.playerDestination, false)

//                 moveAction('to sea zone');

//                 endCurrentAction(colour);
//             };
//         };
//         xhr.open('POST', 'moveAction', true);
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//         let data = 'type_request=' + encodeURIComponent(type_request);

//         xhr.send(data);





//     };
// };
