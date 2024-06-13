from experta import *
from STDFacts import GenitalWartsFact
from STDFacts import ResultFact


class GenitalWartsSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            GenitalWartsFact(
                skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 1 UL
	@Rule(
            GenitalWartsFact(
                skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
