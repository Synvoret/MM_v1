// SPECIAL WEAPON TRACK, PUT IMAGE on PLAYER BOARD
function updatePlayerSpecialWeapons(colour) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            if (response.ChainShotImage !== undefined) {
                document.getElementById('player-special-weapon-chain-shot-image').setAttribute('href', response.ChainShotImage);
            } else {
                document.getElementById('player-special-weapon-chain-shot-image').setAttribute('href', '');
            };

            if (response.GrapeshotImage !== undefined) {
                document.getElementById('player-special-weapon-grapeshot-image').setAttribute('href', response.GrapeshotImage);
            } else {
                document.getElementById('player-special-weapon-grapeshot-image').setAttribute('href', '');
            };

            if (response.GrapplingHooksImage !== undefined) {
                document.getElementById('player-special-weapon-grappling-hooks-image').setAttribute('href', response.GrapplingHooksImage);
            } else {
                document.getElementById('player-special-weapon-grappling-hooks-image').setAttribute('href', '');
            };

            if (response.HeatedShotImage!== undefined) {
                document.getElementById('player-special-weapon-heated-shot-image').setAttribute('href', response.HeatedShotImage);
            } else {
                document.getElementById('player-special-weapon-heated-shot-image').setAttribute('href', '');
            };

            if (response.DoubleShotImage !== undefined) {
                document.getElementById('player-special-weapon-double-shot-image').setAttribute('href', response.DoubleShotImage);
            } else {
                document.getElementById('player-special-weapon-double-shot-image').setAttribute('href', '');
            };

            if (response.CaltropsImage !== undefined) {
                document.getElementById('player-special-weapon-caltrops-image').setAttribute('href', response.CaltropsImage);
            } else {
                document.getElementById('player-special-weapon-caltrops-image').setAttribute('href', '');
            };

            if (response.PremiumRumImage !== undefined) {
                document.getElementById('player-special-weapon-premium-rum-image').setAttribute('href', response.PremiumRumImage);
            } else {
                document.getElementById('player-special-weapon-premium-rum-image').setAttribute('href', '');
            };

            if (response.GrenadeImage !== undefined) {
                document.getElementById('player-special-weapon-grenade-image').setAttribute('href', response.GrenadeImage);
            } else {
                document.getElementById('player-special-weapon-grenade-image').setAttribute('href', '');
            };

            if (response.ExplosiveShellImage !== undefined) {
                document.getElementById('player-special-weapon-explosive-shell-image').setAttribute('href', response.ExplosiveShellImage);
            } else {
                document.getElementById('player-special-weapon-explosive-shell-image').setAttribute('href', '');
            };
        }
    };
    xhr.open('GET', 'updatePlayerSpecialWeapons?colour=' + colour, true);
    xhr.send();
};