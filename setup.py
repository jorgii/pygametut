import os
import cx_Freeze


# Set the path to tcl and tkl library
os.environ["TCL_LIBRARY"] = os.path.normpath("C:/Python34/tcl/tcl8.6")
os.environ["TK_LIBRARY"] = os.path.normpath("C:/Python34/tcl/tk8.6")

executables = [cx_Freeze.Executable("pygametut.py")]

cx_Freeze.setup(
    name="Slither",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["apple.png", "snake_head.png"]}},
    description="Slither Game",
    executables=executables)
