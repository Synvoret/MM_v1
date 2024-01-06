// FAVORs TRACK, PUT CUBE
function updateFavorsTrack(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);
            document.getElementById('cube-favor-image').setAttribute('href', response.cubeImage);
            document.getElementById(response.favorValue + '-favor-track').setAttribute('href', '#cube-favor-image');
        }
    };
    xhr.open('GET', 'favorsTrackCube?colour=' + colour, true);
    xhr.send();
};