function prepareBoard() {

    // NEW BOARD
    newBoard();

    // SEA ZONEs
    const seaZonesList = [
        "basse-terre",
        "bridgetown",
        "caracas",
        "cartagena",
        "curacao",
        // 'gulf-city',
        "nassau",
        "havana",
        "old-providence",
        "petite-goave",
        "port-royal",
        "san-juan",
        "santo-domingo",
        "st-john",
        "st-maarten",
        "the-caribbean-sea",
        "trinidad",
        "tortuga",
    ];

    const colours = [
        'blue',
        'green',
        'red',
        'yellow',
    ]

    // PREPARE ALL SEA ZONEs
    for (const seaZone of seaZonesList) {
        // PUT LOCATION TOKENs
        const locationToken = `location-token-${seaZone}-image`;
        if (seaZone === "the-caribbean-sea") {} 
        else {putLocationToken(locationToken);}
    };

    // STARTING DRAW DEMAND TOKENs, STARTING DRAW SHIP 
    drawMerchantToken(seaZone="all");
    drawShipModification(port="all");
    drawDemandToken(port="all");

    // PUT CUBEs ON TRACK ENEMY HIT LOCATIONs
    updateEnemyHitLocation();

    // PUT CUBEs ON TRACK GLORY POINTs
    for (const colour of colours) {
        updateGloryTrack(colour);
    };

    // DRAW MISSION CARD
    drawMissionCard(1);
    drawMissionCard(2);

};

prepareBoard();

// PLAYER BOARD
const col = 'red'

newPlayerBoard();
updateLoyalityTrack(col);
updateFavorsTrack(col);
drawPlayerCaptainCard(col);
drawPlayerShipCard(col);
updatePlayerHitLocation(col);
updatePlayerGolds(col);
drawGloryCard(col);
// SHIP PLASTIC
putShipPlastic('galleon', col);
