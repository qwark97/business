from business.assumptions import StageAssumptions
from business.balance import Balance, Assets, Liabilities
from business.business_state import Model


def run():
    first_stage_assumptions = StageAssumptions(
        # TODO
    )
    second_stage_assumptions = StageAssumptions(
        # TODO
    )
    third_stage_assumptions = StageAssumptions(
        # TODO
    )
    initial_assets = Assets(
        # TODO
    )
    initial_liabilities = Liabilities(
        # TODO
    )
    initial_balance = Balance(initial_assets, initial_liabilities)
    initial_balance.check()
    m = Model(initial_balance, first_stage_assumptions)
    for _ in range(3):
        m.next_year()

    m.next_stage(second_stage_assumptions)
    for _ in range(5):
        m.next_year()

    m.next_stage(third_stage_assumptions)
    for _ in range(7):
        m.next_year()


if __name__ == '__main__':
    run()
