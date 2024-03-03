from experta import *
from STDFacts import VaginalDischargeFact
from STDFacts import ResultFact

class VaginalDischargeSyndrome(KnowledgeEngine):
    # 1
    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="y",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="y"
        )
        # salience=10  # Higher salience value
    )
    def very_likely_1(self):
        # self.declare(ResultFact(result="VL"))
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
	# 2

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="y",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="n"
        )
    )
    def very_likely_2(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 3

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="y",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="y"
        )
    )
    def very_likely_3(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 4

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="n",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="y"
        )
    )
    def very_likely_4(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 5

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="y",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="n"
        )
    )
    def very_likely_5(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 6

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="n",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="n"
        )
    )
    def very_likely_6(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 7

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="n",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="y"
        )
    )
    def very_likely_7(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)
    # 8

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="y",
            vaginal_itching="n",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="n"
        )
    )
    def very_likely_8(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "VL"
        self.declare(new_result_fact)

	# Medium
	# 1
    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="y",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="y"
        )
    )
    def medium_1(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        self.declare(new_result_fact)
    # 2

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="y",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="n"
        )
    )
    def medium_2(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        self.declare(new_result_fact)
    # 3

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="y",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="y"
        )
    )
    def medium_3(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        self.declare(new_result_fact)
    # 4

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="n",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="y"
        )
    )
    def medium_4(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        self.declare(new_result_fact)
    # 5

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="y",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="n"
        )
    )
    def medium_5(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        new_result_fact.other = "other skin diseasis"
        self.declare(new_result_fact)
    # 6

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="n",
            # pain_urination="y",
            pain_during_urination="y",
            pain_during_sex="n"
        )
    )
    def medium_6(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        new_result_fact.other = "UTI - Urinary tract infection"
        self.declare(new_result_fact)
    # 7

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="n",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="y"
        )
    )
    def medium_6(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "M"
        self.declare(new_result_fact)
    # UL

    @Rule(
        VaginalDischargeFact(
            unusual_discharge="n",
            vaginal_itching="n",
            # pain_urination="n",
            pain_during_urination="n",
            pain_during_sex="n"
        )
    )
    def ul(self):
        new_result_fact = ResultFact()
        new_result_fact.result = "UL"
        self.declare(new_result_fact)
