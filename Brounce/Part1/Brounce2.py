from tkinter import  *
import random
import time

tk = Tk()
tk.title("Brounce!")

# windows screen not changeable/ resizeable
tk.resizable(0,0)

# Never hide the brounce window
tk.wm_attributes("-topmost",1)

canvas = Canvas(tk,width = 700,height = 700,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas


        self.id = canvas.create_rectangle(0,0,700,700,fill ='green')
        self.id = canvas.create_oval(0,0,700,700,fill = color)
        self.id = canvas.create_oval(20, 20, 700-20, 700-20, fill="deep pink")
        #self.id = canvas.create_rectangle(10,0,490,500)
        #self.canvas.move(self.id,245,100)

        #self.id.save("circle.png")
    def draw(self):
        pass
ball = Ball(canvas, 'red')
tk.mainloop()