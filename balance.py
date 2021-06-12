from business.state import State


class Assets:
    def __init__(self, money: float, machinery: float, state: State):
        self.money = money
        self.machinery = machinery
        self._yearly_income = 0
        self._yearly_outcome = 0
        self.__state = state

    def sum_up(self):
        return self.money + self.machinery

    def add_earnings(self, amount: float):
        self.money += self._income(amount)

    def invest(self, investment: float):
        self.money -= investment
        self.machinery += investment

    def unpaid_income(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_fixed_costs(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_tax(self, amount: float):
        self.money -= self._outcome(amount)

    def natural_machinery_loss(self, loss: float):
        self.machinery -= self._outcome(loss)

    def unexpected_loss(self, cost: float):
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
