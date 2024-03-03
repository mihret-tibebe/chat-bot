from experta import *
from STDFacts import ViralHepatititisFact
from STDFacts import ResultFact

class ViralHepatititisSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="y",
				abdominal_pain="y",
				dark_urine="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 2
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="y",
				abdominal_pain="y",
				dark_urine="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 3
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="y",
				abdominal_pain="n",
				dark_urine="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 4
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="n",
				abdominal_pain="y",
				dark_urine="y"
            )
        )
	def very_likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 5
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="y",
				abdominal_pain="y",
				dark_urine="y"
            )
        )
	def very_likely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 6
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="y",
				abdominal_pain="n",
				dark_urine="n"
            )
        )
	def very_likely_6(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 7
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="n",
				abdominal_pain="y",
				dark_urine="n"
            )
        )
	def very_likely_7(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 8
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="n",
				abdominal_pain="n",
				dark_urine="y"
            )
        )
	def very_likely_8(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
    # 1 L
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="y",
				abdominal_pain="y",
				dark_urine="n"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 2
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="y",
				abdominal_pain="n",
				dark_urine="y"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 3
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="n",
				abdominal_pain="y",
				dark_urine="y"
            )
        )
	def likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 4
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="y",
				yellowing_of_the_skin="n",
				abdominal_pain="n",
				dark_urine="n"
            )
        )
	def likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 5
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="y",
				abdominal_pain="n",
				dark_urine="n"
            )
        )
	def likely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
    # 1 UL
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="n",
				abdominal_pain="y",
				dark_urine="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
    # 2
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="n",
				abdominal_pain="n",
				dark_urine="y"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
    # 3
	@Rule(
            ViralHepatititisFact(
                yellowing_of_the_eyes="n",
				yellowing_of_the_skin="n",
				abdominal_pain="n",
				dark_urine="n"
            )
        )
	def unlikely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
