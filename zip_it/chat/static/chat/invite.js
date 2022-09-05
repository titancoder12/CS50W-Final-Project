document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit_invite').addEventListener('click', invite)
})

function invite() {
    if (document.querySelector('#recipient').value == '' || document.querySelector('#channels').value == 'default'){
        alert("You forgot to enter one of the required fields.", 'danger');
        return null;
    }

    fetch('/api/message', {
        method: 'POST',
        //headers: {'X-CSRFToken': csrftoken},
        //mode: 'same-origin',
        body: JSON.stringify({
            channel: document.querySelector('#channels').value,
            recipient: document.querySelector('#recipient').value
        })
    })
    .then((response)=>response.json())
    .then(result=>{
        if (result.message == "Recipient username does not exist.") {
            alert("The recipient username that you typed in is not valid.", 'danger');
        }
        else {
            alert("Invite sent.");
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