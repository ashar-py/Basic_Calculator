from tkinter import *

root=Tk()
root.title('Calculator')

ent=Entry(root, width=40,bg='white', borderwidth=4)
ent.grid(row=0, column=0, columnspan=4)

def click(fnum):
	temp=ent.get()
	ent.delete(0,END)
	ent.insert(0,temp+str(fnum))

def add():
	global fnum,math
	math='+'
	fnum=int(ent.get())
	ent.delete(0,END)

def mul():
	global fnum,math
	math='*'
	fnum=int(ent.get())
	ent.delete(0,END)

def sub():
	global fnum,math
	math='-'
	fnum=int(ent.get())
	ent.delete(0,END)

def div():
	global fnum,math
	math='/'
	fnum=int(ent.get())
	ent.delete(0,END)

def clear():
	ent.delete(0,END)

def equal():
	global fnum,math
	snum=int(ent.get())
	ent.delete(0,END)

	if math=='+':
		ent.insert(0,fnum+snum)
	elif math=='-':
		ent.insert(0,fnum-snum)
	elif math=='*':
		ent.insert(0,fnum*snum)
	elif math=='/':
		if snum==0:
			ent.insert(0,'NaN')
		else:
			ent.insert(0,fnum/snum)


b0=Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
b1=Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
b2=Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
b3=Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
b4=Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
b5=Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
b6=Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
b7=Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
b8=Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
b9=Button(root, text='9', padx=40, pady=20, command=lambda: click(9))

b_clear=Button(root, text='Clear', padx=76, pady=20, bg='red', fg='white', command=clear)
b_equal=Button(root, text='=', padx=160, pady=20, bg='cyan', fg='white', command=equal)

b_add=Button(root, text='+', padx=40, pady=20, command=add)
b_sub=Button(root, text='-', padx=40, pady=20, command=sub)
b_mul=Button(root, text='*', padx=40, pady=20, command=mul)
b_div=Button(root, text='/', padx=40, pady=20, command=div)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b_add.grid(row=1, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b_sub.grid(row=2, column=3)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b_mul.grid(row=3, column=3)

b0.grid(row=4, column=0)
b_clear.grid(row=4, column=1, columnspan=2)
b_div.grid(row=4, column=3)
b_equal.grid(row=5, column=0, columnspan=4)


root.mainloop()



