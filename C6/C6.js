#!/usr/bin/env node

//########################################## 
//#   
//#  #TuentiChallenge4 (2014).
//#  Challenge 6: Man in the middle
//#  https://contest.tuenti.net/Challenges?id=6
//#  Isaac Roldan (@saky)
//#  
//##########################################


var net = require('net');
var util = require('util');
var crypto = require('crypto');

var options = {
	'port': 6969,
	'host': '54.83.207.90',
}

const KEYPHRASE = 'CadetBlueTotalGuineaIsRegular';

var dh, secret, state = 0;
var keyphrase
var socket = net.connect(options, function() {
});

socket.on('data', function(data) {

	data = data.toString().trim().split('|');

	//Just modified the client to respond to all messages intercepted.
	if (data[0] == "CLIENT->SERVER:hello?") {
		socket.write(util.format('hello?')) //send without changing anything

	} else if (data[0] == "SERVER->CLIENT:hello!") {
		socket.write(util.format('hello!')) //send without changing anything

	} else if (data[0] == 'CLIENT->SERVER:key') {
		dh = crypto.createDiffieHellman(256);
		dh.generateKeys();
		socket.write(util.format('key|%s|%s\n', dh.getPrime('hex'), dh.getPublicKey('hex')));
		//Send you own prime and public key

	} else if (data[0] == 'SERVER->CLIENT:key') {
		secret = dh.computeSecret(data[1], 'hex');
		var cipher = crypto.createCipheriv('aes-256-ecb', secret, '');
		keyphrase = cipher.update(KEYPHRASE, 'utf8', 'hex') + cipher.final('hex');
		socket.write(util.format('key|%s\n',data[1]));
		//compute the secret and the encrypted keyphrase and send to the client the server response

	} else if (data[0] == 'CLIENT->SERVER:keyphrase') {
		socket.write(util.format('keyphrase|%s\n', keyphrase));
		//send the keyphrase encrypted to the server

	} else if (data[0] == 'SERVER->CLIENT:result') {
		var decipher = crypto.createDecipheriv('aes-256-ecb', secret, '');
		var message = decipher.update(data[1], 'hex', 'utf8') + decipher.final('utf8');
		console.log(message);
		socket.end();
	} 
	else {
		console.log('Error & end');
		socket.end();
	}
});
