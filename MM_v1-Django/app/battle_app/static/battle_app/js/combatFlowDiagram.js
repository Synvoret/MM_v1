function combatFlowDiagram() {

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {

            battleAppHiddenMainList();

            let response = JSON.parse(xhr.responseText);

            const diagramImage = document.createElement('div');
            const imgElement = document.createElement('img');
            imgElement.style.width = '75%';
            imgElement.src = response.combatFlowDiagramImage;
            diagramImage.appendChild(imgElement);
            document.getElementById('battle-logs').appendChild(diagramImage);

        };
        
    };

    xhr.open('GET', 'combatFlowDiagram', true);
    xhr.send();

};
