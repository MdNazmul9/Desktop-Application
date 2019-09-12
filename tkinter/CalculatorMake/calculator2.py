from tkinter import *
root = Tk()
equa = ""
equation = StringVar()
calculation = Label(root,textvariable = equation)
equation.set("25+54")
calculation.grid(columnspan=4)

def btnPress(num):
    global equa
    equa = equa+str(num)
    equation.set(equa)

Button0 = Button(root, text = "0", command = lambda :btnPress(0))
Button0.grid(row = 1,column = 0)

Button1 = Button(root, text = "1", command = lambda :btnPress(1))
Button1.grid(row = 1,column = 1)

Button2 = Button(root, text = "2", command = lambda :btnPress(2))
Button2.grid(row = 1,column = 2)

root.mainloop()