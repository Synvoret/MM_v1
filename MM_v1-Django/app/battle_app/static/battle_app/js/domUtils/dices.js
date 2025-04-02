async function dices(roundRecordd, side, test, amount) {

    const roundRecord = await combatFlow();

    const url = 'dices';
    const response = await fetch (url, { method: "GET" })
        .then(response => response.json())
        .then(data => {


            const spanDiceRoll = document.createElement('span');
            spanDiceRoll.style.display = 'flex';
            spanDiceRoll.style.alignItems = 'center';

            // side
            const sideDice = document.createElement('p');
            // console.log(roundRecord)
            if (test === 'seamanship') {
                const role = 'test'
                sideDice.textContent = `${side}-${test}-${role}`;
            } else if (test === 'shot' && side === 'aggressor') {
                const role = 'location'
                sideDice.textContent = `${side}-${test}-${role}`;
            } else if (test === 'shot' && side === 'defender') {
                const role = 'test'
                sideDice.textContent = `${side}-${test}-${role}`;
            }
            spanDiceRoll.appendChild(sideDice);

            // amount dices
            for (let i = 1; i <= amount; i++) {
                const diceGraphic = document.createElement('img');
                diceGraphic.style.width = '25px';
                diceGraphic.style.height = '25px';
                diceGraphic.src = data.dice1Image;
                diceGraphic.className = `dice-${i}-${side + '-' + test}`;
                spanDiceRoll.appendChild(diceGraphic);
            };

            // roll button
            const rollButton = document.createElement('button');
            rollButton.className = `roll-button-${side}`;
            rollButton.textContent = 'Roll';
            rollButton.addEventListener('click', () => {
                rollButton.disabled = true;
                dicesRoll(roundRecord, side, test); // roll Dices function start
            });
            spanDiceRoll.appendChild(rollButton);

            document.getElementById(`round-section-${roundRecord.round}`).appendChild(spanDiceRoll);
        })

};
