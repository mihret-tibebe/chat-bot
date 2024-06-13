from flask import Flask, render_template
from flask import Flask, request, jsonify, render_template, send_file
# from flask_sqlalchemy import SQLAlchemy
from inference_engine import run_expert_system
# from flask_mail import Mail, Message
from config import HOST, PORT, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
# from models import db, Prediction, Syndrom
from datetime import datetime, timedelta

app = Flask(__name__, static_folder='static')

# Configure mail settings
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'mhrt2255@gmail.com'
# app.config['MAIL_PASSWORD'] = 'cgij fdqk ogiy yibc'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/STDPrediction'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

@app.route('/mathematicalModel')
def mathematicalModel():
    pdf_file_path = 'static/pdfs/A_Mathematical_Model_of_STD.pdf'
    return send_file(pdf_file_path)
	# , as_attachment=True    #if downlading the file needed uncomment the previous code


def get_syndrom_id(key):
    syndrom = Syndrom.query.filter_by(symptom=key).first()
    if syndrom:
        return str(syndrom.id)
    return None

def saveToDB(symptoms , response):

    symptoms["skin_colored_raised_bumps"] = symptoms["skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area"]
    del symptoms["skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area"]

    dic = {
        "VL": "",
        "L":"",
        "M":""
		}

    for key in response:
        id = get_syndrom_id(key)

        if response[key]["result"] == "Unknown" or response[key]["result"] == "UL":
            continue
        if dic[response[key]["result"]]:
            dic[response[key]["result"]] = dic[response[key]["result"]] + " , " + id
        else:
            dic[response[key]["result"]] = id

    del symptoms["vaginal_discharge"]
    del symptoms["sudden_onset_of_pain"]
    symptoms = {key: 1 if value == "y" else (0 if value == "n" else ("f" if value == "female" else ("m" if value == "male" else None))) for key, value in symptoms.items()}

    symptoms.update(dic)
    prediction_instance = Prediction(**symptoms)
# ///////////////////////////////////////////////
    # db.session.add(prediction_instance)
    # db.session.commit()
# ///////////////////////////////////////////////


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


# WEEKLY REPORT/////////////////////////////////////////////////////
# wors without sorting

def get_top_syndromes_last_week(db):
    # Get the date from a week ago
    one_week_ago = datetime.now() - timedelta(days=7)

    # Query the database for predictions made after the specified date
    predictions = Prediction.query.filter(Prediction.created_at <= one_week_ago).all()
    print(predictions , "*"*30)
    # Initialize a dictionary to store syndrome counts (symptom name, count)
    syndrome_counts = {}
    for prediction in predictions:
        # Join and split syndromes from VL, L, and M columns
        # syndromes = " ".join([prediction.VL.strip(), prediction.L.strip(), prediction.M.strip()]).split()
        # print(prediction.VL.replace(" " , "").split(","))
        syndromes = prediction.VL.replace(" " , "").split(",")
        syndromes += prediction.L.replace(" " , "").split(",")

        # Filter out empty strings


        # Update syndrome counts using retrieved symptom names (assuming a query)
        for syndrome in syndromes:
            symptom_name = get_symptom_name(syndrome)
            if symptom_name:  # Check if symptom_name is not None
                syndrome_counts[symptom_name] = syndrome_counts.get(symptom_name, 0) + 1
        # sorted_syndromes = dict(sorted(syndrome_counts.items(), key=lambda item: item[1]))


    # Sort the dictionary by count in descending order and convert it to a list of tuples
    sorted_syndromes = sorted(syndrome_counts.items(), key=lambda item: item[1], reverse=True)
    sorted_dict_desc = dict(sorted(syndrome_counts.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_syndromes)

    # Return the top N syndromes (you can adjust the value of N as needed)
    # return syndrome_counts
    return sorted_dict_desc  # Return top 10 by default




def get_symptom_name(syndrome_id):
  # Implement logic to query the Syndrom table and retrieve the symptom name
  # based on the provided ID. This might involve using SQLAlchemy.
  #   print(syndrome_id)
  symptom = db.session.query(Syndrom).get(syndrome_id)
  if symptom:
      print(syndrome_id ,"->>>" ,  symptom.symptom)
      return symptom.symptom
  else:
      return None  # Handle cases where syndrome ID is not found in the table

# END OF WEEKLY REPORT//////////////////////////////////////////////
@app.route('/top_syndromes')
def get_top_syndromes():
    """
    This route retrieves the top registered syndromes from the last week.
    """
    top_syndromes = get_top_syndromes_last_week(db)
    print(top_syndromes)
    msg = Message('Top syndroms of the week', sender='mhrt2255@gmail.com', recipients=['mihret.tibebe239@gmail.com'])
    count = 0
    week_feedback = "<ul>"
    for x in top_syndromes:
        week_feedback += f"<li><b>Syndrom:</b> {x}, <b>count:</b> {top_syndromes[x]}</li>"
        count += 1
        if count == 3:
            break
        week_feedback += "</ul>"
    print(week_feedback)
    msg.html = week_feedback
    mail.send(msg)

    # print("hello world")
    # sorted_syndromes = {item[0]: item[1] for item in top_syndromes}
    return jsonify(top_syndromes)


if __name__ == '__main__':
    app.run(
        host ="0.0.0.0",
        port = 5000,
	debug=True)



