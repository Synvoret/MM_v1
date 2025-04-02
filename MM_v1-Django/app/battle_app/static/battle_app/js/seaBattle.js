// function start battle between Player vs NPC (Non-Player Captain)
async function seaBattle() {

    const roundRecord = await combatFlow()

    // START BATTLE    
    if (roundRecord.round == 1) {
        await roundSection(roundRecord);
        await startRound(roundRecord, 'aggressor', roundRecord.aggressor.declaration, 'defender', roundRecord.defender.declaration);
        await seamanship(roundRecord);
        await battleAppHiddenMainList();
    }

    // NEXT ROUNDs
    else if (roundRecord.round > 1) {

        if (roundRecord.aggressor.declaration == ''
            && roundRecord.defender.declaration == '') {
            await roundSection(roundRecord);
        };

        if (roundRecord.aggressor.declaration == '') {
            const actions = roundRecord['aggressor']['actions'];
            await declaration(roundRecord, 'aggressor', actions);
        } else if (roundRecord.defender.declaration == '') {
            const actions = roundRecord['defender']['actions'];
            await declaration(roundRecord, 'defender', actions);
        // if both side declared flee
        } else if ((roundRecord.aggressor.declaration).toLowerCase() == 'flee' 
                    && (roundRecord.defender.declaration).toLowerCase() == 'flee') {
            await nextRound(roundRecord, reason='Both side flees', endBattle=true);
        } else {
            await seamanship(roundRecord);
        }

    }

};
