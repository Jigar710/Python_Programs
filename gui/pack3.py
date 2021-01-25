from tkinter import *

root = Tk()

f1 = Frame(root,border=1,relief=RAISED)
f2 = Frame(root)

b1 = Button(f2,text="ok")
b2 = Button(f2,text="close")

f1.pack(side=TOP,fill='both',expand=True)
f2.pack(side=BOTTOM)

b2.pack(side=RIGHT,padx=5,pady=5)
b1.pack(side=RIGHT)

root.title("Pack Example")
root.minsize(200,200)
root.maxsize(400,400)
root.mainloop()