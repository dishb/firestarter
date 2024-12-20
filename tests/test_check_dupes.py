from firestarter._utils._check_dupes import _check_dupes

def test_dupe_comments() -> None:
    test_list = ["$ comment", "$ comment", "[name] :: name", "[path] :: /Users/dishb/Documents/"]
    assert _check_dupes(test_list) is False

def test_dupe_lines() -> None:
    test_list = ["$ comment", "[name] :: name", "[name] :: name", "[path] :: /Users/dishb/Documents/"]
    assert _check_dupes(test_list) is True

def test_no_dupes() -> None:
    test_list = ["$ comment", "[name] :: name", "[path] :: /Users/dishb/Documents/"]
    assert _check_dupes(test_list) is False

def test_empty_lines() -> None:
    test_list = ["", "", "[name] :: name", "[path] :: /Users/dishb/Documents/"]
    assert _check_dupes(test_list) is False
