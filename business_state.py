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
        # zarobienie hajsu
        promised_income = self._count_income()
        real_income = self._subtract_unpaid(promised_income)
        income = real_income - self.__assumptions.fixed_costs_number
        profit = self._tax(income)

        self.__assets.add_earnings(profit)
        # minus naturalna strata
        self.__assets.natural_machinery_loss(self.__assumptions.natural_loss_percentage)
        # minus koszty niespodziewane
        self.__assets.unexpected_loss(self.__assumptions.unexpected_cost_probability_percentage, self.__assumptions.unexpected_costs_number)
        return self.__assets.sum_up()

    def _count_income(self) -> float:
        income = 0
        clients = self.__assumptions.clients_number
        for _ in range(clients):
            income += self.__assumptions.average_income_per_client_number * (self.__assumptions.average_margin_per_client_percentage / 100)
        return income

    def _subtract_unpaid(self, promised_income: float) -> float:
        paid_percentage = 100 - self.__assumptions.lost_income_percentage
        return promised_income * (paid_percentage / 100)

    def _tax(self, income):
        percentage_left_after_taxation = 100 - self.__assumptions.yearly_tax_percentage
        return income * (percentage_left_after_taxation / 100)







