from tkinter import *

def get():
	#a = var1.get()
	a = e1.get()
	var2.set(a)
	
def reset():
	var1.set("")
	var2.set("")
	
root = Tk()

var1 = StringVar()
var2 = StringVar()

e1 = Entry(root,textvariable=var1)
e2 = Entry(root,textvariable=var2)

b1 = Button(root,text="get",command=get)
b2 = Button(root,text="reset",command=reset)

e1.pack()
e2.pack()
b1.pack()
b2.pack()

root.mainloop()