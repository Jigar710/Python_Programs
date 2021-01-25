from tkinter import *
from tkinter import font

root = Tk()
root.title("My window")
root.minsize(200,200)
root.maxsize(400,400)
root.geometry("300x300")

btn1 = Button(root,text="First")
btn2 = Button(root,text="First",font=font.Font(size=20))
btn3 = Button(root,text="First",font=('times new roman',20,'bold'))

btn1.pack()
btn2.pack()
btn3.pack()

root.mainloop()