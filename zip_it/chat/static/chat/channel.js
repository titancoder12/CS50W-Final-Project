document.addEventListener('DOMContentLoaded', function(){
    fetch(`/api/channel/${get_id()}`)
    .then(response=>response.json())
    .then((channel)=>{
        document.querySelector('title').innerHTML = channel.name;
    });
    load_messages();
    document.querySelector('#sendmessagetext').addEventListener('click', () => {
        create_message()
    })
})

function get_id() {
    id = window.location.pathname.slice(9);
    return id;
}

function load_messages() {
    document.querySelector('#messages').innerHTML = '';
    channel_id = get_id();
    fetch(`/api/messages/${channel_id}`)
    .then(response=>response.json())
    .then((messages)=>{
        for (let i = 0; i < messages.length; i++) {
            fetch(`/api/user/${messages[i].user_id}`)
            .then(response=>response.json())
            .then(username=>{
                const messagediv = document.createElement('div');
                messagediv.innerHTML = 
                `<hr>
                <p class='ms-4'>${username} said:</p>
                <h4 class='ms-3'>${messages[i].text}</h4>
                <hr>`;
                document.querySelector('#messages').append(messagediv);
            })
            console.log(`message ${i}`)
        }
    })
}

function create_message() {
    channel_id = get_id();
    text = document.querySelector('#messagetext').value;
    fetch('/api/message', {
        method: 'POST',
        //headers: {'X-CSRFToken': csrftoken},
        //mode: 'same-origin',
        body: JSON.stringify({
            channel: channel_id,
            text: text
        })
    }).then(()=>{
        document.querySelector('#messagetext').value = '';
        load_messages();
    });
}