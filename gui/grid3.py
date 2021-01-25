from tkinter import *

root = Tk()

lbl = Label(root,text="windows")
txt = Text(root,relief='raised',bd=5)
btn_ok = Button(root,text="OK")
btn_help = Button(root,text="Help")
btn_add = Button(root,text="Add")
btn_remove = Button(root,text="Remove")

root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)

lbl.grid(row=0,column=0)
txt.grid(row=1,column=0,columnspan=2,rowspan=2,sticky=N+E+W+S)

btn_add.grid(row=1,column=2,sticky=W+E)
btn_remove.grid(row=2,column=2,sticky=N)
btn_help.grid(row=3,column=0,sticky=W+E,pady=5)
btn_ok.grid(row=3,column=2,sticky=W+E)

root.title("Grid Example")
root.minsize(200,200)
root.maxsize(400,400)
root.mainloop()