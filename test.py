import tkinter
from tkinter.filedialog import askdirectory

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

folder_path = askdirectory()