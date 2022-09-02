document.addEventListener('DOMContentLoaded', () => {
    loadchannels();
})

function loadchannels() {
    fetch('/api/channels')
    .then(response => response.json())
    .then((result) => {
        for (let i = 0; i < result.length; i++) {
            const channeldiv = document.createElement('div');
            channeldiv.className = 'hovermouse';
            channeldiv.innerHTML = `<hr><h4 class='center'>${result[i].name}</h4><br><hr>`;
            document.querySelector('#channels').append(channeldiv);
            console.log(result[i]);
        }
    })
}

function addnewchannels() {
    //TODO
}