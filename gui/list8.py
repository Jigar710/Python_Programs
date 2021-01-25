from tkinter import *

root = Tk()

frame = Frame(root)

scrollbar = Scrollbar(frame, orient=VERTICAL)

listbox = Listbox(frame, yscrollcommand=scrollbar.set)
#listbox = Listbox(frame)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
lst = ['one','tow','tjree','four','one','tow','tjree','four','one','tow','tjree','four','one','tow','tjree','four']

for i in lst:
	listbox.insert(END,i)
	
frame.pack()	
root.mainloop()