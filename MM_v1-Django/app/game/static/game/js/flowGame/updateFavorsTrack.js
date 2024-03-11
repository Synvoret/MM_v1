// FAVORs TRACK, PUT CUBE
function updateFavorsTrack(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            for (let i = 0; i <= 5; i++) {
                if (document.getElementById(`${i}-favour-track`).getAttribute('href') !== '') {
                    document.getElementById(`${i}-favour-track`).setAttribute('href', '');
                };
            };

            let favour = parseInt(response.favourValue)
            document.getElementById('cube-favour-image').setAttribute('href', response.cubeImage);
            document.getElementById(`${favour}-favour-track`).setAttribute('href', '#cube-favour-image');

        }
    };
    xhr.open('GET', 'favorsTrackCube?colour=' + colour, true);
    xhr.send();
};