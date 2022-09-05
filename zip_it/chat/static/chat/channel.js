const id = window.location.pathname.slice(9);
var loaded_messages = [];
document.addEventListener('DOMContentLoaded', function(){
    fetch(`/api/channel/${id}`)
    .then(response=>response.json())
    .then((channel)=>{
        document.querySelector('title').innerHTML = channel.name;
    });
    load_messages();
    document.querySelector('#sendmessagetext').addEventListener('click', () => {
        create_message()
    });

    setInterval(load_messages, 1000);
})

function load_messages() {
    channel_id = id;
    fetch(`/api/messages/${channel_id}`)
    .then(response=>response.json())
    .then(messages=>Array.from(messages))
    .then((messages)=>{
        // if (messages.length == load_messages.length){
        //     for (let i=0; i<messages.length; i++){
        //         if (messages[i]["id"] != loaded_messages[i]["id"]){
        //             return null;
        //         }
        //     }
        // }
        if (messages == loaded_messages){
            console.log('loaded messages is messages');
            return null;
        }
        else {
            document.querySelector('#messages').innerHTML = '';
            console.log('loaded messages isnt messages');
            loaded_messages = messages;
            console.log(loaded_messages);
        }
        var j = 0;
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
            j++;
        }
    })
    return null;
}

function create_message() {
    channel_id = id;
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
        document.querySelector('#messages').innerHTML = '';
        load_messages();
    });
}