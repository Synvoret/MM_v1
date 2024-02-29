// show cargo card on over mouse 
function showCargoCards(type) {
    let startX = 417;
    if (type === 'show') {
        for (let i = 2; i <= 8; i++){
            if (document.getElementById(`player-cargo-card-use-${i}`).getAttribute('href') !== '') {
                document.getElementById(`player-cargo-card-use-${i}`).setAttribute('x', startX - i * 58 + 70);
            };
        };
    } else if (type === 'hide') {
        for (let i = 2; i <= 8; i++){
            document.getElementById(`player-cargo-card-use-${i}`).setAttribute('x', startX);
        };
    }
};