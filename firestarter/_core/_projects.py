from pathlib import Path
from os import mkdir

from ._files import BLANK_MAIN, DIST_REQS, INIT, SETUP_PY, GAME_MAIN
from .._utils._log import _info

def _create_package(root_dir: Path, name: str) -> None:
    """
    Creates a Python package. Not meant for programming use.

    Args:
        root_dir (Path): The root or base directory for the project.
        name (str): The name of the project.
    """

    _info(f"Creating directory: {root_dir / name}")

    mkdir(root_dir / name)

    _info("Creating file: requirements.txt")

    with open(root_dir / "requirements.txt", "x", encoding = "utf-8") as file:
        file.write("")
        file.close()

    _info("Creating file: dist-requirements.txt")

    with open(root_dir / "dist-requirements.txt", "x", encoding = "utf-8") as file:
        file.write(DIST_REQS)
        file.close()

    _info("Creating directory: tests")

    mkdir(root_dir / "tests")
    with open(root_dir / "tests" / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    _info("Creating file: setup.py")

    with open(root_dir / "setup.py", "x", encoding = "utf-8") as file:
        file.write(SETUP_PY)
        file.close()

def _create_blank(root_dir: Path) -> None:
    """
    Creates a blank project. Not meant for programming use.

    Args:
        root_dir (Path): The root or base directory for the project.
    """

    _info("Creating file: main.py")

    with open(root_dir / "main.py", "x", encoding = "utf-8") as file:
        file.write(BLANK_MAIN)
        file.close()

    _info("Creating file: requirements.txt")

    with open(root_dir / "requirements.txt", "x", encoding = "utf-8") as file:
        file.write("")
        file.close()

def _create_game(root_dir: Path) -> None:
    """
    Creates a Python game. Not meant for programming use.

    Args:
        root_dir (Path): The root or base directory for the project.
    """
    
    _info("Creating file: main.py")
    
    with open(root_dir / "main.py", "x", encoding = "utf-8") as file:
        file.write(GAME_MAIN)
        file.close()
    
    _info("Creating file: requirements.txt")
    
    with open(root_dir / "requirements.txt", "x", encoding = "utf-8") as file:
        file.write("pygame-ce")
        file.close()
