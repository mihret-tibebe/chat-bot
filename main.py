# from flask import Flask, render_template
from flask import Flask, request, jsonify, render_template, send_file
from inference_engine import run_expert_system
from flask_mail import Mail, Message
# from config import HOST, PORT, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
# from models import db, Prediction, Syndrom

app = Flask(__name__, static_folder='static')
app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mhrt2255@gmail.com'
app.config['MAIL_PASSWORD'] = 'cgij fdqk ogiy yibc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
# app.config['MAIL_PASSWORD'] = 'your-email-password'

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amharic/')
def index_amharic():
    return render_template('index_amharic.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/mathematicalModelTest')
def mathematicalModelTest():
    pdf_file_path = 'static/pdfs/A_Mathematical_Model_of_STD.pdf'
    return send_file(pdf_file_path, as_attachment=False)
	# , as_attachment=True

@app.route('/mathematicalModel')
def mathematicalModel():
    pdf_file_path = 'static/pdfs/A_Mathematical_Model_of_STD.pdf'
    return send_file(pdf_file_path)

    # return render_template_string(
    #     """
    #     <script>
    #         window.open('{{ url_for('static', filename='pdfs/A_Mathematical_Model_of_STD.pdf') }}', '_blank');
    #         window.location.href = '{{ url_for('mathematicalModelTest') }}';
    #     </script>
    #     """
    # )



def get_syndrom_id(key):
    syndrom = Syndrom.query.filter_by(symptom=key).first()
    if syndrom:
        return str(syndrom.id)
    return None

def saveToDB(symptoms , response):
    # print(symptoms)
    symptoms["skin_colored_raised_bumps"] = symptoms["skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area"]
    del symptoms["skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area"]
    # print(response)
    dic = {
        "VL": "",
        "L":"",
        "M":"",
        # "U": "",
        "UL":""	}
    # print(response)
    
    for key in response:
        id = get_syndrom_id(key)
        # print("$"*50)
        if response[key]["result"] == "Unknown":
            continue
        if dic[response[key]["result"]]:
            dic[response[key]["result"]] = dic[response[key]["result"]] + " , " + id
        else:
            dic[response[key]["result"]] = id

        # print(dic)
    del symptoms["vaginal_discharge"]
    del symptoms["sudden_onset_of_pain"]

    symptoms_modified = {key: 1 if value == "y" else 0 for key, value in symptoms.items()}

    symptoms.update(dic)
    # prediction_instance = Prediction(**symptoms)
    prediction_instance = Prediction(**symptoms_modified)
# ///////////////////////////////////////////////
    # db.session.add(prediction_instance)
    # db.session.commit()
# ///////////////////////////////////////////////
    # print("done "* 50)
    
    


# send feedback

@app.route('/feedback', methods=['POST'])
def sendFeedback():
    # Your Flask function logic here
    data = request.get_json()
    feedback = data
    print("$"*6, data)
    msg = Message('Hash Chatbot Feedback', sender='mhrt2255@gmail.com', recipients=['mihret.tibebe239@gmail.com'])
    msg.body = feedback
    mail.send(msg)
    return 'Success'

# prediction

@app.route('/templates', methods=['POST'])
def predict():
    print("post request running ********************************")
    try:
        data = request.get_json()
        # print("Received JSON data:", data)

        symptoms = {
            'unusual_discharge': data.get('unusual_discharge', 'n'),
            'vaginal_itching': data.get('vaginal_itching', 'n'),
            'pain_during_urination': data.get('pain_during_urination', 'n'),
            'pain_during_sex': data.get('pain_during_sex', 'n'),
            'genital_sore': data.get('genital_sore', 'n'),
            'inguinal_swelling': data.get('inguinal_swelling', 'n'),
            'pain_below_umbilicus': data.get('pain_below_umbilicus', 'n'),
            'fever': data.get('fever', 'n'),
            'sex': data.get('sex', 'n'),
            'vaginal_discharge': data.get('vaginal_discharge', 'n'),
            'missed_menstrual_period': data.get('missed_menstrual_period', 'n'),
            'vaginal_bleeding': data.get('vaginal_bleeding', 'n'),
            'painful_inguinal_lymph_node_or_swelling_over_the_groin': data.get('painful_inguinal_lymph_node_or_swelling_over_the_groin', 'n'),
            'pus_discharge_from_swelling': data.get('pus_discharge_from_swelling', 'n'),
            'skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area': data.get('skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area', 'n'),
            'skin_lesions_on_between_fingerswrist_genital_area_buttock': data.get('skin_lesions_on_between_fingerswrist_genital_area_buttock', 'n'),
            'lice_or_nits_on_pubic_hair': data.get('lice_or_nits_on_pubic_hair', 'n'),
            'yellowing_of_the_eyes': data.get('yellowing_of_the_eyes', 'n'),
            'yellowing_of_the_skin': data.get('yellowing_of_the_skin', 'n'),
            'abdominal_pain': data.get('abdominal_pain', 'n'),
            'pubic_area_itching': data.get('pubic_area_itching', 'n'),
            'itching_worsening_at_night': data.get('itching_worsening_at_night', 'n'),
            'itching_over_the_thighs_axilla_eyelid': data.get('itching_over_the_thighs_axilla_eyelid', 'n'),
            'similar_complaint_in_the_family_or_vicinity': data.get('similar_complaint_in_the_family_or_vicinity', 'n'),
            'dark_urine': data.get('dark_urine', 'n'),

			# male only
            'urethral_discharge': data.get('urethral_discharge', 'n'),
            'frequent_urination': data.get('frequent_urination', 'n'),
            'scrotal_pain': data.get('scrotal_pain', 'n'),
            'sudden_onset_of_pain': data.get('sudden_onset_of_pain', 'n'),
            'swelling': data.get('swelling', 'n')
            
            
            # Add other symptoms as needed
        }

        # Call the expert system
        results = run_expert_system(**symptoms)

        response = {}
        for key, result in results.items():
            if result != "Unknown":
                if hasattr(result, 'other'):
                    response[key] = {'result': result.result, 'other': result.other}
                else:
                    response[key] = {'result': result.result}
            else:
                response[key] = {'result': result}
        # saveToDB(symptoms , response )
        return jsonify(response)

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(
        host ="0.0.0.0",
        port = 5000,
	debug=True)
