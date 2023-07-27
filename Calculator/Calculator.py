import tkinter as tk

# let's create the base GUI
root = tk.Tk()
root.geometry('320x465') # size change
root.resizable(width=False, height=False) # Fixed size
root.title('Calculator') # title change
root.iconbitmap('Calculator/calculator_icon.ico')
root.config(bg='#FFFDD0') # giving a background color to root gui

# lets define all the function below this
def insert_modulo():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='%')
    else:
        label.config(text=previous_value + '%')

def insert_clearentry():
    label.config(text='CE')

def insert_clear():
    label.config(text='0')

def insert_delete():
    previous_value = label.cget('text')
    if len(previous_value) == 1:
        label.config(text='0')
    else:
        label.config(text=previous_value[:-1])

def insert7():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='7')
    else:
        label.config(text=previous_value + '7')

def insert8():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='8')
    else:
        label.config(text=previous_value + '8')

def insert9():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='9')
    else:
        label.config(text=previous_value + '9')

def insert_multiply():
    previous_value = label.cget('text')
    if previous_value != '0':
        label.config(text=previous_value + '*')

def insert4():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='4')
    else:
        label.config(text=previous_value + '4')

def insert5():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='5')
    else:
        label.config(text=previous_value + '5')

def insert6():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='6')
    else:
        label.config(text=previous_value + '6')

def insert_subtraction():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='-')
    else:
        label.config(text=previous_value + '-')

def insert1():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='1')
    else:
        label.config(text=previous_value + '1')

def insert2():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='2')
    else:
        label.config(text=previous_value + '2')

def insert3():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='3')
    else:
        label.config(text=previous_value + '3')

def insert_addition():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='+')
    else:
        label.config(text=previous_value + '+')

def insert0():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='0')
    else:
        label.config(text=previous_value + '0')

def insert_decimal():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='.')
    else:
        label.config(text=previous_value + '.')

def insert_divide():
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='/')
    else:
        label.config(text=previous_value + '/')

def evaluation():
    expression = label.cget('text')
    try:
        result = eval(expression)
        label.config(text=str(result))
    except Exception as e:
        label.config(text='Error')

# label widget to display text
label = tk.Label(root, text='0', bg='#FFFDD0', font=('Comic Sans MS', 35), anchor='e', padx=10)
label.pack(pady=(65, 10), fill='x')

# let's add a new container in root GUI
frame = tk.Frame(root, bg='#FFFDD0')
frame.pack(fill='both')

# buttons --> row 0 --> Percentage, CE, C, Delete
btn_percent = tk.Button(frame, text='%', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_modulo)
btn_ce = tk.Button(frame, text='CE', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_clearentry)
btn_c = tk.Button(frame, text='C', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_clear)
btn_delete = tk.Button(frame, text='DEL', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_delete)
btn_percent.grid(row=0, column=0, padx=3, pady=3)
btn_ce.grid(row=0, column=1, padx=3, pady=3)
btn_c.grid(row=0, column=2, padx=3, pady=3)
btn_delete.grid(row=0, column=3, padx=3, pady=3)

# buttons --> row 1 --> 7,8,9,*
btn_7 = tk.Button(frame, text='7', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert7)
btn_8 = tk.Button(frame, text='8', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert8)
btn_9 = tk.Button(frame, text='9', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert9)
btn_x = tk.Button(frame, text='*', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_multiply)
btn_7.grid(row=1, column=0, padx=3, pady=3)
btn_8.grid(row=1, column=1, padx=3, pady=3)
btn_9.grid(row=1, column=2, padx=3, pady=3)
btn_x.grid(row=1, column=3, padx=3, pady=3)

# buttons --> row 2 --> 4,5,6,-
btn_4 = tk.Button(frame, text='4', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert4)
btn_5 = tk.Button(frame, text='5', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert5)
btn_6 = tk.Button(frame, text='6', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert6)
btn_minus = tk.Button(frame, text='-', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_subtraction)
btn_4.grid(row=2, column=0, padx=3, pady=3)
btn_5.grid(row=2, column=1, padx=3, pady=3)
btn_6.grid(row=2, column=2, padx=3, pady=3)
btn_minus.grid(row=2, column=3, padx=3, pady=3)

# buttons --> row 3 --> 1,2,3,+
btn_1 = tk.Button(frame, text='1', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert1)
btn_2 = tk.Button(frame, text='2', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert2)
btn_3 = tk.Button(frame, text='3', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert3)
btn_sum = tk.Button(frame, text='+', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_addition)
btn_1.grid(row=3, column=0, padx=3, pady=3)
btn_2.grid(row=3, column=1, padx=3, pady=3)
btn_3.grid(row=3, column=2, padx=3, pady=3)
btn_sum.grid(row=3, column=3, padx=3, pady=3)

# buttons --> row 4 --> +/-, 0, ., =
btn_divide = tk.Button(frame, text='/', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_divide)
btn_0 = tk.Button(frame, text='0', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert0)
btn_decimal = tk.Button(frame, text='.', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_decimal)
btn_equal = tk.Button(frame, text='=', width=9, height=3, bg='#1e90ff', fg='#ffffff', relief='groove', font=('Trebuchet', 9), command=evaluation)
btn_divide.grid(row=4, column=3, padx=3, pady=3)
btn_0.grid(row=4, column=1, padx=3, pady=3)
btn_decimal.grid(row=4, column=2, padx=3, pady=3)
btn_equal.grid(row=4, column=0, padx=3, pady=3)

# let's run mainloop
root.mainloop()