from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Inpunt.set(operator)

def btnEqualsInputn():
    global operator
    sumup=str(eval(operator))
    text_Inpunt.set(sumup)

def btnClearDisplay():
    global operator
    operator=""
    text_Inpunt.set("")


cal = Tk()
cal.title("Calculatrice")
operator=""
text_Inpunt =StringVar()
cal['bg'] = '#ff6666'

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Inpunt, bd=30, insertwidth=4,
                   bg="#ff6666", justify='right').grid(columnspan=4)


btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="7", bg="#99ffff", command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="8",bg="#99ffff", command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="9",bg="#99ffff", command=lambda:btnClick(9)).grid(row=1,column=2)

addition=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="+",bg="#99ffff", command=lambda:btnClick("+")).grid(row=1,column=3)

#========================================================================

btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="4",bg="#99ffff", command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="5",bg="#99ffff", command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="6",bg="#99ffff", command=lambda:btnClick(6)).grid(row=2,column=2)

soustraction=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="-",bg="#99ffff", command=lambda:btnClick("-")).grid(row=2,column=3)

#==========================================================================


btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="4",bg="#99ffff", command=lambda:btnClick(1)).grid(row=3,column=0)

btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="5",bg="#99ffff", command=lambda:btnClick(2)).grid(row=3,column=1)

btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="6",bg="#99ffff", command=lambda:btnClick(3)).grid(row=3,column=2)

multiplication=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="x",bg="#99ffff", command=lambda:btnClick("*")).grid(row=3,column=3)




#==========================================================================
btn0=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="0",bg="#99ffff", command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="C",bg="#99ffff", command=btnClearDisplay).grid(row=4,column=1)

btnEgale=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="=",bg="#99ffff", command=btnEqualsInputn).grid(row=4,column=2)

btnDivision=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="/",bg="#99ffff", command=lambda:btnClick("/")).grid(row=4,column=3)



cal.mainloop()
