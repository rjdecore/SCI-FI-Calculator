import math
from tkinter import messagebox,Entry,Button,Tk,StringVar

screen = Tk()
screen.title("SciFi Calculator developed by Shadab")
screen.iconbitmap('icon.ico')
screen.geometry('455x480')
txt = StringVar()
operator = ''

def click(number):
    global operator
    operator += str(number)
    txt.set(operator)

def clear():
    global  operator
    operator = ''
    txt.set(operator)

def equal():
    global  operator
    try:
        result = eval(operator)
        operator = str(result)
        txt.set(result)
    except:
        messagebox.showinfo('Notification', 'Try Again Something Is Wrong...')
def sin():
    global operator
    try:
        result = math.sin(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try Again Something Is Wrong...')
def cos():
    global operator
    try:
        result = math.cos(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...')
def tan():
    global operator
    try:
        result = math.tan(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...')
def log():
    global operator
    try:
        result = math.log(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...')
def sqrt():
    global operator
    try:
        result = math.sqrt(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...')
entry1 = Entry(bg='snow',font = ('arial',20,'italic bold'), bd=25, insertwidth=4, justify='right', textvariable=txt)
entry1.grid(columnspan=4)

btnsin = Button(text='sin',font=('arial',15,'italic bold'),padx=16,pady=20,bd=8,
             bg='ghost white',command=sin, activebackground='green',activeforeground='white')
btnsin.grid(row=0,column=4)


btn7 = Button(screen, text='7', font=('arial', 22),command=lambda :click(7), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text='8', font=('arial', 22),command=lambda :click(8), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('arial', 22),command=lambda :click(9), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn9.grid(row=1, column=2)

btnPlus = Button(screen, text='+', font=('arial', 22),command=lambda :click('+'), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnPlus.grid(row=1, column=3)

btncos = Button(text='cos',font=('arial',15,'italic bold'),command=cos,padx=14,pady=20,bd=8,
             bg='ghost white', activebackground='green',activeforeground='white')
btncos.grid(row=1,column=4)

btn4 = Button(screen, text='4', font=('arial', 22),command=lambda :click(4), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('arial', 22),command=lambda :click(5), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('arial', 22),command=lambda :click(6), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn6.grid(row=2, column=2)

btnMinus = Button(screen, text='-', font=('arial', 22),command=lambda :click('-'), padx=19, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnMinus.grid(row=2, column=3)

btntan = Button(text='tan',font=('arial',15,'italic bold'),command=tan,padx=14,pady=20,bd=8,
             bg='ghost white',activebackground='green',activeforeground='white')
btntan.grid(row=2,column=4)


btn1 = Button(screen, text='1', font=('arial', 22),command=lambda :click(1), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('arial', 22),command=lambda :click(2), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('arial', 22),command=lambda :click(3), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn3.grid(row=3, column=2)

btnMul = Button(screen, text='*', font=('arial', 22),command=lambda :click('*'), padx=19, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnMul.grid(row=3, column=3)

btnsqrt = Button(text='sqrt',font=('arial',15,'italic bold'),command=sqrt,padx=11,pady=20,bd=8,
             bg='ghost white',activebackground='green',activeforeground='white')
btnsqrt.grid(row=3,column=4)


btn0 = Button(screen, text='0', font=('arial', 22),command=lambda:click(0), padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btn0.grid(row=4, column=0)

btnClear = Button(screen, text='C', font=('arial', 22), command=clear, padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnClear.grid(row=4, column=1)

btnEqual = Button(screen, text='=', font=('arial', 22), command=equal, padx=16, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnEqual.grid(row=4, column=2)

btnDivide = Button(screen, text='/', font=('arial', 22), command=lambda :click('/'), padx=20, pady=10, bd=8, bg='ghost white', activebackground='green', activeforeground ='white')
btnDivide.grid(row=4, column=3)

btnlog = Button(text='log',font=('arial',15,'italic bold'),command=lambda :click('log'),padx=14,pady=18,bd=8,
             bg='ghost white',activebackground='green',activeforeground='white')
btnlog.grid(row=4,column=4)





screen.mainloop()
