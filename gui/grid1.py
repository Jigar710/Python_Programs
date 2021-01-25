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

b1.grid(row=0,column=0,padx=5,pady=5)
b2.grid(row=0,column=1,padx=5,pady=5)
b3.grid(row=0,column=2,padx=5,pady=5)
b4.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
b5.grid(row=1,column=2,rowspan=2,padx=5,pady=5,sticky=N+S)
b6.grid(row=2,column=0,padx=5,pady=5)
b7.grid(row=2,column=1,padx=5,pady=5)

root.title("Pack Example")
root.minsize(200,200)
root.maxsize(400,400)
root.mainloop()