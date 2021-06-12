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
        money_at_the_beginning = self.__assets.money

        promised_income = self._count_income()
        self.__assets.add_earnings(promised_income)

        unpaid_loss = self._unpaid(promised_income)
        self.__assets.unpaid_income(unpaid_loss)

        self.__assets.substract_fixed_costs(self.__assumptions.fixed_costs_number)

        tax = self._tax(max(self.__assets.money - money_at_the_beginning, 0))
        self.__assets.substract_tax(tax)

        # minus naturalna strata
        self.__assets.natural_machinery_loss(self.__assumptions.natural_loss_percentage)
        # minus koszty niespodziewane
        self.__assets.unexpected_loss(self.__assumptions.unexpected_cost_probability_percentage, self.__assumptions.unexpected_costs_number)
        yearly_income, yearly_outcome = self.__assets.get_cash_flow()
        self.__assets.new_year()
        return self.__assets.sum_up(), yearly_income, yearly_outcome

    def _count_income(self) -> float:
        income = 0
        clients = self.__assumptions.clients_number
        for _ in range(clients):
            income += self.__assumptions.average_income_per_client_number * (self.__assumptions.average_margin_per_client_percentage / 100)
        return income

    def _unpaid(self, promised_income: float) -> float:
        return promised_income * (self.__assumptions.lost_income_percentage / 100)

    def _tax(self, income):
        return income * (self.__assumptions.yearly_tax_percentage / 100)







