def _check_dupes(lines: list[str]) -> bool:
    """
    Checks if a given list, representing the lines of a file, have duplicates.

    Args:
        lines (list[str]): A list to represent all the lines of a file, where each line is a
        string.

    Returns:
        bool: Whether or not the list contains duplicate values.
    """

    seen = set()

    for line in lines:
        if line != "" and line[0] != "$":
            if line in seen:
                return True
            else:
                seen.add(line)

    return False
