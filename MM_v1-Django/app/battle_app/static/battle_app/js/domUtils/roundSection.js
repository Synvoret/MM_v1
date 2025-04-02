async function roundSection(roundRecord) {

    // const roundRecord = await combatFlow();

    // ROUND SECTION
    const roundSection = document.createElement('section');
    roundSection.id = `round-section-${roundRecord.round}`;

    const line = document.createElement('hr');

    const battleLogs = document.getElementById('battle-logs');

    // check child for battleLogs
    if (battleLogs.firstElementChild) {
        // If have child
        battleLogs.insertBefore(roundSection, battleLogs.firstElementChild);
    } else {
        // If haven't child
        battleLogs.appendChild(roundSection);
        roundSection.appendChild(line);
    };

    roundSection.appendChild(line);

    // ROUND COUNTER
    const roundCounter = document.createElement('h4');
    roundCounter.className = 'roundCounter';
    roundCounter.textContent = `Round: >> ${roundRecord.round} <<`;
    document.getElementById(`round-section-${roundRecord.round}`).appendChild(roundCounter);
};
