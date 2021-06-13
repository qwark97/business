import pandas as pd

from business.assumptions import StageAssumptions
from business.balance import Assets
from business.business_state import Model
from business.helpers import print_header, print_row, create_plot
from business.state import State, DATABASE


def run_neutral():
    first_stage_assumptions = StageAssumptions(
        clients_number=(6, 1),
        average_income_per_client_number=(10000, 1000),
        average_margin_per_client_percentage=(10, 5),
        lost_income_percentage=(5, 2),
        natural_loss_percentage=(7, 3),
        yearly_tax_percentage=20,
        unexpected_cost_probability_percentage=(10, 10),
        unexpected_costs_number=(1000, 3000),
        fixed_costs_number=(15000, 1000),
        investment_rate_percentage=(5, 1),
    )
    second_stage_assumptions = StageAssumptions(
        clients_number=(15, 2),
        average_income_per_client_number=(15000, 2000),
        average_margin_per_client_percentage=(15, 5),
        lost_income_percentage=(6, 1),
        natural_loss_percentage=(8, 2),
        yearly_tax_percentage=30,
        unexpected_cost_probability_percentage=(10, 10),
        unexpected_costs_number=(1000, 3000),
        fixed_costs_number=(15000, 1000),
        investment_rate_percentage=(10, 3),
    )
    third_stage_assumptions = StageAssumptions(
        clients_number=(20, 2),
        average_income_per_client_number=(15000, 1000),
        average_margin_per_client_percentage=(20, 5),
        lost_income_percentage=(5, 1),
        natural_loss_percentage=(9, 1),
        yearly_tax_percentage=40,
        unexpected_cost_probability_percentage=(10, 10),
        unexpected_costs_number=(1000, 3000),
        fixed_costs_number=(20000, 1000),
        investment_rate_percentage=(7, 2),
    )
    state = State()
    initial_assets = Assets(money=20000, machinery=15000, state=state)
    m = Model(initial_assets, first_stage_assumptions, state=state)
    for i in range(3):
        m.next_year()
        state.save()
    m.next_stage(second_stage_assumptions)
    for i in range(5):
        m.next_year()
        state.save()
    m.next_stage(third_stage_assumptions)
    for i in range(7):
        m.next_year()
        state.save()

    res = []
    print_header()
    for row in DATABASE:
        print_row(row)
        sub_res = {}
        for k, v in row.items():
            sub_res[k] = round(v, 2)
        res.append(sub_res)
    create_plot(DATABASE, "neutral")
    pd.DataFrame(res).to_csv("neutral.csv")
