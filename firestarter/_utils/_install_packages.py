from subprocess import run, PIPE
from pathlib import Path

def _install_package(package: str, root_dir: Path, python_cmd: str) -> None:
    """
    Installs a single package using pip.

    Args:
        package (str): The name of the package to be installed.
    """
    
    venv_python_loc = root_dir / ".venv" / "bin" / python_cmd
    run([venv_python_loc, "-m", "pip", "install", package], check = True, stdout = PIPE, stderr = PIPE)

def _install_packages(file: Path, root_dir: Path, python_cmd: str) -> None:
    """
    Installs multiple packages from a requirements.txt file using pip.

    Args:
        file (Path): Path to the requirements.txt file.
    """
        
    with open(file, "r", encoding = "utf-8") as req_file:
        packages = req_file.read()
        req_file.close()

    packages = packages.split("\n")
    for package in packages:
        _install_package(package, root_dir, python_cmd)