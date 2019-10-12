from tkinter import *
import time
root = Tk()
wd = 600
ht =300
canvas = Canvas(root, width = wd,height = ht)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35, fill='red')
for i in range(60):
    canvas.move(1,5,0)
    root.update()
    time.sleep(0.1)


root.mainloop()


