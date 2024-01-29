function endCurrentAction(action) {

    // FISHING ACTION END
    if (action === 'fishing') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                document.getElementById('fishing-action-main-rect').style.removeProperty('stroke');
                document.getElementById('fishing-action-ok-text').style.removeProperty('fill');
                document.getElementById('fishing-card-image').setAttribute('href', '');
                document.getElementById('fishing-action-use').style.display = 'none';
            }
        };
        xhr.open('GET', 'endCurrentAction', true);
        xhr.send();
    };

};
