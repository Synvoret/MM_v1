async function dicesRoll(roundRecord, side, test) {


    const diceImages = document.getElementById(`round-section-${roundRecord.round}`).querySelectorAll(`img[class^="dice-"][class$="-${side + '-' + test}"]`); // array dices img to roll
    // const diceImagesArray = Object.values(diceImages);
    const amountDiceImages = diceImages.length

    const dataToSend = {
        side: side,
        test: test,
        amountDices: amountDiceImages,
    }
    const url = `dices`;
    const response = await fetch (url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataToSend),
    })
        .then(response => response.json())
        .then(data => {
            diceImages.forEach((img, index) => {
                img.src = Object.values(data)[index]
            });

            if (test === 'seamanship') {
                if (data.aggressor.seamanship_roll_result.length > 0 && data.defender.seamanship_roll_result.length > 0) {
                    const resultsObject = diceRollComparison(roundRecord, test, data.aggressor.seamanship_roll_result, data.defender.seamanship_roll_result);
                    if ('mess1' in resultsObject) {
                        createP(roundRecord, resultsObject.mess1);
                    }
                    if ('mess2' in resultsObject) {
                        createP(roundRecord, resultsObject.mess2);
                    }
                    if ('testWinner' in resultsObject) {
                        if ((data[resultsObject['testWinner']].declaration).toLowerCase() == 'shot') {
                            shooting(roundRecord, resultsObject['testWinner'], data[resultsObject['testWinner']]['cannons']);
                        } else if ((data[resultsObject['testWinner']].declaration).toLowerCase() == 'board') {
                            // boarding(roundCounter, resultsObject['testWinner'], data[resultsObject['testWinner']]['leadership']);
                            // boarding(roundCounter, resultsObject['testLoser'], data[resultsObject['testLoser']]['leadership']);
                            // return;
                        }
                    }
                    if ('testLoser' in resultsObject) {
                        if ((data[resultsObject['testLoser']].declaration).toLowerCase() == 'shot') {
                            shooting(roundRecord, resultsObject['testLoser'], data[resultsObject['testLoser']]['cannons']);
                        } else if ((data[resultsObject['testLoser']].declaration).toLowerCase() == 'board') {
                            // boarding(roundCounter, resultsObject['testLoser'], data[resultsObject['testLoser']]['leadership']);
                        }
                    }
                    if ('nextRound' in resultsObject && resultsObject.nextRound === true) {
                        nextRound(roundRecord, reason='', endBattle=false);
                    }
                }
            } else {
                const aggressorDeclaration = data.aggressor.declaration;
                const defenderDeclaration = data.defender.declaration;
                 // shoot both side
                if (aggressorDeclaration.toLowerCase() == 'shot' && defenderDeclaration.toLowerCase() == 'shot') {
                    if (data['aggressor'][`${test}_roll_result`].length > 0 && data['defender'][`${test}_roll_result`].length > 0) {
                        console.log(aggressorDeclaration, data['aggressor'][`${test}_roll_result`], defenderDeclaration, data['defender'][`${test}_roll_result`]);
                    }
                } 
                
            }

            // if (test === 'shot') {
            //     if (data.aggressor.shot_roll_result.length > 0 && data.defender.shot_roll_result.length > 0) {
            //         const resultsObject = diceRollComparison(roundCounter, test, data.aggressor.shot_roll_result, data.defender.shot_roll_result);
            //     }
            // }

        });


};