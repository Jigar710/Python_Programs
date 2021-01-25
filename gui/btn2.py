from tkinter import *

root = Tk()
root.title("My window")
root.minsize(200,200)
root.maxsize(400,400)
root.geometry("300x300")

btn1 = Button(root,text="first",relief='raised',width=20)
btn2 = Button(root,text="sec",relief='sunken',width=20)
btn3 = Button(root,text="third",relief=FLAT,width=20)
btn4 = Button(root,text="fourth",relief='ridge',width=20)
btn5 = Button(root,text="fifth",relief='groove',width=20)
btn6 = Button(root,text="sixth",relief='solid',width=20)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()

root.mainloop()