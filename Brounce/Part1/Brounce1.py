from tkinter import  *
import random
import time

tk = Tk()
tk.title("Brounce!")

# windows screen not changeable/ resizeable
tk.resizable(0,0)

# Never hide the brounce window
tk.wm_attributes("-topmost",1)

canvas = Canvas(tk,width = 500,height = 500,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()
tk.mainloop()