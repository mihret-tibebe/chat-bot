from experta import *
from STDFacts import ScabiesFact
from STDFacts import ResultFact

class ScabiesSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="y",
				itching_worsening_at_night="y",
				similar_complaint_in_the_family_or_vicinity="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="y",
				itching_worsening_at_night="y",
				similar_complaint_in_the_family_or_vicinity="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 3
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="y",
				itching_worsening_at_night="n",
				similar_complaint_in_the_family_or_vicinity="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 1 L
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="n",
				itching_worsening_at_night="y",
				similar_complaint_in_the_family_or_vicinity="y"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="y",
				itching_worsening_at_night="n",
				similar_complaint_in_the_family_or_vicinity="n"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 3
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="n",
				itching_worsening_at_night="y",
				similar_complaint_in_the_family_or_vicinity="n"
            )
        )
	def likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 1 UL
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="n",
				itching_worsening_at_night="n",
				similar_complaint_in_the_family_or_vicinity="y"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScabiesFact(
                skin_lesions_on_between_fingerswrist_genital_area_buttock="n",
				itching_worsening_at_night="n",
				similar_complaint_in_the_family_or_vicinity="n"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
