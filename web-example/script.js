// Constants for the IP, port, and password of the tally server from local storage
const { IP, PORT, PASSWORD } = {
	IP: 'localhost',
	PORT: '5555',
	PASSWORD: 'Password1',
};

// Get the model of the ATEM to check if the connection is working
fetch(`http://${IP}:${PORT}/`, {
	method: 'GET',
	headers: {
		'Content-Type': 'application/json',
		Authorization: PASSWORD,
	},
})
	.then((response) => response.json())
	.then((data) => {
		document.getElementById('model').innerHTML = 'Connected: ' + data.model;
	})
	.catch((error) => {
		console.error(error);
	});

// Function to set the preview of an ME
async function setPreview(input, me = 0) {
	await fetch(`http://${IP}:${PORT}/action/preview/${me}/${input}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			Authorization: PASSWORD,
		},
	})
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
		})
		.catch((error) => {
			console.error(error);
		});
}

// Function to set the program of an ME
async function setProgram(input, me = 0) {
	await fetch(`http://${IP}:${PORT}/action/program/${me}/${input}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			Authorization: PASSWORD,
		},
	})
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
		})
		.catch((error) => {
			console.error(error);
		});
}

// Main function that loops every half second
async function main() {
	var tallyData = {};

	// send a request to the tally endpoint and log the response
	await fetch(`http://${IP}:${PORT}/tally`, {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
			Authorization: PASSWORD,
		},
	})
		.then((response) => response.json())
		// save the response to a variable and log it
		.then((data) => {
			tallyData = data;

			// log the tally data for exploration
			console.log(tallyData);
		})
		.catch((error) => {
			console.error(error);
		});

	// loop through the tally data and log the source, preview, and program
	tallyData.forEach((tally) => {
		console.log(tally.source, tally.preview, tally.program);
	});

	// create html to display the tally data and action buttons
	var statusFill = '';
	tallyData.forEach((tally) => {
		var preview = '',
			program = '';
		if (tally.preview) {
			var preview = 'previewLive';
		}
		if (tally.program) {
			var program = 'programLive';
		}
		statusFill += `
		<div class="tally">
			<div class="source">Source: ${tally.source}</div>
			<div class="preview ${preview}">Preview: ${tally.preview}</div>
			<div class="program ${program}">Program: ${tally.program}</div>
			<button onclick="setPreview(${tally.source})">Set Preview</button>
			<button onclick="setProgram(${tally.source})">Set Program</button>
		</div>
		`;
	});

	document.getElementById('status').innerHTML = statusFill;
}

main();

// run main every 5 seconds
setInterval(main, 500);
