from experta import *
from STDFacts import LowerAbdominalPainFact
from STDFacts import ResultFact

class LowerAbdominalPainSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
				vaginal_discharge="y", # umbigues
				missed_menstrual_period="n",
				pain_during_sex="y",
				vaginal_bleeding="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
				vaginal_discharge="y",
				missed_menstrual_period="n",
				pain_during_sex="y",
				vaginal_bleeding="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 3
	@Rule(
			LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
				vaginal_discharge="y",
				missed_menstrual_period="n",
				pain_during_sex="n",
				vaginal_bleeding="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 4
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 5
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def very_likely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 6
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def very_likely_6(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 7
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def very_likely_7(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 8
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def very_likely_8(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 9
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def very_likely_9(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 10
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def very_likely_10(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 11
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def very_likely_11(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 12
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def very_likely_12(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 1 M
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		new_result_fact.other = "Ectopic Pregnancy"
		self.declare(new_result_fact)
	# 2
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 3
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 4
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 5
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 6
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_6(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 7
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_7(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 8
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_8(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 9
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_9(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 10
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_10(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 11
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_11(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 12
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_12(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 13
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_13(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 14
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_14(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 15
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_15(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 16
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_16(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 17
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_17(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 18
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_18(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 19
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_19(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 20
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_20(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 21
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_21(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 22
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_22(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 23
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_23(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 24
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_24(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 25
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_25(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 26
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_26(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 27
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_27(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 28
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_28(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 29
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_29(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 30
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_30(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 31
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_31(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 32
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_32(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 33
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_33(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 34
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_34(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 35
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_35(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 36
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def medium_36(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 37
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="y",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def medium_37(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 38
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def medium_38(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	# 39
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def medium_38(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "M"
		self.declare(new_result_fact)
	
	# 1 L
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 3
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 4
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 5
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="y"
            )
        )
	def likely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 6
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="y",
                vaginal_bleeding="n"
            )
        )
	def likely_6(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 7
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def likely_7(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 8
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="y",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def likely_8(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 1 UL
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="n",
                fever="y",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 3
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="y"
            )
        )
	def unlikely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 4
	@Rule(
            LowerAbdominalPainFact(
                pain_below_umbilicus="y",
                fever="n",
                vaginal_discharge="n",
                missed_menstrual_period="n",
                pain_during_sex="n",
                vaginal_bleeding="n"
            )
        )
	def unlikely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
