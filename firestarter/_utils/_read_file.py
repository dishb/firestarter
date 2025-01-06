from pathlib import Path

def _read_file(file: Path) -> list[str]:
    """
    Reads a file and returns a list of all the lines.

    Args:
        file (Path): The file to be read.

    Returns:
        list[str]: A list of all the lins in the file.
    """
    
    with open(file, "r", encoding = "utf-8") as file:
        content = file.read()
        file.close()
    
    lines = content.split("\n")

    for line in lines:
        line = line.split(" ")
        
    return lines
