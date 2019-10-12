from tkinter import *
import random
root = Tk()
wd = 600
ht =300
canvas = Canvas(root, width = wd,height = ht)
canvas.pack()
#canvas.create_arc(10,10,200,80, exten = 90,style = ARC)
#canvas.create_arc(10,50,200,160, exten = 90,style = ARC)
canvas.create_text(300,150, text = "NAZMUL + RAFIA", fill = "red", font = ("Times",30) )

root.mainloop()


