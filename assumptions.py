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
                 average_margin_per_client_percentage:      (int, int),
                 yearly_tax_percentage:                     int,
                 unexpected_cost_probability_percentage:    (int, int),
                 unexpected_costs_number:                   (float, int),
                 fixed_costs_number:                        (float, int),
                 investment_rate_percentage:                (float, int),
                 ):
        self.__lost_income_percentage = lost_income_percentage  # due to unpaid debts
        self.__natural_loss_percentage = natural_loss_percentage  # due to natural events such as exploration
        self.__clients_number = clients_number
        self.__average_income_per_client_number = average_income_per_client_number
        self.__average_margin_per_client_percentage = average_margin_per_client_percentage
        self.__yearly_tax_percentage = yearly_tax_percentage
        self.__unexpected_cost_probability_percentage = unexpected_cost_probability_percentage
        self.__unexpected_costs_number = unexpected_costs_number
        self.__fixed_costs_number = fixed_costs_number
        self.__investment_rate_percentage = investment_rate_percentage

    # Wszystkie poniższe wartości (z wyjątkiem stawki podatku), dla każdego ich użycia wyliczają swoją wartość
    # na dany moment. Uzyskanie tejże polega na wzięciu wartości przekazanej w ramach konstruktora z uwzględnieniem
    # wartości odchylenia standardowego, które również jest przekazywane w ramach inicjalizacji obiektu. W ten sposób
    # każde wykorzystanie pozwala zasymulować zmienność systemu
    # Stawka podatku jest tutaj wyjątkiem - ona zawsze jest zgodna z wartością przekazaną w ramach konstruktora bez
    # żadnych modyfikacji (z wyjątkiem przekazania wartości mniejszej od 0, wtedy stawka podatku wynosi 0)

    @property
    def lost_income_percentage(self):
        return max(normal(*self.__lost_income_percentage), 0)

    @property
    def natural_loss_percentage(self):
        return max(normal(*self.__natural_loss_percentage), 0)

    @property
    def clients_number(self):
        return max(int(normal(*self.__clients_number)), 0)

    @property
    def average_income_per_client_number(self):
        return max(normal(*self.__average_income_per_client_number), 0)

    @property
    def average_margin_per_client_percentage(self):
        return max(normal(*self.__average_margin_per_client_percentage), 0)

    @property
    def yearly_tax_percentage(self):
        return max(self.__yearly_tax_percentage, 0)

    @property
    def unexpected_cost_probability_percentage(self):
        return max(normal(*self.__unexpected_cost_probability_percentage), 0)

    @property
    def unexpected_costs_number(self):
        return max(normal(*self.__unexpected_costs_number), 0)

    @property
    def fixed_costs_number(self):
        return max(normal(*self.__fixed_costs_number), 0)

    @property
    def investment_rate_percentage(self):
        return max(normal(*self.__investment_rate_percentage), 0)
