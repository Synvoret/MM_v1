// DRAW RANDOMLY MERCHANT TOKEN
function drawMerchantToken(id) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById(id).setAttribute('href', xhr.response);
        };
    };
    xhr.open('GET', 'drawMerchantToken', true);
    xhr.send();
};