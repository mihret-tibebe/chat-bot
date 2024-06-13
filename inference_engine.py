from knowledgeBase.VaginalDischargeSyndrome import *
from knowledgeBase.LowerAbdominalPainSyndrome import *
from knowledgeBase.UrethralDischargeSyndrome import *
from knowledgeBase.ScrotalSwellingSyndrome import *
from knowledgeBase.GenitalUlcerSyndrome import *
from knowledgeBase.InguinalBuboSyndrome import *
from knowledgeBase.GenitalWartsSyndrome import *
from knowledgeBase.ScabiesSyndrome import *
from knowledgeBase.PediculosisPubisSyndrome import *
from knowledgeBase.ViralHepatititisSyndrome import *


def run_expert_system(**kwargs):
# vaginal discharge symptoms
	unusual_discharge = kwargs.get('unusual_discharge', "")
	vaginal_itching = kwargs.get('vaginal_itching', "")
	# pain_urination = kwargs.get('pain_during_urination', "")
	pain_during_urination = kwargs.get('pain_during_urination', "")
	pain_during_sex = kwargs.get('pain_during_sex', "")

# uretheral discharge symptoms
	urethral_discharge = kwargs.get('urethral_discharge', "")
	pain_during_urination = kwargs.get('pain_during_urination', "")
	frequent_urination = kwargs.get('frequent_urination', "")

# scrotal swelling
	scrotal_pain = kwargs.get('scrotal_pain', "")
	sudden_onset_of_pain =  kwargs.get('sudden_onset_of_pain', "")
	# pain_during_urination =  kwargs.get('pain_during_urination', "")            # repeated
	swelling =  kwargs.get('swelling', "")

# genital ulcer symptoms
	genital_sore = kwargs.get('genital_sore', "")
	inguinal_swelling = kwargs.get('inguinal_swelling', "")

# lower abdomenal pain
	pain_below_umbilicus = kwargs.get('pain_below_umbilicus', "")
	fever = kwargs.get('fever', "")
	vaginal_discharge = kwargs.get('vaginal_discharge', "")
	missed_menstrual_period = kwargs.get('missed_menstrual_period', "")
	vaginal_bleeding = kwargs.get('vaginal_bleeding', "")

# induinal bubo
	painful_inguinal_lymph_node_or_swelling_over_the_groin = kwargs.get('painful_inguinal_lymph_node_or_swelling_over_the_groin', "")
	pus_discharge_from_swelling = kwargs.get('pus_discharge_from_swelling', "")
	fever = kwargs.get('fever', "")		# repeated

# genital warts
	skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area = kwargs.get('skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area', "")

# scabies
	skin_lesions_on_between_fingerswrist_genital_area_buttock = kwargs.get('skin_lesions_on_between_fingerswrist_genital_area_buttock', "")
	itching_worsening_at_night = kwargs.get('itching_worsening_at_night', "")
	similar_complaint_in_the_family_or_vicinity = kwargs.get('similar_complaint_in_the_family_or_vicinity', "")

# pediculosis pubis
	pubic_area_itching = kwargs.get('pubic_area_itching', "")
	itching_over_the_thighs_axilla_eyelid = kwargs.get('itching_over_the_thighs_axilla_eyelid', "")
	lice_or_nits_on_pubic_hair = kwargs.get('lice_or_nits_on_pubic_hair', "")

# viral hepatitis
	yellowing_of_the_eyes = kwargs.get('yellowing_of_the_eyes', "")
	yellowing_of_the_skin = kwargs.get('yellowing_of_the_skin', "")    
	abdominal_pain = kwargs.get('abdominal_pain', "")    
	dark_urine = kwargs.get('dark_urine', "")
    
	vd_engine = VaginalDischargeSyndrome()  
	vd_engine.reset()
	lap_engine = LowerAbdominalPainSyndrome()
	lap_engine.reset()
	ud_engine = UrethralDischargeSyndrome()
	ud_engine.reset
	ss_engine = ScrotalSwellingSyndrome()
	ss_engine.reset()
	gu_engine = GenitalUlcerSyndrome()
	gu_engine.reset()
	ib_engine = InguinalBuboSyndrome()
	ib_engine.reset()
	gw_engine = GenitalWartsSyndrome()
	gw_engine.reset()
	s_engine = ScabiesSyndrome()
	s_engine.reset()
	pp_engine = PediculosisPubisSyndrome()
	pp_engine.reset()
	vh_engine = ViralHepatititisSyndrome()
	vh_engine.reset()

	# print("***", **kwargs)

	vd_engine.declare(VaginalDischargeFact(
        unusual_discharge=unusual_discharge,
        vaginal_itching=vaginal_itching,
        # pain_urination=pain_urination,
        pain_during_urination=pain_during_urination,
        pain_during_sex=pain_during_sex
    ))

	lap_engine.declare(LowerAbdominalPainFact(
		pain_below_umbilicus=pain_below_umbilicus,
        fever=fever,
        vaginal_discharge=vaginal_discharge,  # umbigues
        missed_menstrual_period=missed_menstrual_period,
        pain_during_sex=pain_during_sex,
        vaginal_bleeding=vaginal_bleeding
	))

	ud_engine.declare(UrethralDischargeFact(
            urethral_discharge=urethral_discharge,
			pain_during_urination=pain_during_urination,
			frequent_urination=frequent_urination
        ))
	
	ss_engine.declare(ScrotalSwellingFact(
		scrotal_pain=scrotal_pain,
		sudden_onset_of_pain=sudden_onset_of_pain,
		pain_during_urination=pain_during_urination,
		swelling=swelling
	))

	gu_engine.declare(GenitalUlcerFact(
		genital_sore=genital_sore,
            inguinal_swelling=inguinal_swelling
	))

	ib_engine.declare(InguinalBuboFact(
		painful_inguinal_lymph_node_or_swelling_over_the_groin=painful_inguinal_lymph_node_or_swelling_over_the_groin,
        pus_discharge_from_swelling=pus_discharge_from_swelling,
        fever=fever
	))

	gw_engine.declare(GenitalWartsFact(
		skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area=skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area
	))

	s_engine.declare(ScabiesFact(
		skin_lesions_on_between_fingerswrist_genital_area_buttock=skin_lesions_on_between_fingerswrist_genital_area_buttock,
        itching_worsening_at_night=itching_worsening_at_night,
        similar_complaint_in_the_family_or_vicinity=similar_complaint_in_the_family_or_vicinity
	))

	pp_engine.declare(PediculosisPubisFact(
		pubic_area_itching=pubic_area_itching,
		itching_over_the_thighs_axilla_eyelid=itching_over_the_thighs_axilla_eyelid,
		lice_or_nits_on_pubic_hair=lice_or_nits_on_pubic_hair
	))

	vh_engine.declare(ViralHepatititisFact(
		yellowing_of_the_eyes=yellowing_of_the_eyes,
        yellowing_of_the_skin=yellowing_of_the_skin,
        abdominal_pain=abdominal_pain,
        dark_urine=dark_urine
	))

	vd_engine.run()
	lap_engine.run()
	ud_engine.run()
	ss_engine.run()
	gu_engine.run()
	ib_engine.run()
	gw_engine.run()
	s_engine.run()
	pp_engine.run()
	vh_engine.run()

	results = {}

# 1 VD
	for fact in vd_engine.facts.values():
		# print(fact)
		if isinstance(fact, ResultFact):            
			result_fact = fact      
		else:            
			result_fact = None
	if result_fact is not None:
		results[vd_engine.__class__.__name__] = result_fact
	else:
		results[vd_engine.__class__.__name__] = "Unknown"

# 2 UD
	for fact in ud_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[ud_engine.__class__.__name__] = result_fact
	else:
		results[ud_engine.__class__.__name__] = "Unknown"

# 3 GU
	for fact in gu_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[gu_engine.__class__.__name__] = result_fact
	else:
		results[gu_engine.__class__.__name__] = "Unknown"

# 4 LAP
	for fact in lap_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[lap_engine.__class__.__name__] = result_fact
	else:
		results[lap_engine.__class__.__name__] = "Unknown"

# 5
	for fact in ss_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[ss_engine.__class__.__name__] = result_fact
	else:
		results[ss_engine.__class__.__name__] = "Unknown"

# 6
	for fact in ib_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[ib_engine.__class__.__name__] = result_fact
	else:
		results[ib_engine.__class__.__name__] = "Unknown"

# 7
	for fact in gw_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[gw_engine.__class__.__name__] = result_fact
	else:
		results[gw_engine.__class__.__name__] = "Unknown"

# 8
	for fact in s_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[s_engine.__class__.__name__] = result_fact
	else:
		results[s_engine.__class__.__name__] = "Unknown"

# 9
	for fact in pp_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[pp_engine.__class__.__name__] = result_fact
	else:
		results[pp_engine.__class__.__name__] = "Unknown"

# 10
	for fact in vh_engine.facts.values():
		if isinstance(fact, ResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[vh_engine.__class__.__name__] = result_fact
	else:
		results[vh_engine.__class__.__name__] = "Unknown"

	# return "Unknown"
	return results
