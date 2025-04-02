// function compares test results during the battle. seamanship, leadership...
function diceRollComparison(roundRecord, test, aggressorResults, defenderResults) {

    // COUNTERs
    // counts the skull in array
    const countAggressorSkull = aggressorResults.filter(skull => skull === 'skull').length;
    const countDefenderSkull = defenderResults.filter(skull => skull === 'skull').length;
    // sum numbers except skull
    const sumAggressorNumbers = aggressorResults
        .filter(number => number !== 'skull')
        .map(number => parseInt(number, 10))
        .reduce((acc, number) => acc + number, 0);
    const sumDefenderNumbers = defenderResults
        .filter(number => number !== 'skull')
        .map(number => parseInt(number, 10))
        .reduce((acc, number) => acc + number, 0);
    // console.log('ILOŚĆ SKULLi', countAggressorSkull, countDefenderSkull, 'SUMA', sumAggressorNumbers, sumDefenderNumbers)

    const resultsObject = {
        'nextRound': false,
    }

    // RESULTs LOGIC for SEAMANSHIP TEST
    if (test === 'seamanship') {
        if (countAggressorSkull === 0 && countDefenderSkull == 0) {
            resultsObject.mess1 = 'No success';
            resultsObject.mess2 = 'Start next round';
            resultsObject.nextRound = true;
        } else if (countAggressorSkull > countDefenderSkull) {
            resultsObject.mess1 = `Aggressor win ${test} test`;
            resultsObject.testWinner = 'aggressor';
            resultsObject.testLoser = 'defender';
        } else if (countAggressorSkull < countDefenderSkull) {
            resultsObject.mess1 = `Defender win ${test} test`;
            resultsObject.testWinner = 'defender';
            resultsObject.testLoser = 'aggressor';
        } else if (countAggressorSkull === countDefenderSkull) {
            if (sumAggressorNumbers > sumDefenderNumbers) {
                resultsObject.mess1 = `Aggressor win ${test} test`;
                resultsObject.testWinner = 'aggressor';
                resultsObject.testLoser = 'defender';
            } else if (sumAggressorNumbers < sumDefenderNumbers) {
                resultsObject.mess1 = `Defender win ${test} test`;
                resultsObject.testWinner = 'defender';
                resultsObject.testLoser = 'aggressor';
            } else if (sumAggressorNumbers === sumDefenderNumbers) {
                resultsObject.mess1 = 'Draw';
                resultsObject.mess2 = 'Start next round';
                resultsObject.nextRound = true;
            }
        }
    }
    

    return resultsObject;

    // if (test === 'seamanship') {
    //     console.log('sprawdzam wyniki SEAMANSHIP');
    //     console.log(aggressorResults);
    //     console.log(defenderResults);
    // }

};
