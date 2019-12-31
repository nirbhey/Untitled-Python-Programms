from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Nirbhey Singh Pahwa\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['Tk_LIBRARY'] = "C:\\Users\\Nirbhey Singh Pahwa\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6"

setup(name = 'App1', version = '0.1', description = 'Simple App', executables = [Executable("test.py")]) # Name will be the final name on the exe and description = [Executable("fileYouWantToMakeExe.py"]

