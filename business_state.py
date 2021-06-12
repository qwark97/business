import random

from business.assumptions import StageAssumptions
from business.balance import Assets
from business.state import State


class Model:
    def __init__(self, assets: Assets, assumptions: StageAssumptions, state: State):
        self.__stage = 1
        self.__year = 0
        self.__assumptions = assumptions
        self.__assets = assets
        self.__state = state

    def next_stage(self, assumptions: StageAssumptions):
        self.__stage += 1
        self.__assumptions = assumptions

    def next_year(self):
        self.__year += 1
        self.__state.set_year(self.__year)
        self.__state.set_stage(self.__stage)
        # na początku nowego roku zapisywane są dotychczasowe zasoby gotówkowe aby móc wyliczyć
        # zyski w danym roku
        money_at_the_beginning = self.__assets.money
        self.__state.set_wealth_at_the_beginning_of_the_year(self.__assets.sum_up())
        self.__state.set_money_at_the_beginning_of_the_year(money_at_the_beginning)
        self.__state.set_machinery_at_the_beginning_of_the_year(self.__assets.machinery)

        # w tym miejscu następuje wyliczenie dochodów (na tym etapie przychód - koszty);
        # szczegóły w jaki sposób wyliczany jest dochód znajdują się w ramach użytej metody
        promised_revenue = self._count_revenue()
        self.__assets.add_earnings(promised_revenue)

        # następnie od uzyskanego przychodu odejmowana jest kwota należności, które
        # z jakichś losowych powodów nie zostały opłacone;
        # szczegóły dotyczące tego jaka kwota i czy w ogóle przepada znajdują się w ramach użytej metody
        unpaid_loss = self._unpaid(promised_revenue)
        self.__state.set_unpaid_loss_in_the_year(unpaid_loss)
        self.__assets.unpaid_income(unpaid_loss)

        # kolejno, od uzyskanych dochodów odejmowane są koszty stałe z danego roku;
        # wartość kosztów stałych jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        fixed_costs = self.__assumptions.fixed_costs_number
        self.__state.set_fixed_costs_in_the_year(fixed_costs)
        self.__assets.subtract_fixed_costs(fixed_costs)

        # na koniec, od zysku uzyskanego w rozważanym roku odejmowany jest podatek
        # wartość podatku wyliczana jest zgodnie z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        tax = self._tax(max(self.__assets.money - money_at_the_beginning, 0))
        self.__state.set_tax_in_the_year(tax)
        self.__assets.subtract_tax(tax)

        # na tym etapie pomniejszana jest wartość maszyn posiadanych w przedsiębiorstwie
        # ze względu na naturalne zużycie
        # wartość konkretnych kwot jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        natural_machinery_loss = self._natural_machinery_loss(self.__assets.machinery)
        self.__state.set_natural_machinery_loss_in_the_year(natural_machinery_loss)
        self.__assets.natural_machinery_loss(natural_machinery_loss)

        # kolejno, następna akcja to transfer części środków gotówkowych na poczet inwestycji w maszynerię
        # wartość konkretnych kwot jest zgodna z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        investments = self._investmets(self.__assets.money)
        self.__state.set_investments_in_the_year(investments)
        self.__assets.invest(investments)

        # na ostatnia operacja to uwzględnienie niespodziewanych strat
        # konkretne wartości i to czy w ogóle takie wydarzenie wystąpi kalkulowane jest zgodnie z przyjętymi założeniami (szczegóły w klasie StageAssumptions)
        unexpected_loss = self._unexpected_loss()
        self.__state.set_unexpected_loss_in_the_year(unexpected_loss)
        self.__assets.unexpected_loss(unexpected_loss)

        yearly_income, yearly_outcome = self.__assets.get_cash_flow()
        self.__state.set_money_income_in_the_year(yearly_income)
        self.__state.set_money_outcome_in_the_year(yearly_outcome)
        self.__assets.new_year()

        wealth = self.__assets.sum_up()
        self.__state.set_wealth_at_the_end_of_the_year(wealth)
        self.__state.set_money_at_the_end_of_the_year(self.__assets.money)
        self.__state.set_machinery_at_the_end_of_the_year(self.__assets.machinery)
        return wealth, yearly_income, yearly_outcome

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

    def _natural_machinery_loss(self, current_machinery: float):
        # wyliczenie naturalnej straty polega na pomniejszeniu wartości wyposażenia
        # o wskazaną wartość procentową
        loss = current_machinery * (self.__assumptions.natural_loss_percentage / 100)
        return loss

    def _investmets(self, current_money):
        # wykonanie akcji inwestowania polega na "transferze" danego procentu
        # gotówki na poczet kwoty opisującej wyposażenie - przy spełnieniu warunku, że
        # stan gotówki musi być większy od 0
        percentage_of_money = max(self.__assumptions.investment_rate_percentage, 0)
        investment = 0
        if current_money > 0:
            investment = current_money * percentage_of_money / 100
        return investment

    def _unexpected_loss(self):
        # akcja niespodziewanej straty składa się z dwóch kroków:
        # w pierwszej kolejności, na podstawie prawdopodobieństwa okreslane jest czy
        # niespodziewana strata w ogóle wystąpi.
        # jeśli pierwszy krok wskazał że strata wystąpi wtedy następuje pomniejszenie majątku o wskazaną kwotę
        probability = self.__assumptions.unexpected_cost_probability_percentage
        will_happen = random.choice([False for _ in range(100 - int(probability))] + [True for _ in range(int(probability))])
        if will_happen:
            return self.__assumptions.unexpected_costs_number
        else:
            return 0
