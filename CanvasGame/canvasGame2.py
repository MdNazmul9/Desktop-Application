from tkinter import *
import random
root = Tk()
wd = 900
ht =600

canvas = Canvas(root, width = wd,height = ht)
canvas.pack()

def  randomRect(num):
    for i in range(num):
        lm = 150
        x1 = random.randrange(lm)
        y1 = random.randrange(lm)
        x2 = x1 + random.randrange(lm)
        y2 = y1 + random.randrange(lm)
        canvas.create_rectangle(x1, y1, x2, y2, fill="deep pink")
        #if i<20:
        #canvas.create_polygon(x1, y1, x2, y2,y1,y2,x1,x2,fill='blue')

randomRect(50)

'''
def createRect(x1,y1,x2,y2):
    canvas.create_rectangle(x1, y1, x2, y2,fill = "deep pink")
'''

root.mainloop()


