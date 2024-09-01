import PyInstaller.__main__

PyInstaller.__main__.run(["main.py",
                          "-F",
                          "-n Main",
                          "-w",
                          "--disable-windowed-traceback"
                          ])
