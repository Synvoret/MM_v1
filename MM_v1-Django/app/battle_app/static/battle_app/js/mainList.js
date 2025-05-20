async function battleAppHiddenMainList() {

    document.getElementById('hr-line-before-back-to-list-button').className = '';    
    document.getElementById('battle-app-main-list').className = 'battle-app-hidden';
    document.getElementById('back-to-main-list-button').className = '';
    localStorage.clear();
};


async function battleAppShowMainList (){
    const response = fetch ('battleApp', {method: "GET"})
        // .then(response => response.json())
        .then(data => {
            document.getElementById('hr-line-before-back-to-list-button').className = 'battle-app-hidden';

            document.getElementById('battle-app-main-list').className = '';
            document.getElementById('back-to-main-list-button').className = 'battle-app-hidden';
        
            const battleLogs = document.getElementById('battle-logs');
            while (battleLogs.firstChild) {
                battleLogs.removeChild(battleLogs.firstChild);
            };
        })

};
