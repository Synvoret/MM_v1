// GRAB AND MOVE SHIPs
function enableDrag(element) {
    let isDragging = false;
    let offset = { x: 0, y: 0 };

    element.addEventListener("mousedown", function (e) {
        isDragging = true;

        // Calculate the offset of the mouse click relative to the element's position
        offset.x = e.clientX - element.getAttribute("x");
        offset.y = e.clientY - element.getAttribute("y");
    });

        document.addEventListener("mousemove", function (e) {
            if (!isDragging) return;

                // Update the element's position based on the mouse movement
                const newX = e.clientX - offset.x;
                const newY = e.clientY - offset.y;

                element.setAttribute("x", newX);
                element.setAttribute("y", newY);
            });

            document.addEventListener("mouseup", function () {
            isDragging = false;
        });
};

const shipPlastic = document.querySelectorAll(".player-ship-plastic");
// Enable drag for each ship plastic
shipPlastic.forEach(enableDrag);
