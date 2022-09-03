document.addEventListener('DOMContentLoaded', ()=>{
    load_invites()
})

function load_invites() {
    fetch('/api/invites')
    .then((response)=>response.json())
    .then((invites)=>{
        for (let invite in invites) {
            const invite_div = document.createElement('div');
            invite_div.className = 'center';
            invite_div.innnerHTML = `<hr><h4 class='nobreak'>${invite.channel_name}</h4><p class='graytext'>Sent by ${invite.sender}</p><hr>`;
            document.querySelector('#invites').append(invite_div);
            console.log('invite!');
        }
    });
}