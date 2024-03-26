function frameElement(id, cleaning=false) {

    let imageElement = document.getElementById(id);
    let parentElement = imageElement.parentNode;

    // cleaning other brother frames after one parent
    if (cleaning) {
        parentElement.querySelectorAll('.frame').forEach(function(element) {
            element.remove();
        });
    };
    
    if (parentElement.querySelector(`#${id}-frame`) !== null) {
        parentElement.querySelector(`#${id}-frame`).remove();
    } else {
        let x = parseInt(imageElement.getAttribute('x'));
        let y = parseInt(imageElement.getAttribute('y'));
        let width = parseInt(imageElement.getAttribute('width'));
        let height = parseInt(imageElement.getAttribute('height'));

        // gain player colour from g tag
        let styles = window.getComputedStyle(parentElement);
        let colour = styles.stroke

        let rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute('id', `${id}-frame`);
        rect.setAttribute('class', 'frame');
        rect.setAttribute("x", x - 2);
        rect.setAttribute("y", y - 2);
        rect.setAttribute("rx", "4");
        rect.setAttribute("ry", "4");
        rect.setAttribute("width", width + 2);
        rect.setAttribute("height", height + 2);
        rect.style.stroke = colour;
        rect.style.strokeWidth = 3;

        parentElement.insertBefore(rect, imageElement);
    };
};


function frameElementsDestroy(id) {
    let parentElement = document.getElementById(id).parentNode;
    parentElement.querySelectorAll('.frame').forEach(function(element) {
        element.remove();
    });
};
