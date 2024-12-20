def _check_dupes(lines: list[str]) -> bool:
    seen = set()

    for line in lines:
        if line != "" and line[0] != "$":
            if line in seen:
                return True
            else:
                seen.add(line)

    return False
