boardContainer.addEventListener('mousemove', function(event) {
    var mouseX = parseInt(event.clientX - boardContainer.getBoundingClientRect().left);
    var mouseY = parseInt(event.clientY - boardContainer.getBoundingClientRect().top);
    tspans.forEach(function(tspan, index) {
        tspan.setAttribute('x', mouseX + 5);
        tspan.setAttribute('y', mouseY  + 35 + index * 14);
    });

    tspans[1].innerHTML = 'poz. ' + mouseX + ' ' + mouseY;
})

// WYŚWIETLENIE OKNA POMOCY DLA NAJECHANEGO ELEMENTU
boardContainer.addEventListener('mousemove', function (event) {
    if (['ellipse', 'circle', 'polygon', 'rect', 'use', 'path'].includes(event.target.tagName.toLowerCase())) {
        var name = event.target.getAttribute('name');
        tspans[0].textContent = name;
    }
});
boardContainer.addEventListener('mouseout', function () {
    // tspans[0].innerHTML = '-';
    tspans[0].textContent = '-';
});




// PRZESUWANIE ELEMENTU
const moveTester = document.getElementById('move-tester');
moveTester.addEventListener('mousedown', (e) => {
    if (e.target === moveTester) {
        isDragging = true;
        offsetX = e.clientX - moveTester.getBoundingClientRect().left;
        offsetY = e.clientY - moveTester.getBoundingClientRect().top;
    }
});
document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    var mouseX = parseInt(e.clientX - boardContainer.getBoundingClientRect().left);
    var mouseY = parseInt(e.clientY - boardContainer.getBoundingClientRect().top);
    moveTester.setAttribute('cx', mouseX);
    moveTester.setAttribute('cy', mouseY);
});
document.addEventListener('mouseup', () => {
    isDragging = false;
});























































