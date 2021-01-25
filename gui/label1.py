from tkinter import *

def copy():
	a = e1.get()
	l1.config(text=a)
	
def reset():
	l1.config(text="")
	
root = Tk()

e1 = Entry(root)
l1 = Label(root,text="default msg")

b1 = Button(root,text="copy",command=copy)
b2 = Button(root,text="reset",command=reset)

e1.pack()
l1.pack()
b1.pack()
b2.pack()

root.mainloop()