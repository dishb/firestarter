from sys import exit as sys_exit

from ._core._entry_points import _console
from ._core._labels import _Labels

if __name__ == "__main__":
    try:
        EXIT_CODE = _console()
        sys_exit(EXIT_CODE)
    except KeyboardInterrupt:
        print("\n" + _Labels.INFO + "Application interrupted and quit with Control+C.\n")
        sys_exit(130)
