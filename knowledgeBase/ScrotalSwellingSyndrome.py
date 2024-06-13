from experta import *
from STDFacts import ScrotalSwellingFact
from STDFacts import ResultFact


class ScrotalSwellingSyndrome(KnowledgeEngine):
    # 1 VL
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="y",
				pain_during_urination="y",
				swelling="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="n",
				pain_during_urination="y",
				swelling="y"
            )
        )
	def very_likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 3
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="n",
				pain_during_urination="n",
				swelling="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)\
    # 1 L
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="n",
				pain_during_urination="y",
				swelling="n"
            )
        )
	def likely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="n",
				pain_during_urination="y",
				swelling="y"
            )
        )
	def likely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 3
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="n",
				pain_during_urination="n",
				swelling="n"
            )
        )
	def likely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 4
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="n",
				pain_during_urination="y",
				swelling="n"
            )
        )
	def likely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 5
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="n",
				pain_during_urination="n",
				swelling="y"
            )
        )
	def likely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 1 UL
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="y",
				pain_during_urination="y",
				swelling="n"
            )
        )
	def unlikely_1(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 2
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="y",
				pain_during_urination="n",
				swelling="y"
            )
        )
	def unlikely_2(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 3
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="y",
				pain_during_urination="n",
				swelling="n"
            )
        )
	def unlikely_3(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 4
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="y",
				pain_during_urination="y",
				swelling="n"
            )
        )
	def unlikely_4(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		new_result_fact.other = "Scrotal Torsion"
		self.declare(new_result_fact)
	# 5
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="y",
				pain_during_urination="n",
				swelling="y"
            )
        )
	def unlikely_5(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 6
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="y",
				pain_during_urination="y",
				swelling="y"
            )
        )
	def unlikely_6(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 7
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="y",
                sudden_onset_of_pain="y",
				pain_during_urination="n",
				swelling="n"
            )
        )
	def unlikely_7(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 8
	@Rule(
            ScrotalSwellingFact(
                scrotal_pain="n",
                sudden_onset_of_pain="n",
				pain_during_urination="n",
				swelling="n"
            )
        )
	def unlikely_8(self):
		new_result_fact = ResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
