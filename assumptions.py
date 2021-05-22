from numpy.random import normal


class StageAssumptions:
    """
    Arguments passed in __init__ are: value (percentage, amount or number of clients) and standard deviation to
    count "proper" value when needed
    """
    def __init__(self,
                 lost_income_percentage:                    (int, int),
                 natural_loss_percentage:                   (int, int),
                 clients_number:                            (int, int),
                 average_income_per_client_number:          (float, int),
                 yearly_tax_percentage:                     (int, int),
                 unexpected_cost_probability_percentage:    (int, int),
                 unexpected_cost_number:                    (float, int),
                 ):
        self.__lost_income_percentage = lost_income_percentage  # due to unpaid debts
        self.__natural_loss_percentage = natural_loss_percentage  # due to natural events such as exploration
        self.__clients_number = clients_number
        self.__average_income_per_client_number = average_income_per_client_number
        self.__yearly_tax_percentage = yearly_tax_percentage
        self.__unexpected_cost_probability_percentage = unexpected_cost_probability_percentage
        self.__unexpected_cost_number = unexpected_cost_number

    @property
    def lost_income_percentage(self):
        return normal(*self.__lost_income_percentage)

    @property
    def natural_loss_percentage(self):
        return normal(*self.__natural_loss_percentage)

    @property
    def clients_number(self):
        return int(normal(*self.__clients_number))

    @property
    def average_income_per_client_number(self):
        return normal(*self.__average_income_per_client_number)

    @property
    def yearly_tax_percentage(self):
        return normal(*self.__yearly_tax_percentage)

    @property
    def unexpected_cost_probability_percentage(self):
        return normal(*self.__unexpected_cost_probability_percentage)

    @property
    def unexpected_cost_number(self):
        return normal(*self.__unexpected_cost_number)
