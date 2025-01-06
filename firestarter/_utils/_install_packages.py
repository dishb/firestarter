from subprocess import run, PIPE
from pathlib import Path

def _install_package(package: str, root_dir: Path, python_cmd: str) -> None:
    """
    Installs a single package using pip.

    Args:
        package (str): The name of the package to be installed.
        root_dir (Path): The path to the project's root directory.
        python_cmd (str): The command used to execute Python in the shell. Varies if the user is on
        a UNIX-based versus Windows system.
    """
    
    venv_python_loc = root_dir / ".venv" / "bin" / python_cmd
    run([venv_python_loc, "-m", "pip", "install", package], check = True, stdout = PIPE, stderr = PIPE)

def _install_packages(file: Path, root_dir: Path, python_cmd: str) -> None:
    """
    Installs a multiple packages using pip.

    Args:
        package (str): The name of the package to be installed.
        root_dir (Path): The path to the project's root directory.
        python_cmd (str): The command used to execute Python in the shell. Varies if the user is on
        a UNIX-based versus Windows system.
    """
        
    with open(file, "r", encoding = "utf-8") as req_file:
        packages = req_file.read()
        req_file.close()

    packages = packages.split("\n")
    for package in packages:
        _install_package(package, root_dir, python_cmd)