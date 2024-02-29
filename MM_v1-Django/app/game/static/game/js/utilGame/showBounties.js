function showBounties(type, bountyValue) {
    let startX = 253;
    let startY = parseInt(document.getElementById(`player-bounty-${bountyValue}-1`).getAttribute('y'));
    if (type === 'show') {
        for (let i = 2; i <= 5; i++){
            if (document.getElementById(`player-bounty-${bountyValue}-${i}`).getAttribute('href') !== '') {
                document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute('x', startX - i * 11);
                document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute('y', startY);
                document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute("transform", `rotate(2 ${startX - (i * 11)} ${startY})`);
            }
        }
    } else if (type === 'hide') {
        for (let i = 2; i <= 5; i++){
            document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute('x', startX - i * 2 + 2);
            document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute('y', startY);
            document.getElementById(`player-bounty-${bountyValue}-${i}`).setAttribute("transform", `rotate(2 ${startX + i * 2 - 2} ${startY})`);
        }
    }
}