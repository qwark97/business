from business.assumptions import StageAssumptions
from business.balance import Assets


class Model:
    def __init__(self, assets: Assets, assumptions: StageAssumptions):
        self.__stage = 1
        self.__year = 0
        self.__assumptions = assumptions
        self.__assets = assets

    def next_stage(self, assumptions: StageAssumptions):
        self.__stage += 1
        self.__assumptions = assumptions

    def next_year(self):
        self.__year += 1
        #
        # some events
        #
