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

    def invest(self, amount):
        if amount > self.money:
            raise Exception(f"Not enough money: {self.money} < {amount}")
        self.money -= amount
        self.machinery += amount

    def unpaid_income(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_fixed_costs(self, amount: float):
        self.money -= self._outcome(amount)

    def subtract_tax(self, amount: float):
        self.money -= self._outcome(amount)

    def natural_machinery_loss(self, percentage: float):
        value_percentage_left = 100 - percentage
        left = self.machinery * (value_percentage_left / 100)
        loss = self.machinery - left
        self._outcome(loss)
        self.machinery = left

    def unexpected_loss(self, probability: float, cost: float):
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
