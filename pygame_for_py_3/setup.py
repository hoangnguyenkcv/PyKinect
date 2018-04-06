import os
os.environ['TCL_LIBRARY'] = "C:\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python\\Python36-32\\tcl\\tk8.6"

import cx_Freeze
executables = [cx_Freeze.Executable('pygameVideo15.py')]
cx_Freeze.setup(
    name = "A bit Racey",
    version = "1.1",
    options = {"build_exe": {"packages": ["pygame"],
                            "include_files": ["mycar.png", "crash.wav", "Jazz.wav"]}},
    executables = executables
    )


