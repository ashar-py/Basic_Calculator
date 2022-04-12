# CalculatorII.py
from math import *
from tkinter import *

root = Tk()
root.title('Calculator')

# Display Screen
screen = Entry(root, width=30, bd=3)
screen.grid(row=0, column=0, columnspan=5, sticky=W + E, pady=3, padx=10)


# Button press
def click(num):
    screen.insert(END, num)


# Math addition
def add():
    global f_num, math
    f_num = screen.get()
    math = '+'
    screen.delete(0, END)


# Math subtraction
def sub():
    global f_num, math
    f_num = screen.get()
    if f_num == '':
        screen.insert(0, '-')
    else:
        math = '-'
        screen.delete(0, END)


# Math multiplication
def mul():
    global f_num, math
    f_num = screen.get()
    math = '*'
    screen.delete(0, END)


# Math division
def div():
    global f_num, math
    f_num = screen.get()
    math = '/'
    screen.delete(0, END)


# Rasing to power
def power(p):
    global f_num, math
    f_num = int(screen.get())
    screen.delete(0, END)
    if p == 2:
        screen.insert(0, f_num ** 2)
    else:
        math = '**'


# Square root
def sqroot():
    global f_num
    f_num = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, str(sqrt(f_num)))


# Clear
def ac():
    screen.delete(0, END)


# Result
def equal():
    global f_num, math
    s_num = screen.get()
    screen.delete(0, END)

    if math == '+':
        screen.insert(0, str(int(f_num) + int(s_num)))
    elif math == '-':
        screen.insert(0, str(int(f_num) - int(s_num)))
    elif math == '*':
        screen.insert(0, str(int(f_num) * int(s_num)))
    elif math == '/':
        if s_num == '0':
            screen.insert(0, 'NaN')
        else:
            screen.insert(0, str(int(f_num) / int(s_num)))
    elif math == '**':
        screen.insert(0, str(int(f_num) ** int(s_num)))


# BackSpace
def backspace():
    temp = screen.get()
    screen.delete(0, END)
    temp = temp[0:len(temp) - 1]

    screen.insert(0, temp)


# Defining all buttons
b0 = Button(root, text='0', padx=5, pady=2, command=lambda: click(0))
b1 = Button(root, text='1', padx=5, pady=2, command=lambda: click(1))
b2 = Button(root, text='2', padx=5, pady=2, command=lambda: click(2))
b3 = Button(root, text='3', padx=5, pady=2, command=lambda: click(3))
b4 = Button(root, text='4', padx=5, pady=2, command=lambda: click(4))
b5 = Button(root, text='5', padx=5, pady=2, command=lambda: click(5))
b6 = Button(root, text='6', padx=5, pady=2, command=lambda: click(6))
b7 = Button(root, text='7', padx=5, pady=2, command=lambda: click(7))
b8 = Button(root, text='8', padx=5, pady=2, command=lambda: click(8))
b9 = Button(root, text='9', padx=5, pady=2, command=lambda: click(9))

b_add = Button(root, text='+', padx=5, pady=2, command=add)
b_sub = Button(root, text='–', padx=6, pady=2, command=sub)
b_mul = Button(root, text='×', padx=5, pady=2, command=mul)
b_div = Button(root, text='÷', padx=5, pady=2, command=div)

b_c = Button(root, text='C', padx=5, pady=2, command=backspace)
b_sqr = Button(root, text='√‾', padx=4, pady=2, command=sqroot)
b_sq = Button(root, text='x²', padx=5, pady=2, command=lambda: power(2))
b_pow = Button(root, text='^', padx=5, pady=2, command=lambda: power(0))

b_eq = Button(root, text='=', padx=5, pady=2, fg='cyan', command=equal)
b_clear = Button(root, text='ac', padx=5, pady=2, fg='red', command=ac)

# Griding all buttons
b7.grid(row=1, column=0, padx=1, pady=2)
b8.grid(row=1, column=1, padx=1, pady=2)
b9.grid(row=1, column=2, padx=1, pady=2)
b_add.grid(row=1, column=3, padx=1, pady=2)

b4.grid(row=2, column=0, padx=1, pady=2)
b5.grid(row=2, column=1, padx=1, pady=2)
b6.grid(row=2, column=2, padx=1, pady=2)
b_sub.grid(row=2, column=3, padx=1, pady=2)

b1.grid(row=3, column=0, padx=1, pady=2)
b2.grid(row=3, column=1, padx=1, pady=2)
b3.grid(row=3, column=2, padx=1, pady=2)
b_mul.grid(row=3, column=3, padx=1, pady=2)

b_clear.grid(row=4, column=0, padx=1, pady=2)
b0.grid(row=4, column=1, padx=1, pady=2)
b_eq.grid(row=4, column=2, padx=1, pady=2)
b_div.grid(row=4, column=3, padx=1, pady=2)

b_c.grid(row=1, column=4, padx=1, pady=2)
b_sqr.grid(row=2, column=4, padx=1, pady=2)
b_sq.grid(row=3, column=4, padx=1, pady=2)
b_pow.grid(row=4, column=4, padx=1, pady=2)

mainloop()
