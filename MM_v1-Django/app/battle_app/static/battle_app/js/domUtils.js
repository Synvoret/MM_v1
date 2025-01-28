// roundcounter function and displaying this
function roundCounter(roundNumber){
    console.log(`POCZĄTEK RUNDY: ${roundNumber}`);
    const roundCounter = document.createElement('h5');
    roundCounter.className = 'roundCounter';
    roundCounter.textContent = `Round: ${roundNumber}`;
    document.getElementById('battle-logs').appendChild(roundCounter);
};


// 
function declarationSide(side) {
    const declaration = document.createElement('p');
    declaration.className = 'declaration';
    declaration.textContent = `Declaration: ${side}`;
    document.getElementById('battle-logs').appendChild(declaration);
};


// function responsible for creating action buttons in row
function createActionButton(action, side) {
    let actionButtons = document.querySelector('.actionButtons');
    const actions = JSON.parse(localStorage.getItem('actions'));
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
        playerAttackNPC();
    });
    actionButtons.appendChild(element);
};


// function responsible for displaying content
function createP(content) {
    const element = document.createElement('p');
    element.className = `description`;
    element.textContent = content;
    document.getElementById('battle-logs').appendChild(element);
};

