from tkinter import *
root = Tk()

def random():
    print("it is the output of random function.")
def py():
    print("python 3")

def java():
    print("welcome to java class")

def js():
    print("JavaScript")
mainMenu = Menu(root)
root.configure(menu = mainMenu)


subMenu = Menu(mainMenu)
subMenu1 = Menu(mainMenu)


mainMenu.add_cascade(label="File",menu = subMenu)
mainMenu.add_cascade(label="langoage",menu = subMenu1)

subMenu.add_command(label = "random function", command = random)

subMenu1.add_command(label = "python3", command = py)
subMenu1.add_separator()
subMenu1.add_command(label = "java", command = java)
subMenu1.add_separator()
subMenu1.add_command(label = "js", command = js)
subMenu1.add_separator()

root.mainloop()
