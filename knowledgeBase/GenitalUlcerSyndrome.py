from experta import *
from STDFacts import GenitalUlcerFact
from STDFacts import ResultFact

class GenitalUlcerSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            GenitalUlcerFact(
                genital_sore="y",
                inguinal_swelling="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 2

	@Rule(
            GenitalUlcerFact(
                genital_sore="y",
                inguinal_swelling="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 1 M

	@Rule(
            GenitalUlcerFact(
                genital_sore="n",
                inguinal_swelling="y"
            )
        )
	def medium(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
    # 1 UL

	@Rule(
            GenitalUlcerFact(
                genital_sore="n",
                inguinal_swelling="n"
            )
        )
	def unlikely(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
