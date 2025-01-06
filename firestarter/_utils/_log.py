from .._core._labels import _Labels

class _Logger():
    """
    A class for convenient logging / printing. Not meant for programming use.
    """
    
    def __init__(self, log_level: str | None = "all"):
        
        self._log_level = log_level
    
    def _error(self, msg: str) -> None:
        """
        A function to print out a message with an error label as a prefix.

        Args:
            msg (str): Message to be printed to the console.
        """
        
        if self._log_level.lower() in ["error", "all"]:
            print(_Labels.ERROR + msg + "\nPlease read the documentation to learn more.")
        
    def _info(self, msg: str) -> None:
        """
        A function to print out a message with a info label as a prefix.

        Args:
            msg (str): Message to be printed to the console.
        """
        
        if self._log_level.lower() in ["info", "all"]:
            print(_Labels.INFO + msg)

    def _action(self, msg: str) -> None:
        """
        A function to print out a message with an action label as a prefix.

        Args:
            msg (str): Message to be printed to the console.
        """
        
        if self._log_level.lower() in ["action", "all"]:
            print(_Labels.ACTION + msg)
