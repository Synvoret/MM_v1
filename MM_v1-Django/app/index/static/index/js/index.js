let spanik = document.getElementById('spanik');
const button = document.getElementById('button');

function clicker(event) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            spanik.innerText = xhr.responseText;
        }
    };
    xhr.open('GET', '/random_number', true);
    xhr.send();
}

button.addEventListener('click', clicker)
