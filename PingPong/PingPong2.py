from tkinter import *
import random
import time

tk = Tk()
tk.title(65*" "+"Pong")
#print(tk.wm_attributes())
# windows screen not changeable/ resizeable
tk.resizable(0, 0)
# Never hide the brounce window
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.configure(bg = 'black')
canvas.create_line(250,0,250,400,fill='white')
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 235, 200)
        starts = [-3,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y =-3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if pos[1]<=0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0]<=0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # self.paddle = paddle
        self.id = canvas.create_rectangle(0, 150, 30, 250, fill=color)
        self.y = 0
        #self.canvas.move(self.id, 200, 300)
        self.canvas_height = self.canvas.winfo_height()
        #self.x = 0

        self.canvas.bind_all("a", self.turn_left)
        self.canvas.bind_all("d", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0,self.y)
        pos = self.canvas.coords(self.id)  # [x1,y1,x2,y2]

        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
    def turn_left(self, evt):
        self.y = -3

    def turn_right(self, evt):
        self.y = 3


ball = Ball(canvas,'orange')
paddle = Paddle(canvas, "white")

while 1:

    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)


tk.mainloop()