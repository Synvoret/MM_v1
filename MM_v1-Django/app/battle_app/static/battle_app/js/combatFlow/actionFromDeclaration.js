async function actionFromDeclaration(roundCounter, action) {
    if (action == 'shot') {
        await shooting(roundCounter);
    }
}