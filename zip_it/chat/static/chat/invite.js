document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit_invite').addEventListener('click', invite)
})

function invite() {
    if (document.querySelector('#recipient').value == '' || document.querySelector('#channels').value == 'default'){
        alert("You forgot to enter one of the required fields.", 'danger');
        return null;
    }

    channels = document.querySelector('#recipient');
    index = channels.value;
    selected_option = channels[index];

    fetch('/api/send_invite', {
        method: 'POST',
        //headers: {'X-CSRFToken': csrftoken},
        //mode: 'same-origin',
        body: JSON.stringify({
            channel: document.querySelector('#channels').id,
            recipient: selected_option.id
        })
    })
    .then((response)=>response.status)
    .then(status=>{
        if (status=404) {
            alert("The recipient username that you typed in is not valid.", 'danger');
        }
        else {
            alert("Invite sent.", "success");
        }
    });
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