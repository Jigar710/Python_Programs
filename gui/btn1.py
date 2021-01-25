from tkinter import *

root = Tk()
root.title("My window")
root.minsize(200,200)
root.maxsize(400,400)
root.geometry("300x300")

#btn1 = Button(root)
#btn1 = Button(root,text="First")
#btn1 = Button(root,text="First",fg="red")
#btn1 = Button(root,text="First",fg="red",bg="blue")
btn1 = Button(root,text="First",fg="red",bg="blue",relief=SUNKEN)
btn1.pack()

root.mainloop()