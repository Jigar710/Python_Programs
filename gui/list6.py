from tkinter import *

def add():
	selection = lbox1.curselection()
	for i in selection:
		data = lbox1.get(i)
		lbox2.insert(END,data)
	
def remove():
	selection = lbox2.curselection()
	print(selection)
	cnt = 0
	for i in selection:
		lbox2.delete(i-cnt)	
		cnt += 1

root = Tk()

lbox1 = Listbox(root,selectmode=MULTIPLE)
lbox2 = Listbox(root,selectmode=MULTIPLE)

lbox1.insert(END,*(10,20,30,40,50,60,70,80,90,100))

frame = Frame(root)

b1 = Button(frame,text=">>",command=add)
b2 = Button(frame,text="<<",command=remove)

b1.pack(side=TOP)
b2.pack(side=TOP)

lbox1.pack(side=LEFT)
frame.pack(side=LEFT)
lbox2.pack(side=LEFT)

root.mainloop()