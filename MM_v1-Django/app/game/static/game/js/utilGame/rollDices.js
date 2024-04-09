// type - type roll: 'create', 'roll', 'reroll to success', 'destroy'
// amountDices - integer number
// storageValuesID - id element where put summary success, 'single' if only one test, for example a scouting
// parentID - id where append element
// x - position x
// y - position y 
// colour - player colour 'blue', 'green', 'red', 'yellow'.
// skill - testes skill value
// success - setting ok text and function
// afterTest - consume action point if true, default always false.
function rollDices(type=null, amountDices=null, storageValuesID=null, parentID=null, x=null, y=null, colour=null, skill=null, success=null, afterTest=false) {

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
                    };
                });

                let parentElement = document.getElementById(parentID); // parent element id
                let group = document.createElementNS("http://www.w3.org/2000/svg", "g");
                group.setAttribute('id', 'dice-group');
                // group.setAttribute('transform', 'scale(1.5)');
                parentElement.appendChild(group);
                let frame = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                let okText = document.createElementNS("http://www.w3.org/2000/svg", "text");
                let cancelText = document.createElementNS("http://www.w3.org/2000/svg", "text");

                if (storageValuesID === 'single') {
                    // frame
                    frame.setAttribute('id', 'dicesFrame');
                    frame.setAttribute('x', x - 130);
                    frame.setAttribute('y', y - 5);
                    frame.setAttribute('height', "29");
                    frame.style.stroke = colour;
                    group.appendChild(frame);

                    // test skill name
                    let skillName = document.createElementNS("http://www.w3.org/2000/svg", "text");
                    skillName.setAttribute("id", "skill-name");
                    skillName.setAttribute("x", x - 120);
                    skillName.setAttribute("y", y + 15);
                    skillName.style.stroke = colour;
                    skillName.innerHTML = skill;
                    group.appendChild(skillName);

                    // amountSuccess
                    let amountSuccess = document.createElementNS("http://www.w3.org/2000/svg", "text");
                    amountSuccess.setAttribute("id", "single-amount-success");
                    amountSuccess.setAttribute("x", x - 20);
                    amountSuccess.setAttribute("y", y + 15);
                    amountSuccess.style.stroke = colour;
                    amountSuccess.innerHTML = 0;
                    group.appendChild(amountSuccess);
                    storageValuesID = 'single-amount-success';

                    // ok
                    okText.setAttribute("id", "ok-text");
                    okText.style.stroke = colour;
                    okText.style.pointerEvents = 'none';
                    okText.style.textDecoration = 'line-through';
                    okText.innerHTML = 'Ok';
                    let okTextParams = `${success}; navRollDices('testOk'); rollDices(type='destroy')`;
                    okText.setAttribute("onclick", okTextParams);
                    group.appendChild(okText);
                    // cancel
                    cancelText.setAttribute("id", "cancel-text");
                    cancelText.style.stroke = colour;
                    cancelText.style.cursor = 'pointer';
                    let cancelTextParams = `navRollDices('testCancel'); rollDices(type='destroy')`;
                    cancelText.setAttribute("onclick", cancelTextParams);
                    cancelText.innerHTML = 'Cancel';
                    group.appendChild(cancelText);
                };

                for (let i = 1; i <= amountDices; i++) {
                    let diceImageElement = document.createElementNS("http://www.w3.org/2000/svg", "image");
                    let setX = x + i * 20 - 20; // x
                    let setY = y; // y
                    diceImageElement.setAttribute("class", `dice-image`);
                    diceImageElement.setAttribute("id", `dice-${i}`); // id
                    diceImageElement.setAttribute("x", setX);
                    diceImageElement.setAttribute("y", setY);
                    diceImageElement.setAttribute("width", "19");
                    diceImageElement.setAttribute("heigth", "19");
                    diceImageElement.setAttribute("href", response.dice1Image);
                    group.appendChild(diceImageElement);
                    if (i == amountDices) {
                        let rollTextElement = document.createElementNS("http://www.w3.org/2000/svg", "text");
                        rollTextElement.setAttribute("id", "roll-dices");
                        rollTextElement.setAttribute("x", setX + 20);
                        rollTextElement.setAttribute("y", setY + 15);
                        let rollDicesParams = ``;
                        if (afterTest) {
                            rollDicesParams = `rollDices(type='roll', amountDices=${amountDices}, storageValuesID='${storageValuesID}', afterTest=true)`;
                        } else {
                            rollDicesParams = `rollDices(type='roll', amountDices=${amountDices}, storageValuesID='${storageValuesID}')`;
                        };
                        rollTextElement.setAttribute("onclick", rollDicesParams);
                        rollTextElement.style.textDecoration = 'none';
                        rollTextElement.style.cursor = 'pointer';
                        rollTextElement.style.pointerEvents = 'auto';
                        rollTextElement.style.stroke = colour;
                        rollTextElement.innerHTML = 'ROLL';
                        group.appendChild(rollTextElement);
                        if (storageValuesID === 'single-amount-success') {
                            frame.setAttribute('width', i * 19 + 270);
                            okText.setAttribute("x", setX + 70);
                            okText.setAttribute("y", setY + 15);
                            cancelText.setAttribute("x", setX + 100);
                            cancelText.setAttribute("y", setY + 15);
                        };
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

                // afterTest = true
                // console.log('afterTest', afterTest, typeof(afterTest), document.getElementById('roll-dices'));
                let afterTest = true
                if (afterTest) {
                    console.log('zuzycie akcji');
                    endCurrentAction(colour=response.playerColour, afterTest=true);
                } else {
                    console.log('nie zuzywam akcji');
                };

                for (let i = 1; i <= amountDices; i++) {
                    document.getElementById(`dice-${i}`).setAttribute('href', response[`dice${i}Image`]);
                    if (response[`dice${i}Value`] == 'skull') {
                        let storageValuesNew = parseInt(storageValuesElement.textContent) + 1;
                        storageValuesElement.innerHTML = storageValuesNew;
                        if (document.getElementById(`ok-text`)) {
                            document.getElementById(`ok-text`).style.cursor = 'pointer';
                            document.getElementById(`ok-text`).style.textDecoration = 'none';
                            document.getElementById(`ok-text`).style.pointerEvents = 'auto';
                        };
                    };
                    localStorage.setItem(`dice${i}Value`, response[`dice${i}Value`]);
                };

                document.getElementById("roll-dices").style.textDecoration = 'line-through';
                document.getElementById("roll-dices").style.pointerEvents = 'none';
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
        let group = document.getElementById('dice-group');
        if (group) {
            group.remove();
        };
    };

};
