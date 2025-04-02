// function responsible for displaying content
async function createP(roundRecord, content) {
    const element = document.createElement('p');
    // element.style.textAlign = 'left';
    element.className = `description`;
    element.textContent = content;
    document.getElementById(`round-section-${roundRecord.round}`).appendChild(element);
};
