from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python36\\tcl\\tk8.6"

executables = [Executable("Big Red Button.py")]


setup(
    name="Do Not Press the Button",
    options={"build_exe": {"packages":["pygame","random","PIL"],
                           "include_files":["Button.png","doge.jpg"]}},
                            icon="Button.png",
    executables = executables

    )
