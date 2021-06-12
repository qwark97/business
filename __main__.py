import sys

from business.negative import run_negative
from business.neutral import run_neutral
from business.positive import run_positive

if __name__ == '__main__':
    arg = 0
    try:
        arg = int(sys.argv[1])
    except Exception:
        print('pass version 1, 2 or 3')
        exit(1)
    if arg == 1:
        run_neutral()
    elif arg == 2:
        run_positive()
    elif arg == 3:
        run_negative()
    else:
        print('invalid arg')
        exit(1)
