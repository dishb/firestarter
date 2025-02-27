import os
from pathlib import Path
from subprocess import run, PIPE
from platform import system

from colorama import deinit, init

from .._core._files import GITIGNORE, INIT, BUILD_SCRIPT
from .._core._projects import _create_blank, _create_package, _create_game
from .._utils._check_dupes import _check_dupes
from .._utils._read_file import _read_file
from .._utils._log import _Logger
from .._utils._install_packages import _install_packages

def _ignite(fuel: Path, logger: _Logger) -> int:
    """
    Parses a fuel template (file) and creates a project with `firestarter`.

    Args:
        file (Path): The file path to the fuel template.
        logger (_Logger): A logger customized with a verbosity level.

    Returns:
        int: The exit code.
    """

    init(autoreset = True)

    if not str(fuel).endswith(".fuel"):
        logger._error(f"{fuel} needs to be a fuel template file that ends in .fuel.")
        return 1
    
    lines = _read_file(fuel)

    if _check_dupes(lines):
        logger._error("Duplicate options found in fuel template file.")
        return 1

    for index, line in enumerate(lines):
        line_num = index + 1
        line = line.split(" ")
        
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
                logger._error(f"Line {line_num}: Invalid value for [git].")
                return 1

        elif line[0] == "[path]":
            path = Path(line[2])

        elif line[0] == "[project-type]":
            if line[2] not in ["blank", "package", "game"]:
                logger._error(f"Line {line_num}: Invalid value for [project-type].")
                return 1

            project = line[2]

        elif line[0] == "[test-framework]":
            if line[2] not in ["pytest", "unittest", "none"]:
                logger._error(f"Line {line_num}: Invalid value for [test-framework].")
                return 1

            test_framework = line[2]

        elif line[0] == "[linter]":
            if line[2] not in ["pylint", "flake8", "black", "bandit", "none", "ruff"]:
                logger._error(f"Line {line_num}: Invalid value for [linter].")
                return 1

            linter = line[2]

        else:
            logger._error(f"Line {line_num}: Invalid header.")
            return 1

    root_dir = Path(path) / name
    if os.path.exists(root_dir):
        logger._error(f"{root_dir} already exists.")
        return 1

    logger._info("Creating project directory.")

    os.mkdir(root_dir)
    os.chdir(root_dir)

    if system().lower() in ["darwin", "linux"]:
        python_cmd = "python3"
        pip_cmd = "pip3"
    elif system().lower() == "windows":
        python_cmd = "python"
        pip_cmd = "pip"
    else:
        logger._error(f"{system()} is not a supported operating system.")
        return 1

    logger._info("Creating virtual environment.")

    venv_path = root_dir / ".venv"
    run([python_cmd, "-m", "venv", venv_path], check = True, stdout = PIPE)

    if git:
        logger._info("Initializing a git repository.")
        run(["git", "init", root_dir], stdout = PIPE, check = True)

        logger._info("Creating file: .gitignore")
        with open(root_dir / ".gitignore", "x", encoding = "utf-8") as file:
            file.write(GITIGNORE)
            file.close()

    if project == "blank":
        _create_blank(root_dir, logger)
    elif project == "package":
        _create_package(root_dir, name, logger)
    elif project == "game":
        _create_game(root_dir, logger)

    core_dir = root_dir / "core"
    logger._info(f"Creating directory: {core_dir}")

    os.mkdir(core_dir)
    with open(core_dir / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    utils_dir = root_dir / "utils"
    logger._info(f"Creating directory: {utils_dir}")

    os.mkdir(utils_dir)
    with open(utils_dir / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    logger._info("Creating file: dev-requirements.txt")

    with open(root_dir / "dev-requirements.txt", "x", encoding = "utf-8") as file:
        if linter != "none":
            file.write(f"{linter}\n")
        if project != "package":
            file.write("pyinstaller\n")
        if test_framework not in ["unittest", "none"]:
            file.write(test_framework)
        file.close()
    
    if project != "package":
        logger._info("Creating build script: build.py")
        with open(utils_dir / "build.py", "x", encoding = "utf-8") as file:
            file.write(BUILD_SCRIPT)
            file.close

    if linter == "pylint":
        logger._info("Creating file: .pylintrc")
        with open(root_dir / ".pylintrc", "x", encoding = "utf-8") as file:
            file.write("")
            file.close()

    logger._action(f"Change to the project directory: cd {root_dir}")

    if system().lower() in ["darwin", "linux"]:
        activate_venv = root_dir / ".venv/bin/activate"
        logger._action(f"Activate the virtual environment: source {activate_venv}")
    else:
        activate_venv = root_dir / ".venv/Scripts/activate"
        logger._action(f"Activate the virtual environment: {activate_venv}")

    req_file = root_dir / "requirements.txt"
    dev_req_file = root_dir / "dev-requirements.txt"
    logger._info(f"\n{pip_cmd} install {req_file}" +
          f"\n{pip_cmd} install {dev_req_file}"
          )
    _install_packages(dev_req_file, root_dir, python_cmd)
    if project == "game":
        _install_packages(req_file, root_dir, python_cmd)

    if project == "package":
        dist_req_file = root_dir / "dist-requirements.txt"
        print(f"{pip_cmd} install {dist_req_file}")
        _install_packages(dist_req_file, root_dir, python_cmd)

        logger._action(f"Install the package in editable mode: {pip_cmd} install -e .")

    print("")
    deinit()
    return 0
