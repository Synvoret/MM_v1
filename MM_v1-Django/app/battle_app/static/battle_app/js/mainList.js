function battleAppHiddenMainList() {
    document.getElementById('battle-app-main-list').className = 'battle-app-hidden';
    document.getElementById('back-to-main-list-button').className = '';
};


function battleAppShowMainList (){
    
    // start
    localStorage.removeItem('battleLog');

    document.getElementById('battle-app-main-list').className = '';
    document.getElementById('back-to-main-list-button').className = 'battle-app-hidden';

    const battleLogs = document.getElementById('battle-logs');
    while (battleLogs.firstChild) {
        battleLogs.removeChild(battleLogs.firstChild);
    };

};
