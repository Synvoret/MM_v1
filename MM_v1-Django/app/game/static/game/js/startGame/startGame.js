// NEW BOARD

newBoard();
// SHIP PLASTIC
putShipPlastic('sloop', 'blue');
// STARTING DRAW DEMAND TOKENs
drawDemandToken("demand-basse-terre-image")
drawDemandToken("demand-bridgetown-image")
drawDemandToken("demand-caracas-image")
drawDemandToken("demand-cartagena-image")
drawDemandToken("demand-curacao-image")
drawDemandToken("demand-nassau-image")
drawDemandToken("demand-havana-image")
drawDemandToken("demand-old-providence-image")
drawDemandToken("demand-petite-goave-image")
drawDemandToken("demand-port-royal-image")
drawDemandToken("demand-san-juan-image")
drawDemandToken("demand-santo-domingo-image")
drawDemandToken("demand-st-john-image")
drawDemandToken("demand-st-maarten-image")
drawDemandToken("demand-trinidad-image")
drawDemandToken("demand-tortuga-image")
// STARTING DRAW SHIP MODIFICATIONs
drawShipModification("ship-modification-basse-terre-image")
drawShipModification("ship-modification-bridgetown-image")
drawShipModification("ship-modification-caracas-image")
drawShipModification("ship-modification-cartagena-image")
drawShipModification("ship-modification-curacao-image")
drawShipModification("ship-modification-nassau-image")
drawShipModification("ship-modification-havana-image")
drawShipModification("ship-modification-old-providence-image")
drawShipModification("ship-modification-petite-goave-image")
drawShipModification("ship-modification-port-royal-image")
drawShipModification("ship-modification-san-juan-image")
drawShipModification("ship-modification-santo-domingo-image")
drawShipModification("ship-modification-st-john-image")
drawShipModification("ship-modification-st-maarten-image")
drawShipModification("ship-modification-trinidad-image")
drawShipModification("ship-modification-tortuga-image")
// STARTING DRAW MERCHANT TOKENs
drawMerchantToken("merchant-token-basse-terre-image")
drawMerchantToken("merchant-token-bridgetown-image")
drawMerchantToken("merchant-token-caracas-image")
drawMerchantToken("merchant-token-cartagena-image")
drawMerchantToken("merchant-token-curacao-image")
drawMerchantToken("merchant-token-nassau-image")
drawMerchantToken("merchant-token-havana-image")
drawMerchantToken("merchant-token-old-providence-image")
drawMerchantToken("merchant-token-petite-goave-image")
drawMerchantToken("merchant-token-port-royal-image")
drawMerchantToken("merchant-token-san-juan-image")
drawMerchantToken("merchant-token-santo-domingo-image")
drawMerchantToken("merchant-token-st-john-image")
drawMerchantToken("merchant-token-st-maarten-image")
drawMerchantToken("merchant-token-the-caribbean-sea-image")
drawMerchantToken("merchant-token-trinidad-image")
drawMerchantToken("merchant-token-tortuga-image")
// PUT CUBEs ON TRACK ENEMY HIT LOCATIONs
updateEnemyHitLocation();
// PUT LOCATION TOKENs
putLocationToken('location-token-basse-terre-image');
putLocationToken('location-token-bridgetown-image');
putLocationToken('location-token-caracas-image');
putLocationToken('location-token-cartagena-image');
putLocationToken('location-token-curacao-image');
putLocationToken('location-token-havana-image');
putLocationToken('location-token-nassau-image');
putLocationToken('location-token-old-providence-image');
putLocationToken('location-token-petite-goave-image');
putLocationToken('location-token-port-royal-image');
putLocationToken('location-token-san-juan-image');
putLocationToken('location-token-santo-domingo-image');
putLocationToken('location-token-st-john-image');
putLocationToken('location-token-st-maarten-image');
putLocationToken('location-token-trinidad-image');
putLocationToken('location-token-tortuga-image');
// DRAW MISSION CARD
drawMissionCard(1);
drawMissionCard(2);
updateGloryTrack();





// PLAYER BOARD
const col = 'blue'
newPlayerBoard();
updateLoyalityTrack(col);
updateFavorsTrack(col);
drawPlayerCaptainCard(col)
drawPlayerShipCard(col);
playerHitLocation(col);
playerGolds(col);
drawGloryCard(col)