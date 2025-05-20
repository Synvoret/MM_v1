// function start battle between Player vs NPC (Non-Player Captain)
async function seaBattle() {

    const roundRecord = await combatFlow();
    // console.log(roundRecord);

    // START BATTLE    
    if (roundRecord.round === 1 ) {
        await roundSection(roundRecord);
        document.getElementById(`round-section-1`).appendChild(await sideSpan('aggressor'));
        document.getElementById(`round-section-1`).appendChild(await statBoard('aggressor'));
        document.getElementById(`round-section-1`).appendChild(await declaration(1, 'aggressor', [roundRecord['aggressor']['declaration']]));
        document.getElementById(`round-section-1`).appendChild(await sideSpan('defender'));
        document.getElementById(`round-section-1`).appendChild(await statBoard('defender'));
        document.getElementById(`round-section-1`).appendChild(await declaration(1, 'defender', [roundRecord['defender']['declaration']]));
        await seamanship(phase='test');
        await battleAppHiddenMainList();
    }

    // NEXT ROUNDs
    else if (roundRecord.round > 1) {
        if (roundRecord.aggressor.declaration === '' && roundRecord.defender.declaration === '') {
            await roundSection(roundRecord);
        };

        // console.log(roundRecord);
        if (roundRecord.aggressor.declaration === '') {
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await sideSpan('aggressor'));
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await statBoard('aggressor'));
            const actions = roundRecord['aggressor']['actions'];
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await declaration(roundRecord.round, 'aggressor', actions));
        } else if (roundRecord.defender.declaration === '') {
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await sideSpan('defender'));
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await statBoard('defender'));
            const actions = roundRecord['defender']['actions'];
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(await declaration(roundRecord.round, 'defender', actions));
        // IF BOTH SIDE DECLARED FLEE
        } else if ((roundRecord.aggressor.declaration).toLowerCase() === 'flee' && (roundRecord.defender.declaration).toLowerCase() === 'flee') {
            await startRound(reason='Both side flees', endBattle=true);
        } else {
            await seamanship('test');
        }

    }

};
