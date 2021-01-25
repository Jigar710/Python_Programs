from tkinter import *

for i in dir(Tk):
	if '_' not in i:
		print(i)
	
help(Tk.maxsize)