import cx_Freeze

executables = [cx_Freeze.Executable("pygameVideo15.py")]
cx_Freeze.setup(
name = "A bit Racey",
options = {"build_exe": {"package": ["pygame"],
                        "include_files": ["racecar.png"]}},
executables = executables
)