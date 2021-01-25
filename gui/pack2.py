from tkinter import *

root = Tk()

b1 = Button(root,text="first")
b2 = Button(root,text="sec")
b3 = Button(root,text="third")
b4 = Button(root,text="fourth")
b5 = Button(root,text="fifth")

b1.pack(side=TOP,fill='x')
b2.pack(side=BOTTOM,fill='x')
b3.pack(side=LEFT,fill='y')
b4.pack(side=RIGHT,fill='y')
b5.pack(side=TOP,fill=BOTH,expand=True)

root.title("Pack Example")
root.minsize(200,200)
root.maxsize(400,400)
root.mainloop()