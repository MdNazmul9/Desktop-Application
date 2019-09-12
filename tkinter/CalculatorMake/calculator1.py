from tkinter import *
root = Tk()
equation = StringVar()
calculation = Label(root,textvariable = equation)
equation.set("544645+224325")
calculation.grid(columnspan=4)
root.mainloop()