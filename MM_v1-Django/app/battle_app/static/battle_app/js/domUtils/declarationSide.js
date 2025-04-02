// declaration description
async function declarationSide(roundRecord, side) {

    const spanDeclaration = document.createElement('p');
    spanDeclaration.style.textAlign = 'left';

    const declaration = document.createElement('span');
    declaration.textContent = `Declaration: `;
    spanDeclaration.appendChild(declaration);

    const sideDeclaration = document.createElement('span');
    sideDeclaration.textContent = `${side}`;
    spanDeclaration.appendChild(sideDeclaration);
    if (side == 'aggressor' || side == 'Aggressor') {
        sideDeclaration.style.color = 'red';
    } else if (side == 'defender' || side == 'Defender') {
        sideDeclaration.style.color = 'blue';
    };

    document.getElementById(`round-section-${roundRecord.round}`).appendChild(spanDeclaration);
};