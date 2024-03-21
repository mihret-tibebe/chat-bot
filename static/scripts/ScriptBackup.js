// display symptoms based on gender
// function showSymptomsBasedOnGender(gender) {
// 	console.log("****show based on gender trigered")
// 	var availableSymptomsContainer = document.getElementById('availableSymptoms');
// 	var symptomList;

	// if(gender == "Female") {

	// 	symptomList = ["unusual_discharge", "genital_sore", "pain_below_umbilicus", "painful_inguinal_lymph_node_or_swelling_over_the_groin", "skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area", "skin_lesions_on_between_fingerswrist_genital_area_buttock", "pubic_area_itching", "yellowing_of_the_eyes"]

	// 	symptomList.forEach(symptom => {
	// 		availableSymptomsContainer.appendChild(createSymptomButton(symptom.key));
	// 	});
	// }
	// else if (gender == "Male") {
	// 	symptomList = ["urethral_discharge", "genital_sore", "scrotal_pain", "painful_inguinal_lymph_node_or_swelling_over_the_groin", "skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area", "skin_lesions_on_between_fingerswrist_genital_area_buttock", "pubic_area_itching", "yellowing_of_the_eyes"]

	// 	symptomList.forEach(symptom => {
	// 		availableSymptomsContainer.appendChild(createSymptomButton(symptom));
	// 	});

	// }
// }


// *2

// create symptom buttons while toggling
// function createSymptomButton(symptom) {
// 	var symptomButton = document.createElement('button');
// 	symptomButton.className = 'symptom-button';
// 	symptomButton.innerHTML = symptom;
// 	symptomButton.onclick = function () {
// 		toggleSymptom(symptom);
// 	};
// 	return symptomButton;
// }


// *3

// check where the button belongs
// function isChildOfContainer(text, container) {
// 	var buttons = container.children;
// 	for (var i = 0; i < buttons.length; i++) {
// 		if (buttons[i].innerHTML === text) {
// 			return true;
// 		}
// 	}
// 	return false;
// }

// *4

// return labele
// function getButtonByText(text, container) {
// 	var buttons = container.children;
// 	for (var i = 0; i < buttons.length; i++) {
// 		if (buttons[i].innerHTML === text) {
// 			return buttons[i];
// 		}
// 	}
// 	return null;
// }


// *5

// get user choice (yes/ no)
// async function getUserChoice(buttons) {
// 	return new Promise(resolve => {
// 		buttons.forEach(button => {
// 			button.addEventListener("click", () => {
// 				resolve(button.textContent.toLowerCase());
// 			});
// 		});
// 	});
// }

// *6

// toggling selected and unselected symptoms
// function toggleSymptom(symptom) {
// 	var availableSymptomsContainer = document.getElementById('availableSymptoms');
// 	var selectedSymptomsContainer = document.getElementById('selectedSymptoms');

// 	var isSymptomSelected = isChildOfContainer(symptom, selectedSymptomsContainer);

// 	if (isSymptomSelected) {
// 		// Unselect the symptom
// 		selectedSymptomsContainer.removeChild(getButtonByText(symptom, selectedSymptomsContainer));
// 		availableSymptomsContainer.appendChild(createSymptomButton(symptom));
// 	} else {
// 		// Select the symptom
// 		availableSymptomsContainer.removeChild(getButtonByText(symptom, availableSymptomsContainer));
// 		selectedSymptomsContainer.appendChild(createSymptomButton(symptom));
// 	}
// }