var express = require('express');
var app = express();
var http = require('http').createServer(app)
var socket = require('socket.io')
app.use(express.static('public'));

//socket setup
var io = socket(http, {
	cors: {
		methods: ["GET", "POST"]
	}
});

//server started
http.listen(7000,'192.168.43.189', () => {
	console.log(`listening on port 7000`);

	io.on('connection', (socket) => {
		console.log(`made socket connection ${socket.id}`);

		socket.on('chat', msg => {
			console.log('haha', msg);
			socket.broadcast.emit('chat', msg);
		})		
	})
})