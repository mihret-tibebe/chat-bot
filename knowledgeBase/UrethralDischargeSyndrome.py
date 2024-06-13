from experta import *
from STDFacts import UrethralDischargeFact
from STDFacts import ResultFact

class UrethralDischargeSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            UrethralDischargeFact(
                urethral_discharge="y",
                pain_during_urination="y",
                frequent_urination="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 2

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="y",
                pain_during_urination="y",
                frequent_urination="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 3

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="y",
                pain_during_urination="n",
                frequent_urination="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 1 L

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="y",
                pain_during_urination="n",
                frequent_urination="n"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 1 M

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="n",
                pain_during_urination="y",
                frequent_urination="y"
            )
        )
	def medium_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		new_result_fact.other = "UTI"
		self.declare(new_result_fact)
    # 2

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="n",
                pain_during_urination="y",
                frequent_urination="n"
            )
        )
	def medium_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		new_result_fact.other = "UTI"
		self.declare(new_result_fact)
    # 1 UL

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="n",
                pain_during_urination="y",
                frequent_urination="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		new_result_fact.other = "multiple causes"
		self.declare(new_result_fact)
    # 2

	@Rule(
            UrethralDischargeFact(
                urethral_discharge="n",
                pain_during_urination="n",
                frequent_urination="n"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
