from colorama import Fore, Style

class _Labels():
    """
    A class for all the labels firestarter uses. Not meant for programming use.
    """

    ACTION = "\n[" + Fore.GREEN + "action" + Style.RESET_ALL +  "] "
    INFO = "\n[" + Fore.BLUE + "info" + Style.RESET_ALL +  "] "
    INIT = "\n[" + Fore.YELLOW + "init" + Style.RESET_ALL +  "] "
    ERROR = "\n[" + Fore.RED + "error" + Style.RESET_ALL + "] "
