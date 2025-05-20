// function responsible for creating ACTION buttons in row
async function actionButton(round, side, act) {

    let actionButtons = document.querySelector('.actionButtons');
    if (!actionButtons) {
        actionButtons = document.createElement('span');
        actionButtons.className = 'actionButtons';
        document.getElementById(`round-section-${round}`).appendChild(actionButtons);
    };
    // create button
    const element = document.createElement('button');
    element.className = `button-${act}`;
    element.textContent = `${act}`;

    element.addEventListener('click', async function() {
        this.parentElement.remove();
        document.getElementById(`round-section-${round}`).appendChild(await createP(`Declaration - ${act}`));
        try {
            const dataToSend = {
                'side': side,
                'act': act
            }
            const response = await fetch(`declaration`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(dataToSend),
            });
            const data = await response.json();
            const declaration = data;
        } catch (error) {
            console.error("Error during catch data", error);
        }
        // nextRound();
        await seaBattle();
    });

    return element;
};
