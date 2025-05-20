async function dices(side, test, amount, func) {

    try {
        const url = 'dices';
        const response = await fetch (url, { method: "GET" })
        const data = await response.json();

        const dices = data.roundRecord;

        const spanDiceRoll = document.createElement('span');
        spanDiceRoll.style.display = 'flex';
        spanDiceRoll.style.alignItems = 'center';

        spanDiceRoll.appendChild(await createP(`${side}-${test}`));

        // amount dices
        for (let i = 1; i <= amount; i++) {
            const diceGraphic = document.createElement('img');
            diceGraphic.style.width = '25px';
            diceGraphic.style.height = '25px';
            diceGraphic.src = dices.dice1Image;
            diceGraphic.className = `dice-${i}-${side + '-' + test}`;
            spanDiceRoll.appendChild(diceGraphic);
        };

        // roll-dices button function after click
        const rollButton = document.createElement('button');
        rollButton.className = `roll-button-${side}-${test}-${dices.round}`;
        rollButton.textContent = 'Roll';
        rollButton.addEventListener('click', async() => {
                rollButton.disabled = true;
                await func()
            }
        );
        spanDiceRoll.appendChild(rollButton);

        return spanDiceRoll;


    } catch (error) {
        console.error("Error during catch data", error);
    }
    

}