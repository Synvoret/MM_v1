// PUT LOCATION TOKENs
function putLocationToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response)
        }
    };
    xhr.open('GET', "putLocationToken", true);
    xhr.send();
}