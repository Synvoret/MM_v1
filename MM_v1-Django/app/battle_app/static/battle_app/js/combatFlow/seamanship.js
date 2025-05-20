async function seamanship(phase) {

        try {
            const response = await fetch ('seamanship', { method: "GET" })
            const data = await response.json();

            const seamanship = data.roundRecord;

            // TEST phase
            if (phase === 'test') {
                document.getElementById(`round-section-${seamanship.round}`).appendChild(await createP('Seamanship test'));
                document.getElementById(`round-section-${seamanship.round}`).appendChild(await dices('aggressor', 'seamanship', seamanship.aggressor.seamanship, () => rollSeamanship(seamanship.round, 'aggressor')));
                document.getElementById(`round-section-${seamanship.round}`).appendChild(await dices('defender', 'seamanship', seamanship.defender.seamanship, () => rollSeamanship(seamanship.round, 'defender')));
            } else if (phase === 'result') {
                if (seamanship['seamanshipResult'] === 'no success') {
                    document.getElementById(`round-section-${seamanship.round - 1}`).appendChild(await createP('No success'));
                    document.getElementById(`round-section-${seamanship.round - 1}`).appendChild(await createP('Next round'));
                    await seaBattle();
                    // await startRound(reason='next_round', endBattle=false);
                    // return;
                } else if (seamanship['seamanshipResult'] === 'draw') {
                    document.getElementById(`round-section-${seamanship.round - 1}`).appendChild(await createP('Draw'));
                    document.getElementById(`round-section-${seamanship.round - 1}`).appendChild(await createP('Next round'));
                    await seaBattle();
                } else {

                    if (seamanship['aggressor']['seamanship_result_comparison'] === 'winner') {
                        document.getElementById(`round-section-${seamanship.round}`).appendChild(await createP(`aggressor won seamanship`));
                    } else {
                        document.getElementById(`round-section-${seamanship.round}`).appendChild(await createP(`defender won seamanship`));
                    }

                    for (side of ['aggressor', 'defender']) {
                        if (seamanship[side]['seamanship_result_comparison'] === 'winner' && seamanship[side]['declaration'] === 'flee') {
                            await startRound(reason=`${side} flees`, endBattle=true);
                            return;
                        }
                        if (seamanship[side]['seamanship_result_comparison'] === 'winner' && seamanship[side]['declaration'] === 'board') {
                            // console.log(`${side} dokonuje abordazu`)
                            return;
                        }
                        if (seamanship[side]['seamanship_result_comparison'] === 'winner' && seamanship[side]['declaration'] === 'shot') {
                            // console.log(`${side} strzela`)
                            await shooting('test', side);
                        }
                        if (seamanship[side]['seamanship_result_comparison'] === 'loser' && seamanship[side]['declaration'] === 'flee') {
                            // console.log(`${side} chciał uciec, nieudało się`)
                            // return;
                        }
                        if (seamanship[side]['seamanship_result_comparison'] === 'loser' && seamanship[side]['declaration'] === 'board') {
                            // console.log(`${side} chciałdokonać abordazu, nie udało się`)
                            return;
                        }
                        if (seamanship[side]['seamanship_result_comparison'] === 'loser' && seamanship[side]['declaration'] === 'shot') {
                            // console.log(`${side} strzela tyloma działami ile sukcesów w seamanship`)
                            await shooting('test', side);
                        }
                    }
                }
            }






        } catch (error) {
            console.error("Error during catch data", error);
        }
        
    
    }