from tkinter import *

def apply():
	print(var.get())
	
def reset():
	#var.set(0) # unchecked all
	var.set(1)

root = Tk()

var = IntVar()

var.set(1)

c1 = Radiobutton(root,text="red",variable=var,value=1)
c2 = Radiobutton(root,text="green",variable=var,value=2)
c3 = Radiobutton(root,text="blue",variable=var,value=3)

b1 = Button(root,text="apply",command=apply)
b2 = Button(root,text="reset",command=reset)

c1.pack()
c2.pack()
c3.pack()
b1.pack()
b2.pack()

root.mainloop()