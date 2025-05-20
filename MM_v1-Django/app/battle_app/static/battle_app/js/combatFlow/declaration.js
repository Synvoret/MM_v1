async function declaration(round, side, action) {

        const spanDeclaration = document.createElement('span');
        spanDeclaration.className = `${side}-declaration-action-${round}`;
        
        if (round === 1) {
            spanDeclaration.appendChild(await createP(`Declaration - ${action}`));
        } else {
            for (act of action) {
                spanDeclaration.appendChild(await actionButton(round, side, act));
            };
        }

        return spanDeclaration;

}
