// PUT CUBEs on TRACK GLORY POINTs
function updateGloryTrack(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            const imageID = colour + "-cube-image"
            document.getElementById(imageID).setAttribute('href', response.cubeImage);
            const gloryPointID = colour + "-" + response.amountGloryPoint + '-glory-point-cube'
            document.getElementById(gloryPointID).setAttribute('href', "#" + imageID);
        }
    };
    xhr.open('GET', "updateGloryTrack?colour=" + colour, true);
    xhr.send();
};
