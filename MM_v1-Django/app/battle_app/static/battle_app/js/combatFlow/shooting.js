async function shooting(phase, side) {

    try {
        const response = await fetch ('shooting', {method: "GET"});
        const data = await response.json();

        const shooting = data.roundRecord;

        // TEST phase
        if (phase === 'test') {
            if (shooting[side]['seamanship_result_comparison'] === 'winner') {
                document.getElementById(`round-section-${shooting.round}`).appendChild(await createP('Shooting'));
                document.getElementById(`round-section-${shooting.round}`).appendChild(await dices(side, 'shot', shooting[side]['cannons'], () => dicesRoll(shooting.round, side, 'shot')));
            } else if (shooting[side]['seamanship_result_comparison'] === 'loser' && shooting[side]['cannons'] > 0) { // shot from all success in seamanship
                // console.log(shooting)
                document.getElementById(`round-section-${shooting.round}`).appendChild(await createP('Shooting'));
                document.getElementById(`round-section-${shooting.round}`).appendChild(await dices(side, 'shot', shooting[side]['cannons'], () => dicesRoll(shooting.round, side, 'shot')));
            }






            // if (shooting['defender']['declaration'] === 'shot' && shooting['defender']['seamanship_result_comparison'] === 'winner') {
            //     document.getElementById(`round-section-${shooting.round}`).appendChild(await dices('aggressor', 'shot', shooting.aggressor.cannons));
            // }
            
            // document.getElementById(`round-section-${shooting.round}`).appendChild(await dices('defender', 'shot', shooting.defender.cannons));
        } 
        // else if (phase === 'result') {
        // if ((shooting['aggressor']['declaration']).toLowerCase() === 'shot' && (shooting['defender']['declaration']).toLowerCase() === 'shot') {
        //         await shooting(['aggressor', 'defender']);
        //     }
        // }

    } catch (error) {
        console.error("Error during catch data", error);
    }
    

}















// async function shooting(sides) {

//     const roundRecord = await combatFlow();

//     // SHOW DICES for SHOOT
//     for (side of sides) {
//         document.getElementById(`round-section-${roundRecord.round}`).appendChild(await dices(side, 'shot', roundRecord[side]['cannons']));
//     }
    // loser seamanship test
    // const loserSkulls = (roundRecord['resultTestLoser']['seamanship_roll_result']).filter(element => element === "skull").length; // amount skull
    // const loserCannons = roundRecord['resultTestLoser']['cannons'];
    // const loserCannonsShot = Math.min(loserCannons, loserSkulls); // shot for each success in seamanship test
    // if (loserCannonsShot > 0) {
    //     document.getElementById(`round-section-${roundRecord.round}`).appendChild(await dices(side, 'shot', loserCannonsShot, dicesRoll));
    // }


    // roll dices


    // possibility choose location

// // 
// };

