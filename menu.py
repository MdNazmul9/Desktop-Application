from tkinter import *
root = Tk()
mainMenu = Menu(root)
root.configure(menu = mainMenu)
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File",menu = subMenu)
root.mainloop()