// PUT CUBEs on TRACK GLORY POINTs
function updateGloryTrack(colour) {
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            const colours = ['blue', 'green', 'red', 'yellow'];
            for (const colour of colours) {
                const cubeImageID = colour + "-cube-image"
                document.getElementById(cubeImageID).setAttribute('href', response[colour + 'CubeImage']);
                const gloryPointID = `${colour}-${response[colour + 'GloryPoint']}-glory-point-cube`;
                document.getElementById(gloryPointID).setAttribute('href', `#${cubeImageID}`);
                if (parseInt(response[colour + 'GloryPoint']) > 0) {
                    let lastGloryPointID = `${colour}-${parseInt(response[colour + 'GloryPoint']) - 1}-glory-point-cube`;
                    document.getElementById(lastGloryPointID).setAttribute('href', ``);
                }
            }
            
        }
    };

    xhr.open('GET', "updateGloryTrack", true);
    xhr.send();

};
