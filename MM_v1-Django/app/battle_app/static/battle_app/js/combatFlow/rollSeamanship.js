async function rollSeamanship(round, side) {

    try {
        const diceImages = document.getElementById(`round-section-${round}`).querySelectorAll(`img[class^="dice-"][class$="-${side + '-seamanship'}"]`); // array dices img to roll
        const amountDices = diceImages.length;

        const dataToSend = {
            'side': side,
            'test': 'seamanship',
            'amountDices': amountDices,
        }
        const response = await fetch(`dices`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(dataToSend),
        });
        const data = await response.json();
        const dicesRoll = data.roundRecord;

        diceImages.forEach((img, index) => {img.src = dicesRoll[`dice${index + 1}Image`]});
    
        // WHEN BOTH SIDES AFTER TEST SEAMANSHIP
        if (data.roundRecord['aggressor']['seamanship_result_comparison'] !== null && data.roundRecord['defender']['seamanship_result_comparison'] !== null) {
            await seamanship(phase='result');
        }


    } catch (error) {
        console.error("Error during catch data", error);
    }
}





        // if (test === 'seamanship') {

        //     document.getElementById(`round-section-${roundRecord.round}`).appendChild(await createP(data.resultMess1));
        //     document.getElementById(`round-section-${roundRecord.round}`).appendChild(await createP(data.resultMess2));
            
        //     if ((roundRecord['aggressor']['declaration']).toLowerCase() === 'shot'
        //         && (roundRecord['defender']['declaration']).toLowerCase() === 'shot') {
        //             await seamanship(phase='result');
        //     }

            // if (data['resultNextRound']) {
            //     await startRound(reason='next_round', endBattle=false);
            // } else if (data['shipSunk']) {
            //     await startRound(reason='Ship Sunk!', endBattle=true);
            // }
        // } else if (test === 'shot') {
            // console.log('AFTER SHOTs', data);
            // if (data['resultNextRound']) {
            //     if (data['aggressor']['seamanship_result_comparison']) { // if aggressor won seamanship test
            //         document.getElementById(`round-section-${data.roundRecord.round}`).appendChild(await createP(`Aggressor shoted ${data['aggressor']['cannons']} cannons and hit the ...`));
            //         // return;
            //     } else if (data['defender']['seamanship_result_comparison']) { // if defender won seamanship test
            //         document.getElementById(`round-section-${data.roundRecord.round}`).appendChild(await createP(`Defender shoted ${data['defender']['cannons']} cannons and hit the ...`));
            //         // return;
            //     }
            //     document.getElementById(`round-section-${roundRecord.round}`).appendChild(await createP('Start next round'));
            //     await startRound(reason='next_round', endBattle=false);
            // } else if (data[side]['seamanship_result_comparison']) {
            //     console.log(`${side} won seamanship test`);
            // } else if (data[side]['seamanship_result_comparison'] === false) {
            //     console.log(`${side} lost seamanship test`);
            // }
        // }

    // } catch (error) {
    //     console.error("Error during catch data", error);
    // };

// };
