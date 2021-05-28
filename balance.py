import random


class Assets:
    def __init__(self, money: float, machinery: float):
        self.money = money
        self.machinery = machinery

    def sum_up(self):
        return self.money + self.machinery

    def add_earnings(self, amount: float):
        self.money += amount

    def invest(self, amount):
        if amount > self.money:
            raise Exception(f"Not enough money: {self.money} < {amount}")
        self.money -= amount
        self.machinery += amount

    def natural_machinery_loss(self, percentage: float):
        value_percentage_left = 100 - percentage
        self.machinery *= value_percentage_left / 100

    def unexpected_loss(self, probability: float, cost: float):
        will_happen = random.choice([False for _ in range(100-int(probability))] + [True for _ in range(int(probability))])
        if will_happen:
            self.money -= cost

