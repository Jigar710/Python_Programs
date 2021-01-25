from tkinter import *

def apply():
	print(var1.get())
	print(var2.get())
	print(var3.get())

def reset():
	var1.set(0)
	var2.set(0)
	var3.set(0)
	
root = Tk()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

c1 = Checkbutton(root,text="red",variable=var1,onvalue=255,offvalue=0)
c2 = Checkbutton(root,text="blue",variable=var2,onvalue=255,offvalue=0)
c3 = Checkbutton(root,text="green",variable=var3,onvalue=255,offvalue=0)

b1 = Button(root,text="apply",command=apply)
b2 = Button(root,text="reset",command=reset)

c1.pack()
c2.pack()
c3.pack()
b1.pack()
b2.pack()

root.minsize(300,300)
root.mainloop()