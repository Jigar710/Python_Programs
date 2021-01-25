from tkinter import *

root = Tk()

lbox1 = Listbox(root)
lbox2 = Listbox(root,selectmode=SINGLE)

lbox1.insert(END,"first")
lbox1.insert(END,"second","third")
lbox1.insert(END,*("fourth","fifth"))

lbox2.insert(END,"first")
lbox2.insert(END,"second","third")
lbox2.insert(END,*("fourth","fifth"))

lbox1.pack(side=LEFT)
lbox2.pack(side=RIGHT)
root.mainloop()