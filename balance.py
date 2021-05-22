class Assets:
    def __init__(self):
        pass

    def sum_up(self):
        return 0


class Liabilities:
    def __init__(self):
        pass

    def sum_up(self):
        return 0


class Balance:

    class InvalidBalance(Exception):
        """Balance is invalid, assets do not equal liabilities"""

    def __init__(self, assets: Assets, liabilities: Liabilities):
        self.__assets = assets
        self.__liabilities = liabilities

    @property
    def assets(self):
        return self.__assets

    @property
    def liabilities(self):
        return self.__liabilities

    def check(self):
        asu = self.__assets.sum_up()
        lsu = self.__liabilities.sum_up()
        if asu != lsu:
            raise Balance.InvalidBalance(f"Assets = {asu} ; Liabilities = {lsu}")
