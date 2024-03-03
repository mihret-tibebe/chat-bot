from experta import *
from STDFacts import PediculosisPubisFact
from STDFacts import ResultFact

class PediculosisPubisSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="y",
				itching_over_the_thighs_axilla_eyelid="y",
				lice_or_nits_on_pubic_hair="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 2
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="y",
				itching_over_the_thighs_axilla_eyelid="n",
				lice_or_nits_on_pubic_hair="y"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 3
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="n",
				itching_over_the_thighs_axilla_eyelid="y",
				lice_or_nits_on_pubic_hair="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 1 L
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="y",
				itching_over_the_thighs_axilla_eyelid="y",
				lice_or_nits_on_pubic_hair="n"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 2
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="y",
				itching_over_the_thighs_axilla_eyelid="n",
				lice_or_nits_on_pubic_hair="n"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 3
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="n",
				itching_over_the_thighs_axilla_eyelid="y",
				lice_or_nits_on_pubic_hair="n"
            )
        )
	def likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 4
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="n",
				itching_over_the_thighs_axilla_eyelid="n",
				lice_or_nits_on_pubic_hair="y"
            )
        )
	def likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 1 UL
	@Rule(
            PediculosisPubisFact(
                pubic_area_itching="n",
				itching_over_the_thighs_axilla_eyelid="n",
				lice_or_nits_on_pubic_hair="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
