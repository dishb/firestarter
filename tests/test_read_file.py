from firestarter._utils._read_file import _read_file

def test_read_file(tmp_path):
    file = tmp_path / "test.txt"
    file_content = """$ comment
$ another comment
[name] :: name
[path] :: /Users/dishb/Documents/"""
    file.write_text(file_content, encoding = "utf-8")
    expected = ["$ comment", "$ another comment", "[name] :: name", "[path] :: /Users/dishb/Documents/"]
    assert _read_file(file) == expected
        
