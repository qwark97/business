import random


class Assets:
    def __init__(self, money: float, machinery: float):
        self.money = money
        self.machinery = machinery
        self._yearly_income = 0
        self._yearly_outcome = 0

    def sum_up(self):
        return self.money + self.machinery

    def add_earnings(self, amount: float):
        self.money += self._income(amount)

    def invest(self, percentage_of_money: float):
        # wykonanie akcji inwestowania polega na "transferze" danego procentu
        # gotówki na poczet kwoty opisującej wyposażenie - przy spełnieniu warunku, że
        # stan gotówki musi być większy od 0
        percentage_of_money = max(percentage_of_money, 0)
        if self.money > 0:
            investment = self.money * percentage_of_money / 100
            self.money -= self._outcome(investment)
            self.machinery += investment

    def unpaid_income(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_fixed_costs(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_tax(self, amount: float):
        self.money -= self._outcome(amount)

    def natural_machinery_loss(self, percentage: float):
        # wyliczenie naturalnej straty polega na pomniejszeniu wartości wyposażenia
        # o wskazaną wartość procentową
        loss = self.machinery * (percentage / 100)
        self.machinery -= self._outcome(loss)

    def unexpected_loss(self, probability: float, cost: float):
        # akcja niespodziewanej straty składa się z dwóch kroków:
        # w pierwszej kolejności, na podstawie przekazanego prawdopodobieństwa okreslane jest czy
        # niespodziewana strata w ogóle wystąpi.
        # jeśli pierwszy krok wskazał że strata wystąpi wtedy następuje pomniejszenie majątku o wskazaną kwotę
        will_happen = random.choice([False for _ in range(100-int(probability))] + [True for _ in range(int(probability))])
        if will_happen:
            self.money -= self._outcome(cost)

    def _outcome(self, amount: float) -> float:
        self._yearly_outcome += amount
        return amount

    def _income(self, amount: float):
        self._yearly_income += amount
        return amount

    def get_cash_flow(self) -> (float, float):
        return self._yearly_income, self._yearly_outcome

    def new_year(self):
        self._yearly_income = 0
        self._yearly_outcome = 0
