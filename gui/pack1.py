from tkinter import *

root = Tk()
root.title("My window")
root.minsize(200,200)
root.maxsize(400,400)
root.geometry("300x300")

btn1 = Button(root,text="first")
btn2 = Button(root,text="sec")
btn3 = Button(root,text="third")
'''
btn1.pack(side=BOTTOM)
btn2.pack(side='bottom')
btn3.pack(side=BOTTOM)
'''
'''
btn1.pack(side=BOTTOM)
btn2.pack(side='bottom',after=btn1)
btn3.pack(side=BOTTOM,after=btn2)
'''
'''
btn1.pack(side=LEFT)
btn2.pack(side='left',after=btn1)
btn3.pack(side=LEFT,after=btn2)
'''
'''
btn1.pack(side=LEFT)
btn2.pack(side='left')
btn3.pack(side=LEFT)
'''
'''
btn1.pack(side=LEFT)
btn2.pack(side='left')
btn3.pack(side=LEFT,before=btn2)
'''

btn1.pack(side=LEFT,fill=Y)
btn2.pack(side='left')
btn3.pack(side=LEFT)

root.mainloop()