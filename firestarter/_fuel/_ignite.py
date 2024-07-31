import os
from pathlib import Path
from subprocess import run, PIPE
from platform import system

from colorama import deinit, init

from .._core._files import GITIGNORE, INIT
from .._core._projects import _create_blank, _create_package, _create_game
from .._core._labels import _Labels

def _ignite(fuel: Path) -> int:
    """
    Parses a fuel template (file) and creates a project with firestarter.

    Args:
        file (Path): The file path to the fuel template.

    Returns:
        int: The exit code.
    """

    init(autoreset = True)

    if not str(fuel).endswith(".fuel"):
        print(_Labels.ERROR + f"{fuel} needs to be a fuel template file (ending in .fuel).")
        return 1

    with open(fuel, "r", encoding = "utf-8") as template:
        content = template.read()
        template.close()

    lines = content.split("\n")

    for index, line in enumerate(lines):
        line = line.split(" ")
        line_num = index + 1

        if line[0] in ["", " ", "$"]:
            pass

        elif line[0] == "[name]":
            name = line[2]

        elif line[0] == "[git]":
            if line[2].lower() in ["yes", "y"]:
                git = True
            elif line[2].lower() in ["no", "n"]:
                git = False
            else:
                print(_Labels.ERROR + f"Line {line_num}: Invalid value for [git].")
                print("Please read the documentation to learn more.")
                return 1

        elif line[0] == "[path]":
            path = Path(line[2])

        elif line[0] == "[project-type]":
            if line[2] not in ["blank", "package", "game"]:
                print(_Labels.ERROR + f"Line {line_num}: Invalid value for [project-type].")
                print("Please read the documentation to learn more.")
                return 1

            project = line[2]

        elif line[0] == "[test-framework]":
            if line[2] not in ["pytest", "unittest", "none"]:
                print(_Labels.ERROR + f"Line {line_num}: Invalid value for [test-framework].")
                print("Please read the documentation to learn more.")
                return 1

            test_framework = line[2]

        elif line[0] == "[linter]":
            if line[2] not in ["pylint", "flake8", "black", "bandit", "none", "ruff"]:
                print(_Labels.ERROR + f"Line {line_num}: Invalid value for [linter].")
                print("Please read the documentation to learn more.")
                return 1

            linter = line[2]

        else:
            print(_Labels.ERROR + f"Line {line_num}: Invalid header.")
            print("Please read the documentation to learn more.")
            return 1

    root_dir = Path(path) / name
    if os.path.exists(root_dir):
        print(_Labels.ERROR + f"{root_dir} already exists.")
        return 1

    print(_Labels.INFO + "Creating project directory.")

    os.mkdir(root_dir)
    os.chdir(root_dir)

    if system().lower() in ["darwin", "linux"]:
        python_cmd = "python3"
        pip_cmd = "pip3"
    elif system().lower() == "windows":
        python_cmd = "python"
        pip_cmd = "pip"
    else:
        print(_Labels.ERROR + f"{system()} is not a supported operating system.")
        print("Please read the documentation to learn more.")
        return 1

    print(_Labels.INFO + "Creating virtual environment.")

    venv_path = root_dir / ".venv"
    run([python_cmd, "-m", "venv", venv_path], check = True, stdout = PIPE)

    if git:
        print(_Labels.INFO + "Initializing a git repository.")
        run(["git", "init", root_dir], stdout = PIPE, check = True)

        print(_Labels.INFO + "Creating file: .gitignore")
        with open(root_dir / ".gitignore", "x", encoding = "utf-8") as file:
            file.write(GITIGNORE)
            file.close()

    if project == "blank":
        _create_blank(root_dir)
    elif project == "package":
        _create_package(root_dir, name)
    elif project == "game":
        _create_game(root_dir)

    core_dir = root_dir / "core"
    print(_Labels.INFO + f"Creating directory: {core_dir}")

    os.mkdir(core_dir)
    with open(core_dir / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    utils_dir = root_dir / "utils"
    print(_Labels.INFO + f"Creating directory: {utils_dir}")

    os.mkdir(utils_dir)
    with open(utils_dir / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    print(_Labels.INFO + "Creating file: dev-requirements.txt")

    with open(root_dir / "dev-requirements.txt", "x", encoding = "utf-8") as file:
        if linter != "none":
            file.write(f"{linter}\n")
        if test_framework not in ["unittest", "none"]:
            file.write(test_framework)
        file.close()

    if linter == "pylint":
        print(_Labels.INFO + "Creating file: .pylintrc")
        with open(root_dir / ".pylintrc", "x", encoding = "utf-8") as file:
            file.write("")
            file.close()

    print(_Labels.ACTION + f"Change to the project directory: cd {root_dir}")

    if system().lower() in ["darwin", "linux"]:
        activate_venv = root_dir / ".venv/bin/activate"
        print(_Labels.ACTION + f"Activate the virtual environment: source {activate_venv}")
    else:
        activate_venv = root_dir / ".venv/Scripts/activate"
        print(_Labels.ACTION +
              f"Activate the virtual environment: {activate_venv}"
              )

    def _install_package(package: str) -> None:
        """
        Installs a single package using pip.

        Args:
            package (str): The name of the package to be installed.
        """
        
        venv_python_loc = root_dir / ".venv" / "bin" / python_cmd
        run([venv_python_loc, "-m", "pip", "install", package], check = True, stdout = PIPE, stderr = PIPE)

    def _install_packages(file: Path) -> None:
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
            _install_package(package)

    req_file = root_dir / "requirements.txt"
    dev_req_file = root_dir / "dev-requirements.txt"
    print(_Labels.INFO + "Installing the dependencies:" +
          f"\n{pip_cmd} install {req_file}" +
          f"\n{pip_cmd} install {dev_req_file}"
          )
    _install_packages(dev_req_file)

    if project == "package":
        dist_req_file = root_dir / "dist-requirements.txt"
        print(f"{pip_cmd} install {dist_req_file}")
        _install_packages(dist_req_file)

        print(_Labels.ACTION + f"Install the package in editable mode: {pip_cmd} install -e .")

    print("")
    deinit()
    return 0
