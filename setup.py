import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages":["PyQt5.QtWidgets","PyQt5.QtGui","PyQt5.QtCore"],
    # includes=["matplotlib.pyplot"],
    "include_files":['left.png','right.png','stand.png','leftR.png','rightR.png','standR.png']
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="JangTry",
    version="0.1",
    description="Let's raise Temmieeeee!",
    options={"build_exe": build_exe_options},
    executables=[Executable("raiseMe.py", base=base)]
)

