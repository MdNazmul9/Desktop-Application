from tkinter import *
root = Tk()
canvas = Canvas(root, width = 300,height =300)
canvas.pack()
def createRect(x1,y1,x2,y2):
    canvas.create_rectangle(x1, y1, x2, y2,fill = "deep pink")

createRect(20,20,100,270)
createRect(102,20,182,270)
#canvas.create_rectangle(20,20,100,270)
#canvas.create_rectangle(102,20,182,270)

#canvas.create_line(0,0,300,,300)
#canvas.create_polygon(0,0,5,20,50,30,40,15)
root.mainloop()


