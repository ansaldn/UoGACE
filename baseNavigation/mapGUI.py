#Map GUI
#baseNavigation
#Created by: Naa Kotey
#Date 09/02/21
#Version 1.0

#Basic shell of compound structure

from tkinter import *

canvas = Canvas(width=1200, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)


#perimeter
#line format(x1,y1, x2, y2)
canvas.create_line(110, 70, 1050, 70, width = 3) #top line prtimeter
canvas.create_line(110, 70, 80, 120, width = 3) #diagonal top left
canvas.create_line(110, 550, 80, 520, width = 3) #diagonal bottom left
canvas.create_line(1050, 70, 1100, 120, width = 3) #diagonal top right
canvas.create_line(1050, 550, 1100, 510, width = 3) #diagonal bottom right
canvas.create_line(80, 120, 80, 520, width = 3)# left line perimeter
canvas.create_line(1100, 120, 1100, 510, width = 3)#right line perimeter
canvas.create_line(110, 550, 1050, 550, width = 3) #bottom line


#Compound Structures
canvas.create_rectangle(150, 290, 230, 360, width=2, fill='grey')#base1
canvas.create_rectangle(940, 290, 1020, 360, width=2, fill='grey')#base2
canvas.create_rectangle(350, 550, 800, 470, width=2, fill='grey')#home


#labels
canvas.create_text(
    550,440,
    font = "Times 12 bold",
    text = "Home")

canvas.create_text(
    180,370,
    font = "Times 12 bold",
    text = "Base1")

canvas.create_text(
    970,370,
    font = "Times 12 bold",
    text = "Base2")

canvas.create_text(
    550,40,
    font = "Times 25 bold",
    text = "ACE Compound")

  
mainloop()
