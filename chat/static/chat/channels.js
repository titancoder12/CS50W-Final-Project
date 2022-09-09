document.addEventListener('DOMContentLoaded', () => {
    loadchannels();
    document.querySelector('#addchannelbtn').addEventListener('click', ()=>{
        addnewchannel();
    });
})

function loadchannels() {
    clear_channels();
    fetch('/api/channels')
    .then(response => response.json())
    .then((result) => {
        for (let i = 0; i < result.length; i++) {
            const channeldiv = document.createElement('div');
            channeldiv.addEventListener('click', () => {
                location.replace('/channel/'+result[i].id);
            })
            channeldiv.className = 'hovermouse';
            channeldiv.innerHTML = `<hr><h4 class='center'>${result[i].name}</h4><br><hr>`;
            document.querySelector('#channels').append(channeldiv);
            console.log(result[i]);
        }
    })
}

function addnewchannel() {
    fetch('/api/createchannel', {
        method: 'POST',
        //headers: {'X-CSRFToken': csrftoken},
        //mode: 'same-origin',
        body: JSON.stringify({
            channel_name: document.querySelector('#newchannelname').value
        })
    })
    .then(()=>loadchannels())
    .then(()=>alert('Channel Created Successfully!', 'success'))
    .then(()=>{
        document.querySelector('#newchannelname').value = '';
    });
}

function clear_channels() {
    document.querySelector('#channels').innerHTML = '';
}

function alert(message, alert_type) {
    const alert = document.createElement('div');
    alert.className = `center alert alert-${alert_type} alert-dismissible fade show`;
    alert.innerHTML = `<b>${message}</b>
    <button type="button" class="btn-close" id='dismissalert' data-bs-dismiss="alert" aria-label="Close"></button>`;   
    document.querySelector('#alerts').append(alert);
    document.querySelector('#dismissalert').addEventListener('click', ()=>{
        document.querySelector('#alerts').innerHTML = '';
    });
}