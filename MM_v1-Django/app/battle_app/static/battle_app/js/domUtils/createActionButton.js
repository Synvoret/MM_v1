// function responsible for creating ACTION buttons in row
async function createActionButton(roundRecord, action, side) {
    // const actionButtons = document.getElementById('round-section-2');
    let actionButtons = document.querySelector('.actionButtons');
    if (!actionButtons) {
        actionButtons = document.createElement('span');
        actionButtons.className = 'actionButtons';
        document.getElementById(`round-section-${roundRecord.round}`).appendChild(actionButtons);
    };
    // create button
    const element = document.createElement('button');
    element.className = `Button${action}`;
    element.textContent = action;

    element.addEventListener('click', async function() {
        this.parentElement.remove();
        await createP(roundRecord, action);
        await combatFlow(request='POST', side=side, parameter='declaration', value=action, next_round=false);
        // nextRound();
        await seaBattle();
    });

    actionButtons.appendChild(element);
};
