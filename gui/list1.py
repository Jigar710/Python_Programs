from tkinter import *

root = Tk()

lbox = Listbox(root)
#help(lbox)

lbox.insert(END,"first")
lbox.insert(END,"second","third")
lbox.insert(END,*("fourth","fifth"))

lbox.pack()
root.mainloop()