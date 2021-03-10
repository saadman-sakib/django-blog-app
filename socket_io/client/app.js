const socket = io('192.168.43.189:7000/');
const button = document.getElementById('btn');

button.addEventListener('click', (e) => {
	console.log("ff");
	const chatForm = document.getElementById('msg');
	socket.emit('chat', chatForm.value);
	console.log("yo");
	e.preventDefault();
})

socket.on('chat', msg => {
	const content = document.getElementById('content')
	content.innerHTML += `<p>${msg}</p>`
	console.log(msg);
})

//sending msg to server, in the 'haha' channel
socket.emit('haha', 'hehe');