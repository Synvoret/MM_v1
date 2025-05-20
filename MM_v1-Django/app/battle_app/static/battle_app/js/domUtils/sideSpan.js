async function sideSpan(side) {

    const spanSide = document.createElement('p');
    spanSide.style.textAlign = 'left';

    const declaration = document.createElement('span');
    declaration.textContent = `Side: `;
    spanSide.appendChild(declaration);

    const sideDeclaration = document.createElement('span');
    sideDeclaration.textContent = `${side.toUpperCase()}`;
    spanSide.appendChild(sideDeclaration);
    if (side == 'aggressor' || side == 'Aggressor') {
        sideDeclaration.style.color = 'red';
    } else if (side == 'defender' || side == 'Defender') {
        sideDeclaration.style.color = 'blue';
    };

    return spanSide;
};