from tkinter import *

def get():
	print(e1.get())
	print(e2.get())
	
root = Tk()

e1 = Entry(root)
e2 = Entry(root)

b1 = Button(root,text="get",command=get)

e1.pack()
e2.pack()
b1.pack()

root.mainloop()