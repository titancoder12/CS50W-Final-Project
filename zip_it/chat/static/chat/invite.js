document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit_invite').addEventListener('click', invite)
})

function invite() {
    if (document.querySelector('#recipient').value == '' || document.querySelector('#channels').value == 'default'){
        alert("You forgot to enter one of the required fields.", 'danger');
        return null;
    }

    channels = document.querySelector('#channels');

    fetch('/api/send_invite', {
        method: 'POST',
        //headers: {'X-CSRFToken': csrftoken},
        //mode: 'same-origin',
        body: JSON.stringify({
            channel: document.querySelector('#channels').value,
            recipient: document.querySelector('#recipient').value
        })
    })
    .then((response)=>response.status)
    .then(status=>{
        console.log(status);
        if (status == 404) {
            alert("The recipient username that you typed in is not valid.", 'danger');
        }
        else if (status == 200){
            alert("Invite sent.", "success");
        }
        else {
            alert("You already sent this person an invite to this channel.", 'danger')
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