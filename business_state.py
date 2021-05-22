from business.assumptions import StageAssumptions
from business.balance import Balance


class Model:
    def __init__(self, balance: Balance, assumptions: StageAssumptions):
        self.__stage = 1
        self.__year = 0
        self.__assumptions = assumptions
        self.__balance = balance

    def next_stage(self, assumptions: StageAssumptions):
        self.__stage += 1
        self.__assumptions = assumptions

    def next_year(self):
        self.__year += 1
