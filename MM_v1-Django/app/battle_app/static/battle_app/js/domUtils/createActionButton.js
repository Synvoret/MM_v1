// function responsible for creating ACTION buttons in row
function createActionButton(action, side) {
    let actionButtons = document.querySelector('.actionButtons');
    if (!actionButtons) {
        actionButtons = document.createElement('span');
        actionButtons.className = 'actionButtons';
        document.getElementById('battle-logs').appendChild(actionButtons);
    };
    // create button
    const element = document.createElement('button');
    element.className = `Button${action}`;
    element.textContent = action;

    element.addEventListener('click', function() {
        this.parentElement.remove();
        createP(action);
        battleLocalStorage(issue='update', key='declarations', value=true, side=side);
        playerAttackNPC();
    });

    actionButtons.appendChild(element);
};