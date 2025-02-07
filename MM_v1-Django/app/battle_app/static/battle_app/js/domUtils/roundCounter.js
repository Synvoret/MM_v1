// roundCounter function and displaying this
function roundCounter(roundNumber){

    const roundCounter = document.createElement('h5');
    roundCounter.className = 'roundCounter';
    roundCounter.textContent = `Round: >> ${roundNumber} <<`;

    document.getElementById(`round-section-${roundNumber}`).appendChild(roundCounter);

};