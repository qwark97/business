from business.assumptions import StageAssumptions
from business.balance import Assets
from business.business_state import Model


def run():
    first_stage_assumptions = StageAssumptions(
        lost_income_percentage=(5, 2),
        natural_loss_percentage=(7, 3),
        clients_number=(15, 2),
        average_income_per_client_number=(4000, 1000),
        average_margin_per_client_percentage=(20, 5),
        yearly_tax_percentage=20,
        unexpected_cost_probability_percentage=(3, 10),
        unexpected_costs_number=(1000, 3000),
        fixed_costs_number=(15000, 1000),
        investment_rate_percentage=(5, 1),
    )
    second_stage_assumptions = StageAssumptions(
        lost_income_percentage=(6, 2),
        natural_loss_percentage=(6, 2),
        clients_number=(20, 3),
        average_income_per_client_number=(4300, 700),
        average_margin_per_client_percentage=(20, 6),
        yearly_tax_percentage=29,
        unexpected_cost_probability_percentage=(3, 5),
        unexpected_costs_number=(1500, 2000),
        fixed_costs_number=(17000, 1000),
        investment_rate_percentage=(10, 1),
    )
    third_stage_assumptions = StageAssumptions(
        lost_income_percentage=(7, 1),
        natural_loss_percentage=(5, 2),
        clients_number=(25, 4),
        average_income_per_client_number=(5200, 500),
        average_margin_per_client_percentage=(20, 4),
        yearly_tax_percentage=35,
        unexpected_cost_probability_percentage=(1, 1),
        unexpected_costs_number=(10000, 1000),
        fixed_costs_number=(20000, 1000),
        investment_rate_percentage=(10, 2),
    )
    initial_assets = Assets(money=35000, machinery=15000)
    m = Model(initial_assets, first_stage_assumptions)
    print("stage:", 1)
    for i in range(3):
        print("\t", i+1, m.next_year())
    glob_i = i+1
    m.next_stage(second_stage_assumptions)
    print("stage:", 2)
    for i in range(5):
        print("\t", glob_i+i+1, m.next_year())
    glob_i += i+1
    m.next_stage(third_stage_assumptions)
    print("stage:", 3)
    for i in range(7):
        print("\t", glob_i+i+1, m.next_year())


if __name__ == '__main__':
    run()
