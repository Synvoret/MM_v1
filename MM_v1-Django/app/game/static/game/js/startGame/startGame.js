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
        'gulf-city',
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

    // STARTING DRAW DEMAND TOKENs
    putLocationToken(seaZone="all")
    drawMerchantToken(seaZone="all");
    // STARTING DRAW SHIP MODIFICATIONs
    drawShipModification(port="all");
    drawDemandToken(port="all");

    // PUT CUBEs ON TRACK ENEMY HIT LOCATIONs
    updateEnemyHitLocation();
    // PUT CUBEs ON TRACK GLORY POINTs
    updateGloryTrack()

    // DRAW MISSIONs CARD
    drawMissionCard(1);
    drawMissionCard(2);

};


function preparePlayerBoard() {
    // PLAYER BOARD
    const col = 'red'

    newPlayerBoard();
    updateLoyalityTrack(col);
    updateFavorsTrack(col);
    // drawPlayerCaptainCard(col);
    // drawPlayerShipCard(col);
    updatePlayerHitLocation(col);
    updatePlayerGolds(col);
    drawGloryCard(col);
    // SHIP PLASTIC
    // putShipPlastic('galleon', col, "st-maarten", true);


    // put random element to selected element
    // randomInsidePosition("frigate", "spanish", "cartagena", false);

};


prepareBoard();
// preparePlayerBoard();