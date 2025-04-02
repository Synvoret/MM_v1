async function statBoard(roundRecord, side) {

    const url = 'combatFlow';
    const response = await fetch (url, { method: "GET" })
        .then(response => response.json())
        .then(data => {

            const sideStat = data.roundRecord[side];
            
            
            
            // ship board p
            const shipBoardP = document.createElement('p');
            shipBoardP.style.textAlign = 'left';
            // ship board span
            const shipBoardSpan = document.createElement('span');
            // if (side == 'aggressor' || side == 'Aggressor') {
            //     shipBoardP.style.color = 'red';
            // } else if (side == 'defender' || side == 'Defender') {
            //     shipBoardP.style.color = 'blue';
            // };
            // ship span
            const shipSpan = document.createElement('span');
            shipSpan.textContent = `Ship-${sideStat.ship} `;
            shipBoardSpan.appendChild(shipSpan);
            // hull span
            const hullSpan = document.createElement('span');
            hullSpan.textContent = `Hull-${sideStat.hull} `;
            shipBoardSpan.appendChild(hullSpan);
            // cargo span
            const cargoSpan = document.createElement('span');
            cargoSpan.textContent = `Cargo-${sideStat.cargo} `;
            shipBoardSpan.appendChild(cargoSpan);
            // masts span
            const mastsSpan = document.createElement('span');
            mastsSpan.textContent = `Masts-${sideStat.masts} `;
            shipBoardSpan.appendChild(mastsSpan);
            // crew span
            const crewSpan = document.createElement('span');
            crewSpan.textContent = `Crew-${sideStat.crew} `;
            shipBoardSpan.appendChild(crewSpan);
            // cannon span
            const cannonSpan = document.createElement('span');
            cannonSpan.textContent = `Cannon-${sideStat.cannons} `;
            shipBoardSpan.appendChild(cannonSpan);
            // maneuverability span
            const maneuverabilitySpan = document.createElement('span');
            maneuverabilitySpan.textContent = `Maneuverability-${sideStat.maneuverability} `;
            shipBoardSpan.appendChild(maneuverabilitySpan);

            shipBoardP.appendChild(shipBoardSpan);



            // captains p
            const captainsBoardP = document.createElement('p');
            captainsBoardP.style.textAlign = 'left';
            const captainsBoardSpan = document.createElement('span');
            // captain span
            const captainSpan = document.createElement('span');
            // captainSpan.textContent = `Captain-${sideStat.captain} `;
            captainSpan.textContent = `Captain-`;
            captainsBoardSpan.appendChild(captainSpan);
            // seamanship span
            const seamanshipSpan = document.createElement('span');
            seamanshipSpan.textContent = `Seamanship-${sideStat.seamanship} `;
            captainsBoardSpan.appendChild(seamanshipSpan);
            // leadership span
            const leadershipSpan = document.createElement('span');
            leadershipSpan.textContent = `Leadership-${sideStat.leadership} `;
            captainsBoardSpan.appendChild(leadershipSpan);

            captainsBoardP.appendChild(captainsBoardSpan);



            // special weapons p
            const weaponsBoardP = document.createElement('p');
            weaponsBoardP.style.textAlign = 'left';
            const weaponsBoardSpan = document.createElement('span');
            // special weapons span
            const weaponSpan = document.createElement('span');
            weaponSpan.textContent = `Special Weapons-${sideStat.special_weapons} `;
            weaponsBoardSpan.appendChild(weaponSpan);

            weaponsBoardP.appendChild(weaponsBoardSpan);


            document.getElementById(`round-section-${roundRecord.round}`).appendChild(shipBoardP);
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(captainsBoardP);
            document.getElementById(`round-section-${roundRecord.round}`).appendChild(weaponsBoardP);

        })

}