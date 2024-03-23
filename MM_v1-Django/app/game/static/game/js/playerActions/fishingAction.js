// FISHING ACTION - consume one action point
function fishingAction(type_request) {

    if (type_request === 'get') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                navFishingAction(type_request);

                document.getElementById('fishing-action-main-rect').style.stroke = response.playerColour;
                document.getElementById('fishing-action-ok-text').style.fill = response.playerColour;
                document.getElementById('fishing-card-image').setAttribute('href', response.fishingCardImage);
                document.getElementById('fishing-action-use').style.display = 'block';
            }
        };
        xhr.open('GET', 'fishingAction', true);
        xhr.send();
    };


    if (type_request === 'post') {

        navFishingAction(type_request);

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let colour = response.playerColour;
                if (response.fishingValue) {
                    updatePlayerGolds(colour);
                };
                if (response.fishingHits) {
                    updatePlayerHitLocation(colour);
                };
                document.getElementById('fishing-action-main-rect').style.removeProperty('stroke');
                document.getElementById('fishing-action-ok-text').style.removeProperty('fill');
                document.getElementById('fishing-card-image').setAttribute('href', '');
                document.getElementById('fishing-action-use').style.display = 'none';

                endCurrentAction(colour);
            };
        };
        xhr.open('POST', 'fishingAction', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send();
    };
};
