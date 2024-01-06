// PUT CUBEs on TRACK GLORY POINTs
function updateGloryTrack() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById("blue-cube-image").setAttribute('href', response.blueCubeImage);
            document.getElementById("green-cube-image").setAttribute('href', response.greenCubeImage);
            document.getElementById("red-cube-image").setAttribute('href', response.redCubeImage);
            document.getElementById("yellow-cube-image").setAttribute('href', response.yellowCubeImage);
            document.getElementById('blue-' + response.playerBlue + '-glory-point-cube').setAttribute('href', "#blue-cube-image");
            document.getElementById('green-' + response.playerGreen + '-glory-point-cube').setAttribute('href', "#green-cube-image");
            document.getElementById('red-' + response.playerRed + '-glory-point-cube').setAttribute('href', "#red-cube-image");
            document.getElementById('yellow-' + response.playerYellow + '-glory-point-cube').setAttribute('href', "#yellow-cube-image");
        }
    };
    xhr.open('GET', "gloryTrackCube", true);
    xhr.send();
};