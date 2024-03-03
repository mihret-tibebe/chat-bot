from experta import *
from STDFacts import InguinalBuboFact
from STDFacts import ResultFact

class InguinalBuboSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
        InguinalBuboFact(
            painful_inguinal_lymph_node_or_swelling_over_the_groin="y",
			pus_discharge_from_swelling="y",
			fever="y"
        )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="y",
                pus_discharge_from_swelling="y",
                fever="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 3
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="y",
                pus_discharge_from_swelling="n",
                fever="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 4
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="y",
                pus_discharge_from_swelling="n",
                fever="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 1 L
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="n",
                pus_discharge_from_swelling="y",
                fever="y"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="n",
                pus_discharge_from_swelling="y",
                fever="n"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 1 UL
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="n",
                pus_discharge_from_swelling="n",
                fever="y"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            InguinalBuboFact(
                painful_inguinal_lymph_node_or_swelling_over_the_groin="n",
                pus_discharge_from_swelling="n",
                fever="n"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
