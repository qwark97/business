class Assets:
    def __init__(self, money: float):
        self.money = money
        self.receivables = 0

    def sum_up(self):
        return self.money + self.receivables
