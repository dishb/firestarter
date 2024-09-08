def _check_dupes(lines: list) -> bool:
    seen = set()
    dupes = []

    for line in lines:
        if line != "":
            if line[0] in seen:
                dupes.append(line[0])
            else:
                seen.add(line[0])

    return len(dupes) == 0
