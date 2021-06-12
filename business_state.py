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
        # na początku nowego roku zapisywane są dotychczasowe zasoby gotówkowe aby móc wyliczyć
        # zyski w danym roku
        money_at_the_beginning = self.__assets.money

        # w tym miejscu następuje wyliczenie dochodów (na tym etapie przychód - koszty);
        # szczegóły w jaki sposób wyliczany jest dochód znajdują się w ramach użytej metody
        promised_revenue = self._count_revenue()
        self.__assets.add_earnings(promised_revenue)

        # następnie od uzyskanego przychodu odejmowana jest kwota należności, które
        # z jakichś losowych powodów nie zostały opłacone;
        # szczegóły dotyczące tego jaka kwota i czy w ogóle przepada znajdują się w ramach użytej metody
        unpaid_loss = self._unpaid(promised_revenue)
        self.__assets.unpaid_income(unpaid_loss)

        # kolejno, od uzyskanych dochodów odejmowane są koszty stałe z danego roku;
        # wartość kosztów stałych jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        self.__assets.subtract_fixed_costs(self.__assumptions.fixed_costs_number)

        # na koniec, od zysku uzyskanego w rozważanym roku odejmowany jest podatek
        # wartość podatku wyliczana jest zgodnie z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        tax = self._tax(max(self.__assets.money - money_at_the_beginning, 0))
        self.__assets.subtract_tax(tax)

        # na tym etapie pomniejszana jest wartość maszyn posiadanych w przedsiębiorstwie
        # ze względu na naturalne zużycie
        # wartość konkretnych kwot jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        self.__assets.natural_machinery_loss(self.__assumptions.natural_loss_percentage)

        # kolejno, następna akcja to transfer części środków gotówkowych na poczet inwestycji w maszynerię
        # wartość konkretnych kwot jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        self.__assets.invest(self.__assumptions.investment_rate_percentage)

        # na ostatnia operacja to uwzględnienie niespodziewanych strat
        # konkretne wartości i to czy w ogóle takie wydarzenie wystąpi kalkulowane jest zgodnie z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        self.__assets.unexpected_loss(self.__assumptions.unexpected_cost_probability_percentage, self.__assumptions.unexpected_costs_number)

        yearly_income, yearly_outcome = self.__assets.get_cash_flow()
        self.__assets.new_year()
        return self.__assets.sum_up(), yearly_income, yearly_outcome

    def _count_revenue(self) -> float:
        # dochód wyliczany jest jako
        # liczba klientów zgodna z założeniami razy średni przychód od klienta razy marża na transakcji;
        # szczegóły dotyczące skąd biorą się wartości w założeniach są dostępne w klasie StageAssumptions
        income = 0
        clients = self.__assumptions.clients_number
        for _ in range(clients):
            income += self.__assumptions.average_income_per_client_number * (self.__assumptions.average_margin_per_client_percentage / 100)
        return income

    def _unpaid(self, promised_revenue: float) -> float:
        # kwota która przypada wyliczana jest na podstawie "obiecanego" zysku pomnożonego przez
        # przyjęty w założeniach procent straty;
        # szczegóły dotyczące skąd biorą się wartości w założeniach są dostępne w klasie StageAssumptions
        return promised_revenue * (self.__assumptions.lost_income_percentage / 100)

    def _tax(self, income):
        # kwota podatku to dochód razy stawka zgodna z przyjętą roczną stawką podatku dla danego roku na danym etapie
        return income * (self.__assumptions.yearly_tax_percentage / 100)







