// function responsible for displaying content
function createP(roundNumber, content) {
    const element = document.createElement('p');
    element.className = `description`;
    element.textContent = content;
    document.getElementById(`round-section-${roundNumber}`).appendChild(element);
};