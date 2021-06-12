import matplotlib.pyplot as plt
import numpy as np


def print_header():
    print("Legenda:")
    print("E   - Etap")
    print("R   - Rok")
    print("MPR - Majątek na początku roku")
    print("MKR - Majątek na koniec roku")
    print("GPR - Gotówka na początku roku")
    print("GKR - Gotówka na koniec roku")
    print("UPR - Urządzenia na początek roku")
    print("UKR - Urządzenia na koniec roku")
    print("PR  - Przychody w roku")
    print("WR  - Wydatki w roku")
    print("NPR - Należności przepadłe w roku")
    print("KSR - Koszty stałe w roku")
    print("OR  - Opodatkowanie w roku")
    print("ZMR - Zużycie maszyn w roku")
    print("IMR - Inwestycje w maszyny w roku")
    print("NSR - Niespodziewana strata roku")
    print()
    print("%1s   %2s   %10s   %10s   %10s   %10s   %10s   %10s   %10s    %10s    %10s   %10s    %10s   %10s   %10s    %10s  " % (
    "E", "R", "MPR", "MKR", "GPR", "GKR", "UPR", "UKR", "PR", "WR", "NPR", "KSR", "OR", "ZMR", "IMR", "NSR"))
    print("*"*194)


def print_row(row):
    E, R, MPR, MKR, GPR, GKR, UPR, UKR, PR, WR, NPR, KSR, OR, ZMR, IMR, NSR = list([round(float(x), 2) for x in row.values()])
    print("%1s | %2s | %10s | %10s | %10s | %10s | %10s | %10s | %10s  | %10s  | %10s | %10s  | %10s | %10s | %10s |  %10s |" % (int(E), int(R), MPR, MKR, GPR, GKR, UPR, UKR, PR, WR, NPR, KSR, OR, ZMR, IMR, NSR))


def create_plot(data, plot_file_name):
    year = []
    wealth_at_the_beginning_of_the_year = []
    money_income_in_the_year = []
    money_outcome_in_the_year = []

    for row in data:
        year.append(row['year'])
        wealth_at_the_beginning_of_the_year.append(row['wealth_at_the_beginning_of_the_year'])
        money_income_in_the_year.append(row['money_income_in_the_year'])
        money_outcome_in_the_year.append(row['money_outcome_in_the_year'])

    year = np.array(year)
    wealth_at_the_beginning_of_the_year = np.array(wealth_at_the_beginning_of_the_year)
    money_income_in_the_year = np.array(money_income_in_the_year)
    money_outcome_in_the_year = np.array(money_outcome_in_the_year)

    plt.figure(figsize=(19.2, 10.8))
    plt.xlabel('Rok prowadzenia działalności')
    plt.title('Wykres przedstawiający stan majątku, przypływy oraz wydatki w poszczególnych latach')
    plt.plot(year, wealth_at_the_beginning_of_the_year, label="Majątek", color='black')
    plt.plot(year, money_income_in_the_year, label="Wpływy", color='blue')
    plt.plot(year, money_outcome_in_the_year, label="Wydatki", color='red')
    plt.axvline(4, 0, 1, label='Etap 2', color='purple', linestyle='dotted')
    plt.axvline(9, 0, 1, label='Etap 3', color='orange', linestyle='dotted')
    plt.xticks(year)

    plt.legend()
    plt.savefig(f"{plot_file_name}.png")
