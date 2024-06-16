
function handleUserChoice(symptom, choice) {
	console.log(`User selected ${choice} for ${symptom}`);
	// Proceed to next iteration or do something based on user choice
	// For now, I'll just log the user's choice
}

// start of questioning function
// list of details
const uvd = "This refers to any abnormal or atypical discharge from the vagina.\nAny abnormal discharge from the vagina that differs in color, consistency, or odor from your usual discharge.\n\n\nይህ ከሴት ብልት የሚወጣ ማንኛውንም ያልተለመደ ፈሳሽን ይመለከታል።ከሴት ብልት የሚወጣ ማንኛውም ያልተለመደ ፈሳሽ በቀለም፣ ወጥነት ወይም ጠረን ከወትሮው ፈሳሽዎ ይለያል።"
const pdu = "This asks if there is pain or discomfort experienced while urinating.\nPain or discomfort experienced while urinating.\n\nይህ በሽንት ጊዜ የሚያጋጥም ህመም ካለ ይጠይቃል።"
const vi = "This asks if there is an itching sensation in the vaginal area.\nItching or irritation in the vaginal area.\n\nይህ በሴት ብልት አካባቢ የማሳከክ ስሜት እንዳለ ይጠይቃል።"
const pds = "This asks if there is pain or discomfort experienced during sexual intercourse.\nPainful intercourse, often felt as discomfort or sharp pain during penetration.\n\nይህ በግብረ ሥጋ ግንኙነት ወቅት የሚያጋጥም ህመም ወይም ምቾት ካለ ይጠይቃል።\nየሚያሳምም የግብረ ሥጋ ግንኙነት፣ ብዙ ጊዜ እንደ አለመመቸት ወይም ወደ ውስጥ በሚገቡበት ጊዜ ከፍተኛ ህመም ይሰማዋል።"
const gs = "This asks if there are any open or ulcerated sores in the genital area.\nPainful or tender areas on the genitals, indicating potential infection or irritation.\n\nይህ በጾታ ብልት አካባቢ ምንም አይነት ክፍት ወይም ቁስለት እንዳለ ይጠይቃል።\nበጾታ ብልት ላይ የሚያሰቃዩ ወይም ለስላሳ ቦታዎች፣ ይህም ኢንፌክሽን ወይም ብስጭት መኖሩን ያሳያል።"
const lap = "This asks if there is pain or discomfort in the lower part of the abdomen, below the belly button.\nPain or discomfort below the belly button, often indicating various underlying issues.\n\nይህ ከሆድ በታች ባለው የሆድ ክፍል ውስጥ ከሆድ በታች ህመም ወይም ምቾት መኖሩን ይጠይቃል።\nከሆድ ግርጌ በታች ህመም ወይም ምቾት ማጣት ይህም ብዙ ጊዜ የተለያዩ ችግሮችን ያሳያል።"
const f = "This asks if there is an elevated body temperature.\nElevated body temperature, which can be a sign of infection or inflammation.\n\nይህ ከፍ ያለ የሰውነት ሙቀት መኖሩን ይጠይቃል።\nየሰውነት ሙቀት መጨመር፣ ይህም የኢንፌክሽን ወይም እብጠት ምልክት ሊሆን ይችላል።"
const vd = "This asks if there is any type of discharge coming from the vagina.\nVaginal discharge: Normal or abnormal fluid coming from the vagina.\n\nይህ ከሴት ብልት የሚወጣ አይነት ፈሳሽ ካለ ይጠይቃል።\nየሴት ብልት ፈሳሽ፡ ከሴት ብልት የሚወጣ መደበኛ ወይም ያልተለመደ ፈሳሽ።"
const mmp = "This asks if there has been a skipped menstrual period.\nSkipping a menstrual cycle without pregnancy, which can indicate various health issues.\n\nይህ የወር አበባ ጊዜ ያለፈ መሆኑን ይጠይቃል።\nእርግዝና ሳይኖር የወር አበባ ዑደትን መዝለል የተለያዩ የጤና ችግሮችን ሊያመለክት ይችላል።"
const vb = "This asks if there is any bleeding from the vagina outside of the normal menstrual cycle.\nVaginal bleeding: Abnormal bleeding from the vagina, outside of regular menstruation.\n\nይህ ከተለመደው የወር አበባ ዑደት ውጪ ከሴት ብልት የሚመጣ ደም መፍሰስ እንዳለ ይጠይቃል።\nየሴት ብልት ደም መፍሰስ፡ ከሴት ብልት ያልተለመደ ደም መፍሰስ፣ ከወር አበባ ውጪ።"
const pil = "This asks if there is pain or swelling in the lymph nodes located in the groin area.\nDiscomfort or tenderness in the lymph nodes located in the groin area.\n\nይህ በግራጫ አካባቢ በሚገኙ የሊምፍ ኖዶች ላይ ህመም ወይም እብጠት እንዳለ ይጠይቃል።\nበግራይን አካባቢ በሚገኙ የሊንፍ ኖዶች ውስጥ ምቾት ማጣት ወይም ርህራሄ።"
const pdfs = "This asks if there is a discharge of pus from any swollen area.\nDrainage of thick, yellowish fluid from an inflamed or infected area.\n\nይህ ከየትኛውም ያበጠ አካባቢ የንፍጥ ፈሳሽ እንዳለ ይጠይቃል።\nከተነደደ ወይም ከተበከለ አካባቢ ወፍራም ቢጫ ቀለም ያለው ፈሳሽ መፍሰስ።"
const scr = "This asks if there are any raised bumps with a rough texture on the genital area, which may be the same color as the surrounding skin.\nRaised lesions on the genital area, potentially indicative of certain infections or conditions.\n\nይህ በጾታ ብልት አካባቢ ላይ ሸካራ ሸካራነት ያላቸው ከፍ ያሉ እብጠቶች መኖራቸውን ይጠይቃል፣ እነሱም በዙሪያው ካለው ቆዳ ጋር አንድ አይነት ቀለም ሊሆኑ ይችላሉ።\nበብልት አካባቢ ላይ የተነሱ ቁስሎች አንዳንድ ኢንፌክሽኖችን ወይም ሁኔታዎችን ሊያመለክቱ ይችላሉ።"
const slbf = "This asks if there are any abnormal skin lesions or sores present in the spaces between the fingers, wrists, genital area, or buttocks.\nAbnormal skin changes or sores in these specific areas.\n\nይህ በጣቶቹ፣ በእጅ አንጓዎች፣ በብልት አካባቢ ወይም በትሮች መካከል ባሉት ክፍተቶች ላይ ምንም አይነት ያልተለመደ የቆዳ ቁስሎች ወይም ቁስሎች እንዳሉ ይጠይቃል።\nበእነዚህ ልዩ ቦታዎች ላይ ያልተለመደ የቆዳ ለውጦች ወይም ቁስሎች።"
const lnph = "This asks if there are any lice or their eggs (nits) present on the pubic hair.\nPresence of lice or their eggs (nits) in the pubic hair, indicating infestation.\n\nይህ በጉርምስና ፀጉር ላይ ቅማል ወይም እንቁላሎቻቸው (ኒት) መኖራቸውን ይጠይቃል።\nቅማሎች ወይም እንቁላሎቻቸው (ኒት) በጉርምስና ፀጉር ውስጥ መኖራቸው ይህም ኢንፌክሽንን ያሳያል።"
const ye = "This asks if the whites of the eyes appear yellow.\nJaundice, a yellow discoloration of the eyes, often a sign of liver or gallbladder issues.\n\nይህ የዓይኑ ነጮች ቢጫ ከታዩ ይጠይቃል።\nጃንዲስ፣ የአይን ቢጫ ቀለም፣ ብዙ ጊዜ የጉበት ወይም የሐሞት ፊኛ ችግሮች ምልክት ነው።"
const ys = "This asks if the skin has a yellowish tint.\nJaundice affecting the skin, similar to the eyes, indicating potential liver problems.\n\nይህ የቆዳው ቢጫ ቀለም እንዳለው ይጠይቃል።\nከዓይን ጋር የሚመሳሰል የቆዳ በሽታ የያዛት በሽታ፣ ይህም የጉበት ችግሮችን ያሳያል።"
const ap = "This asks if there is pain or discomfort in the abdomen.\nDiscomfort or pain in the abdominal region, which can stem from various causes.\n\nይህ በሆድ ውስጥ ህመም ወይም ምቾት እንዳለ ይጠይቃል።\nምቾት ወይም የሆድ አካባቢ ህመም በተለያዩ ምክንያቶች ሊመጣ ይችላል።"
const du = "This asks if the urine appears darker in color than usual.\nUrine that appears darker than usual, potentially indicating dehydration or liver issues.\n\nይህ ሽንት ከወትሮው የበለጠ ጠቆር ያለ መስሎ እንደታየ ይጠይቃል።\nሽንት ከወትሮው ጠቆር ያለ መስሎ ይታያል፣ ይህም ድርቀትን ወይም የጉበት ችግሮችን ሊያመለክት ይችላል።"
const pai = "This asks if there is itching in the pubic area.\nItching or irritation in the pubic region.\n\nይህ በጉርምስና አካባቢ ማሳከክ እንዳለ ይጠይቃል።\nበሆድ አካባቢ ማሳከክ ወይም መበሳጨት።"
const iwan = "This asks if the itching sensation becomes more intense during the nighttime.\nIncreased itching sensation experienced during nighttime.\n\nይህ በምሽት ጊዜ የማሳከክ ስሜቱ የበለጠ እየጠነከረ እንደሆነ ይጠይቃል።\nበሌሊት የሚደርስ የማሳከክ ስሜት ይጨምራል።"
const scfv = "This asks if there are other people in the family or nearby who have similar symptoms or complaints.\n\nይህ በቤተሰብ ውስጥ ወይም በአቅራቢያው ተመሳሳይ ምልክቶች ወይም ቅሬታ ያላቸው ሌሎች ሰዎች እንዳሉ ይጠይቃል።"
const itae = "This asks if there is itching experienced in the thighs, armpit area, or eyelids.\nItching or irritation in these specific areas of the body.\n\nይህ በጭኑ፣ በብብት አካባቢ ወይም በዐይን ሽፋሽፍቶች ላይ የሚከሰት ማሳከክ እንዳለ ይጠይቃል።\nበእነዚህ ልዩ የሰውነት ክፍሎች ላይ ማሳከክ ወይም ብስጭት።"

const ud = "This refers to any abnormal or atypical discharge from the penis or urethra.\nAbnormal fluid coming from the penis, which can indicate infection or other issues\n\nይህ የሚያመለክተው ማንኛውም ከብልት ወይም ከሽንት ቱቦ የሚወጣ ያልተለመደ ወይም ያልተለመደ ፈሳሽ ነው።ይህ የሚያመለክተው ማንኛውም ከብልት ወይም ከሽንት ቱቦ የሚወጣ ያልተለመደ ወይም ያልተለመደ ፈሳሽ ነው።"
const fu = "This asks if there is an increased need to urinate more often than usual.\nNeeding to urinate more often than usual, potentially indicating urinary tract issues.\n\nይህ ከወትሮው በበለጠ በተደጋጋሚ የመሽናት ፍላጎት መኖሩን ይጠይቃል።\nከወትሮው በበለጠ ብዙ ጊዜ መሽናት ስለሚያስፈልገው የሽንት ቱቦ ችግሮችን ሊያመለክት ይችላል።"
const sp = "This asks if there is pain or discomfort in the scrotum (the pouch of skin containing the testicles).\nPain or discomfort in the scrotum, the pouch of skin containing the testicles.\n\nይህ በ Scrotum ውስጥ ህመም ወይም ምቾት እንዳለ ይጠይቃል (የቆዳውን የወንድ የዘር ፍሬ የያዘው ከረጢት)።\nበቁርጥማት ውስጥ ህመም ወይም ምቾት ማጣት፣ የወንድ የዘር ፍሬዎችን የያዘ የቆዳ ቦርሳ።"
const sw = "This asks if there is swelling or enlargement of the scrotum.\nSwelling or enlargement of the scrotum, potentially indicative of various conditions.\n\nይህ የሆድ ቁርጠት ማበጥ ወይም መስፋፋት እንዳለ ይጠይቃል።\nየእግር እብጠት ወይም መጨመር የተለያዩ ሁኔታዎችን ሊያመለክት ይችላል።"
const is = "This asks if there is swelling in the groin area.\nSwelling in the groin area.\n\nይህ ብሽሽት አካባቢ እብጠት እንዳለ ይጠይቃል።\nበእግር አካባቢ እብጠት።"
const sop = "This asks whether the pain started suddenly or developed gradually over time.\nWhether the pain in the scrotal area started suddenly or developed gradually.\n\nይህ ሕመሙ በድንገት መጀመሩን ወይም ከጊዜ ወደ ጊዜ ቀስ በቀስ ማደግን ይጠይቃል።\nበ scrotal አካባቢ ላይ ያለው ህመም በድንገት የጀመረ ወይም ቀስ በቀስ ያደገ እንደሆነ ይጠይቃል።"


async function askSymptom(gender = '') {

	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	container.removeChild(male);
	container.removeChild(female);

	if (gender == 'female') {

		var symptomList = {
			"unusual_discharge": { symptom: "Unusual vaginal discharge", value: "", description: uvd },
			"pain_during_urination": { symptom: "Dysuria (pain during urination)", value: "", description: pdu },
			"vaginal_itching": { symptom: "Vaginal itching", value: "", description: vi },
			"pain_during_sex": { symptom: "Dyspareunia (pain during sex)", value: "", description: pds },
			"genital_sore": { symptom: "Genital sore", value: "", description: gs },
			"pain_below_umbilicus": { symptom: "Lower abdominal pain, Pain below umblicus", value: "", description: lap },
			"fever": { symptom: "Fever", value: "", description: f },
			"vaginal_discharge": { symptom: "Vaginal discharge", value: "", description: vd },
			"missed_menstrual_period": { symptom: "Missed menstrual Period", value: "", description: mmp },
			"vaginal_bleeding": { symptom: "Vaginal bleeding", value: "", description: vb },
			"painful_inguinal_lymph_node_or_swelling_over_the_groin": { symptom: "Painful inguinal lymph node or swelling over the groin", value: "", description: pil },
			// "inguinal_swelling": { symptom: "Inguinal swelling", value: "" },
			"pus_discharge_from_swelling": { symptom: "Pus discharge from swelling", value: "", description: pdfs },
			"skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area": { symptom: "Skin colored raised bumps with rough surface single or multiple on genital area", value: "", description: scr },
			"skin_lesions_on_between_fingerswrist_genital_area_buttock": { symptom: "Skin lesions between fingerswrist genital area buttock", value: "", description: slbf },
			"lice_or_nits_on_pubic_hair": { symptom: "lice or nits on pubic hair", value: "", description: lnph },
			"yellowing_of_the_eyes": { symptom: "Yellowing of the eyes", value: "", description: ye },
			"yellowing_of_the_skin": { symptom: "Yellowing of the skin", value: "", description: ys },
			"abdominal_pain": { symptom: "Abdominal pain", value: "", description: ap },
			"dark_urine": { symptom: "Dark urine", value: "", description: du },
			"pubic_area_itching": { symptom: "Pubic area itching", value: "", description: pai },
			"itching_worsening_at_night": { symptom: "Itching worsening at night", value: "", description: iwan },
			"similar_complaint_in_the_family_or_vicinity": { symptom: "Similar complaint in the family or vicinity", value: "", description: scfv },
			"itching_over_the_thighs_axilla_eyelid": { symptom: "Itching over the thighs axilla eyelid", value: "", description: itae }
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

			"urethral_discharge": { symptom: "Unusual discharge", value: "", description: ud },
			"pain_during_urination": { symptom: "Dysuria (pain during urination)", value: "", description: pdu },
			"frequent_urination": { symptom: "Frequent urination", value: "", description: fu },
			"scrotal_pain": { symptom: "Scrotal pain", value: "", description: sp },
			"sudden_onset_of_pain": { symptom: "Sudden onset of pain", value: "", description: sop },
			"swelling": { symptom: "Scrotal swelling", value: "", description: sw },
			"genital_sore": { symptom: "Genital sore", value: "", description: gs },
			"painful_inguinal_lymph_node_or_swelling_over_the_groin": { symptom: "Painful inguinal lymph node or swelling over the groin", value: "", description: itae },
			"inguinal_swelling": { symptom: "Inguinal swelling", value: "", description: is },
			"fever": { symptom: "Fever", value: "", description: f },
			"skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area": { symptom: "Skin colored raised bumps with rough surface single or multiple on genital area", value: "", description: scr },
			"skin_lesions_on_between_fingerswrist_genital_area_buttock": { symptom: "Skin lesions between fingerswrist genital area buttock", value: "", description: slbf },
			"lice_or_nits_on_pubic_hair": { symptom: "lice or nits on pubic hair", value: "", description: lnph },
			"yellowing_of_the_eyes": { symptom: "Yellowing of the eyes", value: "", description: ye },
			"yellowing_of_the_skin": { symptom: "Yellowing of the skin", value: "", description: ys },
			"abdominal_pain": { symptom: "Abdominal pain", value: "", description: ap },
			"dark_urine": { symptom: "Dark urine", value: "", description: du },
			"pubic_area_itching": { symptom: "Pubic area itching", value: "", description: pai },
			"itching_worsening_at_night": { symptom: "Itching worsening at night", value: "", description: iwan },
			"similar_complaint_in_the_family_or_vicinity": { symptom: "Similar complaint in the family or vicinity", value: "", description: scfv },
			"itching_over_the_thighs_axilla_eyelid": { symptom: "Itching over the thighs axilla eyelid", value: "", description: itae }
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

		// var selectedValue = await conversationBuilder(message, symptomList[key].symptom, symptomList[key].description);
		var selectedValue = await conversationBuilder(message, symptomList[key].symptom, symptomList[key].description);


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

// gender input
async function genderInput(gender) {
	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	var userMessage = document.createElement('div');
	userMessage.className = 'user-message';

	userMessage.innerHTML = '<strong>User</strong> <br/>' + gender;
	chatContainer.appendChild(userMessage);
}

// conversation  handler
async function conversationBuilder(message, name = '', description = '') {
	var container = document.getElementById("availableSymptoms");
	var chatContainer = document.getElementById('chat');

	var botMessage = document.createElement('div');
	botMessage.className = 'bot-message';

	var userMessage = document.createElement('div');
	userMessage.className = 'user-message';

	botMessage.innerHTML = message;
	chatContainer.appendChild(botMessage);

	////////////////////////////////
	var infoIcon = document.createElement('i');
	infoIcon.className = 'bi bi-info-circle-fill me-2';
	infoIcon.style.cursor = 'pointer';
	infoIcon.setAttribute('data-bs-toggle', 'modal');
	infoIcon.setAttribute('data-bs-target', '#infoModal');

	var popupTitle = document.getElementById('infoModalLabel');
	popupTitle.textContent = name;

	var popupDescription = document.getElementById('infoModalBody');
	popupDescription.textContent = description;

	var space = document.createElement('br');

	// Append the icon and message text to the botMessage
	botMessage.appendChild(space);
	botMessage.appendChild(infoIcon);

	chatContainer.scrollTop = chatContainer.scrollHeight;

	var yesButton = document.createElement("button");
	yesButton.classList.add("symptom-button");
	yesButton.textContent = "Yes";

	var noButton = document.createElement("button");
	noButton.classList.add("symptom-button");
	noButton.textContent = "No";

	var clearButton = document.createElement("button");
	clearButton.classList.add("symptom-button");
	clearButton.textContent = "Clear Choice";

	container.appendChild(yesButton);
	container.appendChild(noButton);

	//
	var closeButton = document.querySelector('.modal-header .close');
	closeButton.addEventListener('click', function () {
		var modal = document.getElementById('infoModal');
		var modalInstance = bootstrap.Modal.getInstance(modal);
		modalInstance.hide();
	});
	// container.appendChild(clearButton);

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

// function toggleSidebar() {
// 	var sidebar = document.getElementById("sidebar");
// 	sidebar.classList.toggle("active");
// }

function toggleSidebar() {
	var sidebar = document.getElementById("sidebar");
	var hamburgerMenu = document.querySelector(".hamburger-menu");
	sidebar.classList.toggle("active");
	hamburgerMenu.classList.toggle("active");
}

function toggleSendFeedbackButton() {
	var feedback = document.getElementById("feedback-txt").value;
	var button = document.getElementById("send-btn");
	if (feedback.trim() !== "") {
		button.removeAttribute("disabled");
	} else {
		button.setAttribute("disabled", "disabled");
	}
	console.log("Button state:", button.disabled ? "disabled" : "enabled");
}

function feedbackWordLimit() {
	const textarea = document.getElementById('feedback-txt');
	const wordCount = document.getElementById('wordCount');
	const maxWords = 150; // Set your desired word limit here

	const words = textarea.value.split(/\s+/);
	if (words.length > maxWords) {
		textarea.value = words.slice(0, maxWords).join(' ');
		textarea.disabled = true; // Disable the textarea
	} else {
		textarea.disabled = false; // Enable the textarea
	}
	wordCount.textContent = `${words.length}/${maxWords} words`;
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

	var textField = document.getElementById('feedback-txt');
	textField.value = '';
	toggleSendFeedbackButton();
	alert('Your feedback is sent. We appreciate you taking the time to share your ideas with us.')
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
			handleBackendResponse(data, sex);
		})
		.catch(error => console.error('Error:', error));
}


// convert result
function convertResult(result) {
	if (result.toLowerCase() == 'vl') {
		return "Very Likely"
	}
	else if (result.toLowerCase() == 'l') {
		return "Likely"
	}
	else if (result.toLowerCase() == 'm') {
		return "Moderatly"
	}
}

// insert space b/n syndrom name
function insertSpaceBeforeUppercase(word) {
	return word.replace(/[A-Z]/g, match => ' ' + match);
}

// display predection returened from backend

function handleBackendResponse(data, gender) {
	console.log('Handling backend response');

	var chatContainer = document.getElementById('chat');
	message1 = "<strong>Bot</strong> <br>";
	message2 = "";
	var botMessage = document.createElement('div');
	botMessage.className = 'bot-message';
	botMessage.style.backgroundColor = '#7ff59f';

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

					if (result == 'VL') {
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
				else {
					resultItem.syndromName = syndrome;
					resultItem.result = result1;
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

			}
		}
	}
	console.log(resultlList);

	// sort resultList using priority
	resultlList.sort((a, b) => a.priority - b.priority);

	// console.log(resultlList);

	resultlList.forEach((resultItem) => {
		if (gender == "female" && resultItem.syndromName == "ScrotalSwellingSyndrome") {
			return;
		}

		message2 = `The prediction result for ${insertSpaceBeforeUppercase(resultItem.syndromName)} is ${resultItem.result}.<br/>`;
		message1 = message1 + message2;

		// console.log(resultItem.x);
	});

	let advice = "<br/><br/>Based on these results, it is highly advised to seek medical care promptly. Additionally, please refrain from engaging in sexual activity until you have completed your treatment to prevent further complications and transmission.";

	message1 = message1 + advice;

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