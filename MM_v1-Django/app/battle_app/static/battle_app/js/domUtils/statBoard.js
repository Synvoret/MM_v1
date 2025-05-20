async function statBoard(side) {

    try {
        const url = 'statBoard';
        const response = await fetch (url, { method: "GET" })
        const data = await response.json();
    
        const sideStat = data.roundRecord[side];
        
        // div stat
        const statBoardDiv = document.createElement('div');
        statBoardDiv.className = 'statBoard';
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
        hullSpan.style.color = 'green';
        shipBoardSpan.appendChild(hullSpan);
        // cargo span
        const cargoSpan = document.createElement('span');
        cargoSpan.textContent = `Cargo-${sideStat.cargo} `;
        cargoSpan.style.color = 'green';
        shipBoardSpan.appendChild(cargoSpan);
        // masts span
        const mastsSpan = document.createElement('span');
        mastsSpan.textContent = `Masts-${sideStat.masts} `;
        mastsSpan.style.color = 'green';
        shipBoardSpan.appendChild(mastsSpan);
        // crew span
        const crewSpan = document.createElement('span');
        crewSpan.textContent = `Crew-${sideStat.crew} `;
        crewSpan.style.color = 'green';
        shipBoardSpan.appendChild(crewSpan);
        // cannon span
        const cannonSpan = document.createElement('span');
        cannonSpan.textContent = `Cannon-${sideStat.cannons} `;
        cannonSpan.style.color = 'green';
        shipBoardSpan.appendChild(cannonSpan);
        // maneuverability span
        const maneuverabilitySpan = document.createElement('span');
        maneuverabilitySpan.textContent = `Maneuverability-${sideStat.maneuverability} `;
        maneuverabilitySpan.style.color = 'green';
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
        seamanshipSpan.style.color = 'green';
        captainsBoardSpan.appendChild(seamanshipSpan);
        // leadership span
        const leadershipSpan = document.createElement('span');
        leadershipSpan.textContent = `Leadership-${sideStat.leadership} `;
        leadershipSpan.style.color = 'green';
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

        statBoardDiv.appendChild(shipBoardP);
        statBoardDiv.appendChild(captainsBoardP);
        statBoardDiv.appendChild(weaponsBoardP);

        return statBoardDiv;

    } catch (error) {
        console.error("Error during catch data", error);
    }
    

}
