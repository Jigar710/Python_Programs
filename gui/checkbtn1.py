from tkinter import *

def apply():
	print(var1.get())

def reset():
	var1.set(0)
	
root = Tk()

var1 = IntVar()

c1 = Checkbutton(root,text="red",variable=var1,onvalue=10,offvalue=0)
c2 = Checkbutton(root,text="blue",variable=var1,onvalue=10,offvalue=0)
c3 = Checkbutton(root,text="green",variable=var1,onvalue=30,offvalue=0)

b1 = Button(root,text="apply",command=apply)
b2 = Button(root,text="reset",command=reset)

c1.pack()
c2.pack()
c3.pack()
b1.pack()
b2.pack()

root.minsize(300,300)
root.mainloop()