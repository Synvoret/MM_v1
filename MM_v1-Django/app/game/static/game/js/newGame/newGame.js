function prepareNav() {

    // FIRST STEP - add players
    document.getElementById('add-players-div').style.display = "block";
    document.querySelector('.nav-button-player-start').setAttribute('disabled', true);
};

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

prepareNav();
prepareBoard();
