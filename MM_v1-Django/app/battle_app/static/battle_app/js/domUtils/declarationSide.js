// declaration description
function declarationSide(roundNumber, side) {
    const spanDeclaration = document.createElement('p');
    spanDeclaration.style.textAlign = 'left';

    const declaration = document.createElement('span');
    declaration.textContent = `Declaration: `;
    declaration.style.textAlign = 'left';
    spanDeclaration.appendChild(declaration);

    const sideDeclaration = document.createElement('span');
    sideDeclaration.style.textAlign = 'left';
    sideDeclaration.textContent = `${side}`;
    spanDeclaration.appendChild(sideDeclaration);
    if (side === 'Player') {
        sideDeclaration.style.color = 'red';
    } else if (side === 'NPC') {
        sideDeclaration.style.color = 'blue';
    };

    document.getElementById(`round-section-${roundNumber}`).appendChild(spanDeclaration);
};