//var hello = '';
document.addEventListener('DOMContentLoaded', ()=>{
    sayhello();
});


function sayhello(){
    let hello = '';
    fetch('hello') 
    .then((response)=>response.json())   
    .then((responsejson)=>{
        hello=responsejson['text'];
        console.log(hello);
        return hello;
    })
    .then(()=>console.log(hello))
    .then(()=>{document.querySelector('#text').innerHTML = hello})
}