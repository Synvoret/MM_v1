// function responsible for displaying content
async function createP(content) {

    const element = document.createElement('p');
    // element.style.textAlign = 'left';
    element.className = `description`;
    element.textContent = content;
    return element;
};
