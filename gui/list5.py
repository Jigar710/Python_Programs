from tkinter import *

def first():
	s = lbox1.curselection()
	print(s)
	for i in s:
		print(lbox1.get(i))

def second():
	s = lbox2.curselection()
	print(s)
	
def third():
	s = lbox3.curselection()
	print(s)
	
def fourth():
	s = lbox4.curselection()
	print(s)
	
root = Tk()

lbox1 = Listbox(root)
lbox2 = Listbox(root,selectmode=SINGLE)
lbox3 = Listbox(root,selectmode=MULTIPLE)
lbox4 = Listbox(root,selectmode=EXTENDED)

lbox1.insert(END,*(1,2,3,4,5))
lbox2.insert(END,*(10,20,30,40,50))
lbox3.insert(END,*(100,200,300,400,500))
lbox4.insert(END,*(1000,2000,3000,4000,5000))

lbox1.grid(row=0,column=0)
lbox2.grid(row=0,column=1)
lbox3.grid(row=0,column=2)
lbox4.grid(row=0,column=3)

b1 = Button(root,text="first",command=first)
b2 = Button(root,text="second",command=second)
b3 = Button(root,text="third",command=third)
b4 = Button(root,text="fourth",command=fourth)

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=1,column=3)

root.mainloop()