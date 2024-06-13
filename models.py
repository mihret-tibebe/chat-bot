from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sex = db.Column(db.String(1), nullable=False)
    unusual_discharge = db.Column(db.Integer)
    # f_color_change = db.Column(db.Integer)
    # f_bad_odor = db.Column(db.Integer)
    vaginal_itching = db.Column(db.Integer)
    pain_during_urination = db.Column(db.Integer)
    pain_during_sex = db.Column(db.Integer)
    pain_below_umbilicus = db.Column(db.Integer)
    fever = db.Column(db.Integer)
    missed_menstrual_period = db.Column(db.Integer)
    vaginal_bleeding = db.Column(db.Integer)
    painful_inguinal_lymph_node_or_swelling_over_the_groin = db.Column(db.Integer)
    pus_discharge_from_swelling = db.Column(db.Integer)
    genital_sore = db.Column(db.Integer)
    inguinal_swelling = db.Column(db.Integer)
    skin_colored_raised_bumps = db.Column(db.Integer)
    skin_lesions_on_between_fingerswrist_genital_area_buttock = db.Column(db.Integer)
    itching_worsening_at_night = db.Column(db.Integer)
    similar_complaint_in_the_family_or_vicinity = db.Column(db.Integer)
    pubic_area_itching = db.Column(db.Integer)
    itching_over_the_thighs_axilla_eyelid = db.Column(db.Integer)
    lice_or_nits_on_pubic_hair = db.Column(db.Integer)
    yellowing_of_the_eyes = db.Column(db.Integer)
    yellowing_of_the_skin = db.Column(db.Integer)
    abdominal_pain = db.Column(db.Integer)
    swelling = db.Column(db.Integer)
    scrotal_pain = db.Column(db.Integer)
    dark_urine = db.Column(db.Integer)
    urethral_discharge = db.Column(db.Integer)
    # m_color_change = db.Column(db.Integer)
    # m_bad_odor = db.Column(db.Integer)
    frequent_urination = db.Column(db.Integer)
    VL = db.Column(db.String(50))
    L = db.Column(db.String(50))
    M = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
	return '<User %r>' % self.username

class Syndrom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symptom = db.Column(db.String(50), nullable=False)