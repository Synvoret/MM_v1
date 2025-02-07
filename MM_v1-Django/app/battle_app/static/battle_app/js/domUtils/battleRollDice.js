async function battleDiceRoll(roundNumber, feature, side) {

    const response = await fetch ('diceImage', {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {

        const battleLogStr = localStorage.getItem("battleLog");
        const battleLogObj = JSON.parse(battleLogStr);
        amountDices = battleLogObj[side][feature];

        const spanDiceRoll = document.createElement('span');
        spanDiceRoll.style.display = 'flex';
        spanDiceRoll.style.alignItems = 'center';

        // side
        const sideDice = document.createElement('p');
        sideDice.textContent = `${side}`;
        spanDiceRoll.appendChild(sideDice);

        // amount dices
        for (let i = 1; i <= amountDices; i++) {
            const diceGraphic = document.createElement('img');
            diceGraphic.style.width = '25px';
            diceGraphic.style.height = '25px';
            diceGraphic.src = data.dice1Image;
            diceGraphic.className = `dice-${i}-${side}`;
            spanDiceRoll.appendChild(diceGraphic);
        };

        // roll button
        const rollButton = document.createElement('button');
        rollButton.className = `roll-button-${side}`;
        rollButton.textContent = 'Roll';
        rollButton.addEventListener('click', () => {
            rollButton.disabled = true;

            diceRoll(roundNumber, side); // roll dices function start

        });
        spanDiceRoll.appendChild(rollButton);

        document.getElementById(`round-section-${roundNumber}`).appendChild(spanDiceRoll);
    })

};





// roll dices
async function diceRoll(roundNumber, side) {
    const response = await fetch ('diceImage', {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {
        const battleLogStr = localStorage.getItem("battleLog");
        const battleLogObj = JSON.parse(battleLogStr);
        const diceImages = document.getElementById(`round-section-${roundNumber}`).querySelectorAll(`img[class^="dice-"][class$="-${side}"]`);
        diceImages.forEach(img => {
            const rollResult = Math.floor(Math.random() * 6) + 1;
            battleLogObj[side].seamanship_result.push(rollResult);
            img.src = data[`dice${rollResult}Image`];
        });
        localStorage.setItem("battleLog", JSON.stringify(battleLogObj));
        if (battleLogObj['Player']['seamanship_result'].length > 0 && battleLogObj['NPC']['seamanship_result'].length > 0) {
            // all seamanship dices rolled
            diceRollComparison(roundNumber);
            console.log(battleLogObj['Player']['seamanship_result']);
            console.log(battleLogObj['NPC']['seamanship_result']);
        };
    });

};








// async function battleDiceRoll(amount, side) {
//     const response = await fetch ('diceImage', {
//         method: "GET"
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
// };


// upgrade
// async function battleDiceRoll(amount, side) {
//     try {
//         const response = await fetch('diceImage', { method: "GET" });
//         const data = await response.json();
//         console.log(data);
    
//         // Załóżmy, że masz w HTML element <p id="result"></p>
//         const resultParagraph = document.getElementById('result');
//         resultParagraph.textContent = JSON.stringify(data); // Możesz też użyć innerHTML, jeśli potrzebujesz HTML
    
//         } catch (error) {
//         console.error('Błąd podczas pobierania danych:', error);
//         }
//     }
