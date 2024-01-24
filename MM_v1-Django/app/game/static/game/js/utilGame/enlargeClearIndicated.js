function enlagreIndicated(id) {

    let elementToEnlarge = document.getElementById(id); // get zooming element
    let zoom = 4; // zoom value if zooming image
    let fontSize = 20; //size value if zooming text


    // ID: NEED ID-NAME ELEMENT
    if (elementToEnlarge.getAttribute('id').startsWith('id-name-')) {
        // element
        let name = elementToEnlarge.getAttribute('name');
        let enlargeIndicatedNameId = document.getElementById('board-enlarge-indicated-text');
        modifedName = name.replace(/^name-/i, '').replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        document.getElementById('board-enlarge-indicated-use').setAttribute('href', '#board-enlarge-indicated-text');
        enlargeIndicatedNameId.innerHTML = modifedName;
        enlargeIndicatedNameId.style.fontSize = fontSize;
        document.getElementById('board-enlarge-indicated-use').style.display = 'block';
        // zoom in/out
        elementToEnlarge.addEventListener("wheel", function(event) {
            event.preventDefault();
            if (event.deltaY > 0) {
                fontSize = Math.max(1, fontSize - 1);
            } else if (event.deltaY < 0) {
                fontSize += 1;
            };
            enlargeIndicatedNameId.style.fontSize = fontSize;
        });
    };


    // ID: NEED ID-FEATURE ELEMENT
    if (elementToEnlarge.getAttribute('id').startsWith('id-feature-')) {
        // element
        let seaZone = (elementToEnlarge.getAttribute('id')).replace('id-feature-', '');
        let widthIndicated = '50'
        let heightIndicated = '25'
        let featuresImage = '';
        let enlargeIndicatedImageId = document.getElementById('board-enlarge-indicated-image');
        enlargeIndicatedImageId.removeAttribute('href');
        let enlargeIndicatedRectId = document.getElementById('board-enlarge-indicated-rect');
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                featuresImage = response.featureImage;
                enlargeIndicatedImageId.setAttribute('href', featuresImage);
                enlargeIndicatedImageId.setAttribute('width', widthIndicated * zoom);
                enlargeIndicatedImageId.setAttribute('height', heightIndicated * zoom);
                enlargeIndicatedRectId.setAttribute('width', widthIndicated * zoom);
                enlargeIndicatedRectId.setAttribute('height', heightIndicated * zoom);
            }
        };
        xhr.open('GET', 'featuresSeaZones?sea_zone=' + seaZone, true);
        xhr.send();
        document.getElementById('board-enlarge-indicated-use').setAttribute('href', '#board-enlarge-indicated-image');
        document.getElementById('board-enlarge-indicated-use').style.display = 'block';
        // zoom in/out
        elementToEnlarge.addEventListener("wheel", function(event) {
            event.preventDefault();
            if (event.deltaY > 0) {
                zoom = Math.max(1, zoom - 1);
            } else if (event.deltaY < 0) {
                zoom += 1;
            };
            enlargeIndicatedImageId.setAttribute('width', widthIndicated * zoom);
            enlargeIndicatedImageId.setAttribute('height', heightIndicated * zoom);
            enlargeIndicatedRectId.setAttribute('width', widthIndicated * zoom);
            enlargeIndicatedRectId.setAttribute('height', heightIndicated * zoom);
        });
    };


    // ID: NEED ID CURRENTLY IMAGE ELEMENT
    if (elementToEnlarge.tagName === 'image') {
        // element
        let image = elementToEnlarge.getAttribute('href');
        let widthIndicated = elementToEnlarge.getAttribute('width');
        let heightIndicated = elementToEnlarge.getAttribute('height');
        // image, rect, zoom
        let enlargeIndicatedImageId = document.getElementById('board-enlarge-indicated-image');
        let enlargeIndicatedRectId = document.getElementById('board-enlarge-indicated-rect');
        // setting parametrs if image href exist
        if (image) {
            enlargeIndicatedImageId.setAttribute('href', image);
            enlargeIndicatedImageId.setAttribute('width', widthIndicated * zoom);
            enlargeIndicatedImageId.setAttribute('height', heightIndicated * zoom);
            enlargeIndicatedRectId.setAttribute('width', widthIndicated * zoom);
            enlargeIndicatedRectId.setAttribute('height', heightIndicated * zoom);
            document.getElementById('board-enlarge-indicated-use').setAttribute('href', '#board-enlarge-indicated-image');
            document.getElementById('board-enlarge-indicated-use').style.display = 'block';
            // zoom in/out
            elementToEnlarge.addEventListener("wheel", function(event) {
                event.preventDefault();
                if (event.deltaY > 0) {
                    zoom = Math.max(1, zoom - 1);
                } else if (event.deltaY < 0) {
                    zoom += 1;
                };
                enlargeIndicatedImageId.setAttribute('width', widthIndicated * zoom);
                enlargeIndicatedImageId.setAttribute('height', heightIndicated * zoom);
                enlargeIndicatedRectId.setAttribute('width', widthIndicated * zoom);
                enlargeIndicatedRectId.setAttribute('height', heightIndicated * zoom);
            });
        };
    };

    // position indicated on BOARD
    let boardSvg = document.getElementById('board-svg');
    boardSvg.addEventListener('mousemove', function(event) {
        let boardSvgRect = boardSvg.getBoundingClientRect();
        let mouseX = event.clientX - boardSvgRect.left;
        let mouseY = event.clientY - boardSvgRect.top;
        let positionShift = 25;
        document.getElementById('board-enlarge-indicated-use').setAttribute('x', mouseX + positionShift);
        document.getElementById('board-enlarge-indicated-use').setAttribute('y', mouseY + positionShift);
    });
    // mouse leave id-name element
    elementToEnlarge.addEventListener("mouseleave", function() {
        document.getElementById('board-enlarge-indicated-use').style.display = 'none';
    });
};
