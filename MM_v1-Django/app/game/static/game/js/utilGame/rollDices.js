// type - type roll: 'create', 'roll', 'close'
// amountDices - 
// storageValuesID - id element where put summary success
// parentID - where append element
// x - position x
// y - position y 
// colour - player colour
function rollDices(type, amountDices, storageValuesID, parentID, x, y, colour) {

    if (type === 'create') {

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);

                // cleaning
                let elementsToRemove = document.querySelectorAll('.dice-image');
                elementsToRemove.forEach(function(element) {
                    element.remove();
                });
                const keys = Object.keys(localStorage);
                const pattern = /^dice\d+Value$/;
                keys.forEach(key => {
                    if (pattern.test(key)) {
                        localStorage.removeItem(key);
                    }
                });

                let parentElement = document.getElementById(parentID); // parent element id

                for (let i = 1; i <= amountDices; i++) {
                    let diceImageElement = document.createElementNS("http://www.w3.org/2000/svg", "image");
                    let setX = x + i * 20 - 20; // x
                    let setY = y; // y
                    diceImageElement.setAttribute("class", `dice-image`)
                    diceImageElement.setAttribute("id", `dice-${i}`); // id
                    diceImageElement.setAttribute("x", setX);
                    diceImageElement.setAttribute("y", setY);
                    diceImageElement.setAttribute("width", "19");
                    diceImageElement.setAttribute("heigth", "19");
                    diceImageElement.setAttribute("href", response.dice1Image);
                    parentElement.appendChild(diceImageElement);
                    if (i == amountDices) {
                        let rollTextElement = document.createElementNS("http://www.w3.org/2000/svg", "text");
                        rollTextElement.setAttribute("id", "roll-dices");
                        rollTextElement.setAttribute("x", setX + 20);
                        rollTextElement.setAttribute("y", setY + 15);
                        let rollDicesParams = `rollDices(type='roll', amountDices=${amountDices}, storageValuesID="${storageValuesID}")`;
                        rollTextElement.setAttribute("onclick", rollDicesParams);
                        rollTextElement.style.textDecoration = 'none';
                        rollTextElement.style.pointerEvents = 'auto'
                        rollTextElement.style.stroke = colour;
                        rollTextElement.innerHTML = 'ROLL';
                        parentElement.appendChild(rollTextElement);
                    };
                };

            };
        };

        xhr.open('GET', 'rollDices?colour=' + colour + '&type=' + type, true);
        xhr.send();
    };


    if (type === 'roll') {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                let storageValuesElement = document.getElementById(storageValuesID);
                
                for (let i = 1; i <= amountDices; i++) {
                    document.getElementById(`dice-${i}`).setAttribute('href', response[`dice${i}Image`]);
                    if (response[`dice${i}Value`] == 'skull') {
                        let storageValuesNew = parseInt(storageValuesElement.textContent) + 1;
                        storageValuesElement.innerHTML = storageValuesNew;
                    }
                    localStorage.setItem(`dice${i}Value`, response[`dice${i}Value`]);
                };

                document.getElementById("roll-dices").style.textDecoration = 'line-through';
                document.getElementById("roll-dices").style.pointerEvents = 'none'
            };
        };
        
        xhr.open('GET', 'rollDices?colour=' + colour + '&type=' + type + '&amountDices=' + amountDices, true);
        xhr.send();
    };


    if (type === 'reroll to success') {
        const keys = Object.keys(localStorage);
        const pattern = /^dice\d+Value$/;

        for (let key of keys) {
            if (pattern.test(key) && localStorage.getItem(key) !== 'skull') {
                localStorage.setItem(key, 'skull');
                document.getElementById(`dice-${key[4]}`).setAttribute('href', '/media/dices/dice_skull6.png')
                let amountSuccess = parseInt(document.getElementById(storageValuesID).textContent);
                amountSuccess++;
                document.getElementById(storageValuesID).innerHTML = amountSuccess;
                break;
            };
        };

    };


    if (type === 'destroy') {
        let diceImagesClass = document.querySelectorAll('.dice-image');
        diceImagesClass.forEach(function(element) {
            element.remove();
            element = null;
        });
        let rollDicesID = document.getElementById('roll-dices');
        rollDicesID.remove();
        rollDicesID = null;
    };

};
