
function handleUserChoice(symptom, choice) {
	console.log(`User selected ${choice} for ${symptom}`);
	// Proceed to next iteration or do something based on user choice
	// For now, I'll just log the user's choice
}

// start of questioning function

async function askSymptom(gender = '') {

	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	container.removeChild(male);
	container.removeChild(female);

	if (gender == 'female') {

		var symptomList = {
			"unusual_discharge": { symptom: "Unusual vaginal discharge", value: "" },
			"pain_during_urination": { symptom: "Dysuria (pain during urination)", value: "" },
			"vaginal_itching": { symptom: "Vaginal itching", value: "" },
			"pain_during_sex": { symptom: "Dyspareunia (pain during sex)", value: "" },
			"genital_sore": { symptom: "Genital sore", value: "" },
			"pain_below_umbilicus": { symptom: "Lower abdominal pain, Pain below umblicus", value: "" },
			"fever": { symptom: "Fever", value: "" },
			"vaginal_discharge": { symptom: "Vaginal discharge", value: "" },
			"missed_menstrual_period": { symptom: "Missed menstrual Period", value: "" },
			"vaginal_bleeding": { symptom: "Vaginal bleeding", value: "" },
			"painful_inguinal_lymph_node_or_swelling_over_the_groin": { symptom: "Painful inguinal lymph node or swelling over the groin", value: "" },
			// "inguinal_swelling": { symptom: "Inguinal swelling", value: "" },
			"pus_discharge_from_swelling": { symptom: "Pus discharge from swelling", value: "" },
			"skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area": { symptom: "Skin colored raised bumps with rough surface single or multiple on genital area", value: "" },
			"skin_lesions_on_between_fingerswrist_genital_area_buttock": { symptom: "Skin lesions between fingerswrist genital area buttock", value: "" },
			"lice_or_nits_on_pubic_hair": { symptom: "lice or nits on pubic hair", value: "" },
			"yellowing_of_the_eyes": { symptom: "Yellowing of the eyes", value: "" },
			"yellowing_of_the_skin": { symptom: "Yellowing of the skin", value: "" },
			"abdominal_pain": { symptom: "Abdominal pain", value: "" },
			"dark_urine": { symptom: "Dark urine", value: "" },
			"pubic_area_itching": { symptom: "Pubic area itching", value: "" },
			"itching_worsening_at_night": { symptom: "Itching worsening at night", value: "" },
			"similar_complaint_in_the_family_or_vicinity": { symptom: "Similar complaint in the family or vicinity", value: "" },
			"itching_over_the_thighs_axilla_eyelid": { symptom: "Itching over the thighs axilla eyelid", value: "" }
		};

		// symptomList[inguinal_swelling] = symptomList[painful_inguinal_lymph_node_or_swelling_over_the_groin].symptom

		loopThroughSymptoms(symptomList)
			.then(() => {
				sendMessage(symptomList, gender);
			})
			.catch(error => {
				console.error('Error in loopThroughSymptoms:', error);
			});

	}
	else if (gender == 'male') {

		var symptomList = {
			// "pus_discharge_from_swelling": "Pus discharge from swelling",

			"urethral_discharge": { symptom: "Unusual discharge", value: '' },
			"pain_during_urination": { symptom: "Dysuria (pain during urination)", value: "" },
			"frequent_urination": { symptom: "Frequent urination", value: "" },
			"scrotal_pain": { symptom: "Scrotal pain", value: "" },
			"sudden_onset_of_pain": { symptom: "Sudden onset of pain", value: "" },
			"swelling": { symptom: "Scrotal swelling", value: "" },
			"genital_sore": { symptom: "Genital sore", value: "" },
			"painful_inguinal_lymph_node_or_swelling_over_the_groin": { symptom: "Painful inguinal lymph node or swelling over the groin", value: "" },
			"inguinal_swelling": { symptom: "Inguinal swelling", value: "" },
			"fever": { symptom: "Fever", value: "" },
			"skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area": { symptom: "Skin colored raised bumps with rough surface single or multiple on genital area", value: "" },
			"skin_lesions_on_between_fingerswrist_genital_area_buttock": { symptom: "Skin lesions between fingerswrist genital area buttock", value: "" },
			"lice_or_nits_on_pubic_hair": { symptom: "lice or nits on pubic hair", value: "" },
			"yellowing_of_the_eyes": { symptom: "Yellowing of the eyes", value: "" },
			"yellowing_of_the_skin": { symptom: "Yellowing of the skin", value: "" },
			"abdominal_pain": { symptom: "Abdominal pain", value: "" },
			"dark_urine": { symptom: "Dark urine", value: "" },
			"pubic_area_itching": { symptom: "Pubic area itching", value: "" },
			"itching_worsening_at_night": { symptom: "Itching worsening at night", value: "" },
			"similar_complaint_in_the_family_or_vicinity": { symptom: "Similar complaint in the family or vicinity", value: "" },
			"itching_over_the_thighs_axilla_eyelid": { symptom: "Itching over the thighs axilla eyelid", value: "" }
		};

		loopThroughSymptoms(symptomList)
			.then(() => {
				sendMessage(symptomList, gender);
			})
			.catch(error => {
				console.error('Error in loopThroughSymptoms:', error);
			});
	}

}

// for loop handler

async function loopThroughSymptoms(symptomList) {
	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	var count = 0;

	for (const key in symptomList) {
		var message = '<strong>Bot</strong> <br/>' + "Do you have " + symptomList[key].symptom + "?";
		var selectedValue = await conversationBuilder(message);

		if (selectedValue == "Yes") {
			if (key == "unusual_discharge") {
				let detailsValue = [];

				var message = '<strong>Bot</strong> <br/>' + "Is it unusual color such as greenish or yellowish?";
				var selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				message = '<strong>Bot</strong> <br/>' + "Does it has bad odor?";
				selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				console.log(detailsValue);

				vl = [1, 1];
				l1 = [1, 0];
				l2 = [0, 1];
				ul = [0, 0];
				if (JSON.stringify(detailsValue) === JSON.stringify(vl)) {
					symptomList[key].value = "y"; // sure yes
				} else if (JSON.stringify(detailsValue) === JSON.stringify(l1)) {
					symptomList[key].value = "y"; // likely yes
				} else if (JSON.stringify(detailsValue) === JSON.stringify(l2)) {
					symptomList[key].value = "y"; // likely yes
				} else {
					symptomList[key].value = "n";
				}

			}
			else if (key == "urethral_discharge") {
				let detailsValue = [];

				var message = '<strong>Bot</strong> <br/>' + "Is it unusual color such as greenish or yellowish?";
				var selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				message = '<strong>Bot</strong> <br/>' + "Does it has bad odor?";
				selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				console.log(detailsValue);

				vl = [1, 1];
				l1 = [1, 0];
				l2 = [0, 1];
				ul = [0, 0];
				if (JSON.stringify(detailsValue) === JSON.stringify(vl)) {
					symptomList[key].value = "y"; // sure yes
				} else if (JSON.stringify(detailsValue) === JSON.stringify(l1)) {
					symptomList[key].value = "y"; // likely yes
				} else if (JSON.stringify(detailsValue) === JSON.stringify(l2)) {
					symptomList[key].value = "y"; // likely yes
				} else {
					symptomList[key].value = "n";
				}

			}
			else if (key == "scrotal_pain") {
				let detailsValue = [];

				var message = '<strong>Bot</strong> <br/>' + "Does the pain past less than 6 weeks?";
				var selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				message = '<strong>Bot</strong> <br/>' + "Is the onset of the pain sudden or gradual, if it is sudden say Yes, if Gradual say No?";
				selectedValue2 = await conversationBuilder(message);
				if (selectedValue2 == "Yes") {
					detailsValue.push(1);
				}
				else {
					detailsValue.push(0);
				}

				console.log(detailsValue);

				vl = [1, 0];
				l1 = [1, 1];
				l2 = [0, 0];
				if (JSON.stringify(detailsValue) === JSON.stringify(vl)) {
					symptomList[key].value = "y"; // sure yes
				} else if (JSON.stringify(detailsValue) === JSON.stringify(l1)) {
					symptomList[key].value = "y"; // likely yes
				} else {
					symptomList[key].value = "y"; // likely yes
				}

			}
			else {
				symptomList[key].value = "y";
			}
		}
		// 
		else if (selectedValue == "No") {
			symptomList[key].value = "n";
		}

		chatContainer.scrollTop = chatContainer.scrollHeight;

	}

	return Promise.resolve();
}

// conversation  handler
async function conversationBuilder (message) {
	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	var botMessage = document.createElement('div');
	botMessage.className = 'bot-message';

	var userMessage = document.createElement('div');
	userMessage.className = 'user-message';

	botMessage.innerHTML = message;
	chatContainer.appendChild(botMessage);

	chatContainer.scrollTop = chatContainer.scrollHeight;

	var yesButton = document.createElement("button");
	yesButton.classList.add("symptom-button");
	yesButton.textContent = "Yes";

	var noButton = document.createElement("button");
	noButton.classList.add("symptom-button");
	noButton.textContent = "No";

	container.appendChild(yesButton);
	container.appendChild(noButton);

	const selectedValue = await waitForUserInput([yesButton, noButton]);
	userMessage.innerHTML = '<strong>User</strong> <br/>' + selectedValue;
	chatContainer.appendChild(userMessage);

	container.removeChild(yesButton);
	container.removeChild(noButton);

	return selectedValue;
}

function waitForUserInput(buttons) {
	return new Promise((resolve) => {
		buttons.forEach(button => {
			button.addEventListener('click', () => {
				resolve(button.textContent);
			});
		});
	});
}

function toggleSidebar() {
	var sidebar = document.getElementById("sidebar");
	sidebar.classList.toggle("active");
}

function toggleSendFeedbackButton() {
	var feedback = document.getElementById("feedback-txt").value;
	var button = document.getElementById("next-btn");
	if (feedback.trim() !== "") {
		button.removeAttribute("disabled");
	} else {
		button.setAttribute("disabled", "disabled");
	}
	console.log("Button state:", button.disabled ? "disabled" : "enabled");
}

function sendFeedback() {
	let feedback = document.getElementById('feedback-txt').value;

	fetch('/feedback', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(feedback),
	})
	console.log("$$$$$$", feedback);
}



function sendMessage(symptomList, sex) {
	console.log('Sending message');

	// Convert the symptomList object to an array of selected symptoms
	var selectedSymptoms = Object.keys(symptomList).filter(key => symptomList[key].value !== "");

	// Construct the object to send to the backend
	var symptomsObject = {};
	selectedSymptoms.forEach(function (symptomKey) {
		symptomsObject[symptomKey] = symptomList[symptomKey].value;
	});

	symptomsObject["sex"] = sex;
	console.log('Selected symptoms:', symptomsObject);

	// Send the selected symptoms to the backend
	fetch('/templates', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(symptomsObject),
	})
		.then(response => response.json())
		.then(data => {
			console.log('Backend response:', data);
			handleBackendResponse(data);
		})
		.catch(error => console.error('Error:', error));
}


// convert result
function convertResult(result) {
	if (result.toLowerCase() == 'vl'){
		return "Very Likely"
	}
	else if (result.toLowerCase() == 'l'){
		return "Likely"
	}
	else if (result.toLowerCase() == 'm') {
		return "Moderatly"
	}
}

// display predection returened from backend

// function handleBackendResponse(data, symptomsObject) {
function handleBackendResponse(data) {
	console.log('Handling backend response');

	var chatContainer = document.getElementById('chat');
	message1 = "<strong>Bot</strong> <br>";
	message2 = "";
	var botMessage = document.createElement('div');
	botMessage.className = 'bot-message';
	
	countSyndrom = 0;
	let resultlList = [];
	for (const syndrome in data) {
		let resultItem = {};
		let other;

		if (data.hasOwnProperty(syndrome)) {
			const result = data[syndrome].result;
			if ('other' in data[syndrome]) {
				// The object has the specified attribute
				other = data[syndrome].other;
			}

			if (result.toLowerCase() != 'unknown' && result.toLowerCase() != 'ul' && result.toLowerCase() != 'm') {

				result1 = convertResult(result);

				countSyndrom += 1;
				if (other) {
					resultItem.syndromName = syndrome;
					resultItem.result = result1;
					resultItem.other = other;

					if (result == 'VL')
					{
						resultItem.priority = 1;
					}
					else if (result == 'L') {
						resultItem.priority = 2;
					}
					else if (result == 'M') {
						resultItem.priority = 3;
					}
					else {
						resultItem.priority = 0;
					}

					resultlList.push(resultItem);

				}
				else{
					resultItem.syndromName = syndrome;
					resultItem.result = result1;
					console.log(`%%%%%%%%%%%% ${result}`);
					if (result == "VL") {
						resultItem.priority = 1;
					}
					else if (result == "L") {
						resultItem.priority = 2;
					}
					else if (result == "M") {
						resultItem.priority = 3;
					}
					else {
						resultItem.priority = 0;
					}

					resultlList.push(resultItem);
				}
				console.log("$$$$$$$$$$$$$$$" +resultItem.syndromName + " " + resultItem.result)

			}
		}
	}
	console.log(resultlList);

	// sort resultList using priority
	resultlList.sort((a, b) => a.priority - b.priority);
	// console.log(resultlList);

	resultlList.forEach((resultItem) => {
		// console.log(resultItem.x);
		message2 = `The prediction result for ${resultItem.syndromName} is ${resultItem.result}.<br/>`;
		message1 = message1 + message2;
	});

	if (countSyndrom == 0) {
		message2 = "You don't have any of the major STI syndroms. For better result please visit your nearest health care center."
		message1 = message1 + message2;
	}

	botMessage.innerHTML = message1;
	chatContainer.appendChild(botMessage);

	// Clear selected symptoms
	document.getElementById('selectedSymptoms').innerHTML = '';

	// Scroll to the bottom of the chat
	chatContainer.scrollTop = chatContainer.scrollHeight;
}