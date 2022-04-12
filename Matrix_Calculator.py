from tkinter import *
import numpy as np

root = Tk()
root.title('Matrix Calculator')

Label(root, text='Matrix A').grid(row=0, column=2, columnspan=2, sticky=W+E)
Label(root, text='[', fg='grey', font=('',60)).grid(row=1, column=0, rowspan=4)
Label(root, text=']', fg='grey', font=('',60)).grid(row=1, column=5, rowspan=4)

a=[]
for x in range(4):
	a.append([])
	for y in range(4):
		a[x].append(Entry(width=4))

for x in range(4):
	for y in range(4):
		a[x][y].grid(row=x+1, column=y+1, padx=3, pady=2)


Label(root, text='Matrix B').grid(row=0, column=11, columnspan=2, sticky=W+E)
Label(root, text='[', fg='grey', font=('',60)).grid(row=1, column=9, rowspan=4)
Label(root, text=']', fg='grey', font=('',60)).grid(row=1, column=14, rowspan=4)

b=[]
for x in range(4):
	b.append([])
	for y in range(4):
		b[x].append(Entry(width=4))

for x in range(4):
	for y in range(4):
		b[x][y].grid(row=x+1, column=y+10, padx=3, pady=2)


def change():
	return


def multiply():
	return


def add():
	return


def determinant(m):
	global A, B, count, result

	'''
	B=np.array(
		[[int(b[0][0].get()), int(b[0][1].get()), int(b[0][2].get()), int(b[0][3].get())],
		[int(b[1][0].get()), int(b[1][1].get()), int(b[1][2].get()), int(b[1][3].get())],
		[int(b[2][0].get()), int(b[2][1].get()), int(b[2][2].get()), int(b[2][3].get())],
		[int(b[3][0].get()), int(b[3][1].get()), int(b[3][2].get()), int(b[3][3].get())]])
	'''
	print(m)
	if m =='B':
		A=np.array(
		[[int(a[0][0].get()), int(a[0][1].get()), int(a[0][2].get()), int(a[0][3].get())],
		[int(a[1][0].get()), int(a[1][1].get()), int(a[1][2].get()), int(a[1][3].get())],
		[int(a[2][0].get()), int(a[2][1].get()), int(a[2][2].get()), int(a[2][3].get())],
		[int(a[3][0].get()), int(a[3][1].get()), int(a[3][2].get()), int(a[3][3].get())]])
		
		d = np.linalg.det(A)

		Label(result, text='|', font=('', 60)).grid(row= 1, column=0)
		Label(result,
			text=str(A[0][0])+' '+str(A[0][1])+' '+str(A[0][2])+' '+str(A[0][3])+'\n'+
				str(A[1][0])+' '+str(A[1][1])+' '+str(A[1][2])+' '+str(A[1][3])+'\n'+
					str(A[2][0])+' '+str(A[2][1])+' '+str(A[2][2])+' '+str(A[2][3])+'\n'+
						str(A[3][0])+' '+str(A[3][1])+' '+str(A[3][2])+' '+str(A[3][3]), font=('',15)).grid(row=1, column=1, rowspan=4, columnspan=4)

		Label(result, text='|', font=('', 60)).grid(row= 1, column=5)
		Label(result, text=' = ' + str(d)).grid(row= 1, column=6)
		count+=7
	


def inverse():
	return


Button(root, text='<->', command=change).grid(row=2, column=7, padx=50)
Button(root, text='A x B', command=multiply).grid(row=4, column=7, padx=50)
Button(root, text='A + B', command=add).grid(row=3, column=7, padx=50)

p=0
for mat in "AB":
	print(mat)
	Button(root, text='det('+mat+')', padx=20, command=lambda: determinant(mat)).grid(row=5, column=p, columnspan=3, padx=5, pady=5)
	print(mat)
	Button(root, text='adj('+mat+')', padx=20, command='''lambda: determinant(mat)''').grid(row=5, column=p+3, columnspan=3, padx=5, pady=5)
	Button(root, text='inv('+mat+')', padx=20, command='''lambda: determinant(mat)''').grid(row=6, column=p, columnspan=3, padx=5, pady=5)
	Button(root, text='sqr('+mat+')', padx=20, command='''lambda: determinant(mat)''').grid(row=6, column=p+3, columnspan=3, padx=5, pady=5)
	Button(root, text='Clear', padx=10, command='''lambda: determinant(mat)''').grid(row=7, column=p, columnspan=3, padx=5, pady=5)
	print("Now for B")
	p+=9

result = LabelFrame(root, bd=2)
result.grid(row=8, column=0, columnspan=16, pady=30, sticky=W+E)
Label(result, text=' hekjs').grid(row=0, column=0)
Button(root, text='Clean', fg='red', bd=0, command=lambda: clear('R')).grid(row=9, column=15)
count=0

mainloop()