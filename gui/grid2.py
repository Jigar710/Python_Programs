from tkinter import *

#help(b1.grid)

root = Tk()
b1 = Button(root,text="button1")
b2 = Button(root,text="button2")
b3 = Button(root,text="button3")
b4 = Button(root,text="button4")
b5 = Button(root,text="button5")
b6 = Button(root,text="button6")
b7 = Button(root,text="button7")

root.grid_columnconfigure(1,weight=1)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1,sticky=E+W)
b3.grid(row=0,column=2)

root.title("Grid Example")
root.minsize(200,200)
root.maxsize(400,400)
root.mainloop()