// LOYALITY TRACK, PUT CUBE
function updateLoyalityTrack(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {

            let loyalitiesClass = document.getElementsByClassName('loyality');
            for (let i = 0; i < loyalitiesClass.length; i++) {
                loyalitiesClass[i].setAttribute('href', '');
            };

            let response = JSON.parse(xhr.responseText);
            document.getElementById('cube-loyality-image').setAttribute('href', response.cubeImage);
            document.getElementById(response.loyalityValue +'-loyality-track').setAttribute('href', '#cube-loyality-image');


        }
    };
    xhr.open('GET', 'loyalityTrackCube?colour=' + colour, true);
    xhr.send();
};