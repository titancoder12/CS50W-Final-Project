const id = window.location.pathname.slice(9);
var loaded_messages = [];
document.addEventListener('DOMContentLoaded', function(){
    fetch(`/api/channel/${id}`)
    .then(response=>response.json())
    .then((channel)=>{
        document.querySelector('title').innerHTML = channel.name;
    });

    document.querySelector('#sendmessagetext').addEventListener('click', create_message);

    setInterval(load_messages, 1000);
})

function load_messages() {
    channel_id = id;
    fetch(`/api/messages/${channel_id}`)
    .then(response=>response.json())
    //.then(messages=>Array.from(messages))
    .then((messages)=>messages.sort(function(a,b) {
        return b.id - a.id
    }))
    .then((messages)=>{
        // if (messages.length == load_messages.length){
        //     for (let i=0; i<messages.length; i++){
        //         if (messages[i]["id"] != loaded_messages[i]["id"]){
        //             return null;
        //         }
        //     }
        // }
        if (JSON.stringify(messages) == JSON.stringify(loaded_messages)){
            return null;
        }
        else {
            document.querySelector('#messages').innerHTML = '';
            loaded_messages = messages;
            //console.log(loaded_messages);
        }
        
        console.log(messages);
        for (let i = 0; i < messages.length; i++) {
            const messagediv = document.createElement('div');
            document.querySelector('#messages').append(messagediv);
            fetch(`/api/user/${messages[i].user_id}`)
            .then(response=>response.json())
            .then(username=>{
                messagediv.id = messages[i].id;
                console.log(messages[i]);
                messagediv.innerHTML = 
                `<hr>
                <p class='ms-4'>${username} said:</p>
                <h4 class='ms-3'>${messages[i].text}</h4>
                <hr>`;
                console.log(messages[i].text);
            })
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
        var elem = document.getElementById('messages');
        //elem.scrollBottom = elem.scrollHeight;
        window.scrollTo(0, document.body.scrollHeight);
    });
}