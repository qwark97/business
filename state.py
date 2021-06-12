DATABASE = []


class State:
    def __init__(self):
        self.__stage = 0
        self.__year = 0
        self.__wealth_at_the_beginning_of_the_year = 0
        self.__wealth_at_the_end_of_the_year = 0
        self.__money_at_the_beginning_of_the_year = 0
        self.__money_at_the_end_of_the_year = 0
        self.__machinery_at_the_beginning_of_the_year = 0
        self.__machinery_at_the_end_of_the_year = 0
        self.__money_income_in_the_year = 0
        self.__money_outcome_in_the_year = 0
        self.__unpaid_loss_in_the_year = 0
        self.__fixed_costs_in_the_year = 0
        self.__tax_in_the_year = 0
        self.__natural_machinery_loss_in_the_year = 0
        self.__investments_in_the_year = 0
        self.__unexpected_loss_in_the_year = 0

    def _reset_values(self):
        self.__stage = 0
        self.__year = 0
        self.__wealth_at_the_beginning_of_the_year = 0
        self.__wealth_at_the_end_of_the_year = 0
        self.__money_at_the_beginning_of_the_year = 0
        self.__money_at_the_end_of_the_year = 0
        self.__machinery_at_the_beginning_of_the_year = 0
        self.__machinery_at_the_end_of_the_year = 0
        self.__money_income_in_the_year = 0
        self.__money_outcome_in_the_year = 0
        self.__unpaid_loss_in_the_year = 0
        self.__fixed_costs_in_the_year = 0
        self.__tax_in_the_year = 0
        self.__natural_machinery_loss_in_the_year = 0
        self.__investments_in_the_year = 0
        self.__unexpected_loss_in_the_year = 0

    def set_stage(self, value):
        self.__stage = value

    def set_year(self, value):
        self.__year = value

    def set_wealth_at_the_beginning_of_the_year(self, value):
        self.__wealth_at_the_beginning_of_the_year = value

    def set_wealth_at_the_end_of_the_year(self, value):
        self.__wealth_at_the_end_of_the_year = value

    def set_money_at_the_beginning_of_the_year(self, value):
        self.__money_at_the_beginning_of_the_year = value

    def set_money_at_the_end_of_the_year(self, value):
        self.__money_at_the_end_of_the_year = value

    def set_machinery_at_the_beginning_of_the_year(self, value):
        self.__machinery_at_the_beginning_of_the_year = value

    def set_machinery_at_the_end_of_the_year(self, value):
        self.__machinery_at_the_end_of_the_year = value

    def set_money_income_in_the_year(self, value):
        self.__money_income_in_the_year = value

    def set_money_outcome_in_the_year(self, value):
        self.__money_outcome_in_the_year = value

    def set_unpaid_loss_in_the_year(self, value):
        self.__unpaid_loss_in_the_year = value

    def set_fixed_costs_in_the_year(self, value):
        self.__fixed_costs_in_the_year = value

    def set_tax_in_the_year(self, value):
        self.__tax_in_the_year = value

    def set_natural_machinery_loss_in_the_year(self, value):
        self.__natural_machinery_loss_in_the_year = value

    def set_investments_in_the_year(self, value):
        self.__investments_in_the_year = value

    def set_unexpected_loss_in_the_year(self, value):
        self.__unexpected_loss_in_the_year = value

    def save(self):
        data = {
            "stage": self.__stage,
            "year": self.__year,
            "wealth_at_the_beginning_of_the_year": self.__wealth_at_the_beginning_of_the_year,
            "wealth_at_the_end_of_the_year": self.__wealth_at_the_end_of_the_year,
            "money_at_the_beginning_of_the_year": self.__money_at_the_beginning_of_the_year,
            "money_at_the_end_of_the_year": self.__money_at_the_end_of_the_year,
            "machinery_at_the_beginning_of_the_year": self.__machinery_at_the_beginning_of_the_year,
            "machinery_at_the_end_of_the_year": self.__machinery_at_the_end_of_the_year,
            "money_income_in_the_year": self.__money_income_in_the_year,
            "money_outcome_in_the_year": self.__money_outcome_in_the_year,
            "unpaid_loss_in_the_year": self.__unpaid_loss_in_the_year,
            "fixed_costs_in_the_year": self.__fixed_costs_in_the_year,
            "tax_in_the_year": self.__tax_in_the_year,
            "natural_machinery_loss_in_the_year": self.__natural_machinery_loss_in_the_year,
            "investments_in_the_year": self.__investments_in_the_year,
            "unexpected_loss_in_the_year": self.__unexpected_loss_in_the_year,
        }
        DATABASE.append(data)
        self._reset_values()
