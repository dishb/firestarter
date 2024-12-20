from pathlib import Path

def _read_file(file: Path) -> list[str]:
    with open(file, "r", encoding = "utf-8") as file:
        content = file.read()
        file.close()
    
    lines = content.split("\n")

    for line in lines:
        line = line.split(" ")
        
    return lines
