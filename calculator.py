from tkinter import*


def click_btn(num_op):
    global operator
    operator = operator + str(num_op)
    textInput.set(operator)


def clear_btn():
    global operator
    operator = ""
    textInput.set("")


def equal_btn():
    global operator
    answer = str(eval(operator))
    textInput.set(answer)


def delete_btn():
    global operator
    operator = operator[:-1]
    textInput.set(operator)


top = Tk()
top.title("Calculator")
operator = ""
textInput = StringVar()

display = Entry(top, font=('arial', 20, 'bold'), textvariable=textInput, bd=40, bg='white', justify='right',
                insertwidth=4).grid(columnspan=4)


# ==========================================================================================================


Clear = Button(top, font=('arial', 20, 'bold'), padx=64, bg='white', fg='black', text='C',
               command=clear_btn).grid(row=1, columnspan=2)

Delete = Button(top, font=('arial', 20, 'bold'), padx=64, bg='white', fg='black',
                text='Del', command=delete_btn).grid(row=1, column=2, columnspan=2)


# ===========================================================================================================


btn7 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7',
              bg='white', command=lambda: click_btn(7)).grid(row=2, column=0)
btn8 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8',
              bg='white', command=lambda: click_btn(8)).grid(row=2, column=1)
btn9 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9',
              bg='white', command=lambda: click_btn(9)).grid(row=2, column=2)
Equal_to = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=',
              bg='white', command=equal_btn).grid(row=2, column=3)

# ========================================================================================================

btn4 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4',
              bg='white', command=lambda: click_btn(4)).grid(row=3, column=0)
btn5 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5',
              bg='white', command=lambda: click_btn(5)).grid(row=3, column=1)
btn6 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6',
              bg='white', command=lambda: click_btn(6)).grid(row=3, column=2)
Addition = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+',
              bg='white', command=lambda: click_btn("+")).grid(row=3, column=3)

# ===========================================================================================================


btn1 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1',
              bg='white', command=lambda: click_btn(1)).grid(row=4, column=0)
btn2 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2',
              bg='white', command=lambda: click_btn(2)).grid(row=4, column=1)
btn3 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3',
              bg='white', command=lambda: click_btn(3)).grid(row=4, column=2)
Substraction = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
              bg='white', command=lambda: click_btn("-")).grid(row=4, column=3)


# ===========================================================================================================


decimal = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='.',
              bg='white', command=lambda: click_btn(".")).grid(row=5, column=0)
btn0 = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0',
              bg='white', command=lambda: click_btn(0)).grid(row=5, column=1)
Divide = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/',
              bg='white', command=lambda: click_btn("/")).grid(row=5, column=2)
Multiply = Button(top, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='X',
              bg='white', command=lambda: click_btn("*")).grid(row=5, column=3)

top.mainloop()