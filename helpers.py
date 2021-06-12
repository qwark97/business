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
