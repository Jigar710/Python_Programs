import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog

flag_save = False

def new():
	global flag_save
	data = txt.get(1.0,tk.END)
	#print(len(data))
	
	if(flag_save == True):
		txt.delete(1.0,tk.END)
		
	elif(len(data)>1 and flag_save == False):
		ans = messagebox.askyesnocancel(title='Save',message='Do u want to save changes')
		#print(ans)
		if(ans==True):
			save()
			txt.delete(1.0,tk.END)
			
		elif(ans==False):
			txt.delete(1.0,tk.END)
			
	flag_save = False
	
def fopen():
	ans = filedialog.askopenfilename()
	if(ans):
		f = open(ans)
		data = f.read()
		txt.delete(1.0,tk.END)
		txt.insert(1.0,data)	
		
def save():
	global flag_save
	
	ans = filedialog.asksaveasfilename(defaultextension='.txt',filetype=[('text files','.txt'),('Python files','.py'),('C files','.c')])
	print(ans)
	
	if(ans):
		f = open(ans,'w')
		data = txt.get(1.0,tk.END)
		f.write(data)
		flag_save = True
		
def exit():
	root.destroy()

def cut():
	pass
def copy():
	pass
def paste():
	pass
def clear():
	pass

#format menu
def fg():
	a,c = colorchooser.askcolor()
	txt.config(fg=c)
def bg():
	a,c = colorchooser.askcolor()
	txt.config(bg=c)
def normal():
	txt.config(font=("arail",15))
def italic():
	txt.config(font=("arail",15,"italic"))	
def bold():
	txt.config(font=("arail",15,"bold"))	
	
def help():
	pass

root = tk.Tk()

menubar = tk.Menu(root)

file = tk.Menu(menubar,tearoff=0)
file.add_command(label="New",command=new)
file.add_command(label="Open",command=fopen)
file.add_command(label="Save",command=save)
file.add_command(label="Exit",command=exit)

edit = tk.Menu(menubar,tearoff=0)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)
edit.add_command(label="Clear",command=clear)

format = tk.Menu(menubar,tearoff=0)
format.add_command(label="Foreground",command=fg)
format.add_command(label="Background",command=bg)
format.add_command(label="Normal Font",command=normal)
format.add_command(label="Italic Font",command=italic)
format.add_command(label="Bold Font",command=bold)

help = tk.Menu(menubar,tearoff=0)
help.add_command(label="Help Here",command=help)

menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Edit",menu=edit)
menubar.add_cascade(label="Format",menu=format)
menubar.add_cascade(label="Help",menu=help)

root.config(menu=menubar)
root.minsize(300,300)

txt = tk.Text(root)
txt.pack(expand=True,fill=tk.BOTH)

root.mainloop()