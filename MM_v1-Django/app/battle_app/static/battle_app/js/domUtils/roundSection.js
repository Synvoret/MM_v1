function roundSection(roundNumber) {

    const roundSection = document.createElement('section');
    roundSection.id = `round-section-${roundNumber}`;
    document.getElementById('battle-logs').appendChild(roundSection);

};




// const roundCounter = document.createElement('h5');
// roundCounter.className = 'roundCounter';
// roundCounter.textContent = `Round: >> ${roundNumber} <<`;
// document.getElementById('battle-logs').appendChild(roundCounter);