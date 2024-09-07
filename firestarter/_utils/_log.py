from .._core._labels import _Labels

def _error(msg: str) -> None:
    print(_Labels.ERROR + msg)
    
def _info(msg: str) -> None:
    print(_Labels.INFO + msg)

def _action(msg: str) -> None:
    print(_Labels.ACTION + msg)

def _init(msg: str) -> None:
    print(_Labels.INIT + msg)
