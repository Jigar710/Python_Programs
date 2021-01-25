from tkinter import *

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="new")
filemenu.add_command(label="open")
filemenu.add_command(label="save")
filemenu.add_command(label="exit")
menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_command(label="paste")
menubar.add_cascade(menu=editmenu,label="Edit")

root.config(menu=menubar)
root.mainloop()