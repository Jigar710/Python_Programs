from tkinter import *

root = Tk()

lbox1 = Listbox(root,selectmode=EXTENDED)

lbox1.insert(END,"first")
lbox1.insert(END,"second","third")
lbox1.insert(END,*("fourth","fifth"))

lbox1.pack()

root.mainloop()