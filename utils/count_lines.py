import os

def count_lines_in_file(file_path: str) -> int:
    try:
        with open(file_path, "r", encoding = "utf-8") as file:
            return sum(1 for line in file if line.strip())
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

def count_lines_in_python_files(root_dir: str) -> tuple[int, list[tuple[str, int]]]:
    total_lines = 0
    python_files = []

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                if "__pycache__" not in file_path and "venv" not in file_path:
                    lines = count_lines_in_file(file_path)
                    total_lines += lines
                    python_files.append((file_path, lines))

    return total_lines, python_files

def main() -> None:
    root_dir = "../firestarter/"
    total_lines, python_files = count_lines_in_python_files(root_dir)

    print(f"Total lines in all .py files: {total_lines}\n")
    print("Lines in each .py file:")
    for file_path, lines in python_files:
        print(f"{file_path}: {lines} lines")

if __name__ == "__main__":
    main()
