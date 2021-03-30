#Map GUI
#baseNavigation
#Created by: Naa Kotey
#Date 09/02/21
#Version 1.2

from tkinter import *
import tkinter as tk
#import autonomousRover


canvas = Canvas(width=1200, height=600, bg='gray89')
canvas.pack(expand=YES, fill=BOTH)

#perimeter
#line format(x1,y1, x2, y2)
canvas.create_line(160, 70, 1100, 70, width = 6) #top line perimeter
canvas.create_line(160, 70, 130, 120, width = 6) #diagonal top left
canvas.create_line(160, 550, 130, 520, width = 6) #diagonal bottom left
canvas.create_line(1100, 70, 1150, 120, width = 6) #diagonal top right
canvas.create_line(1100, 550, 1150, 510, width = 6) #diagonal bottom right
canvas.create_line(130, 120, 130, 520, width = 6)# left line perimeter
canvas.create_line(1150, 120, 1150, 510, width = 6)#right line perimeter
canvas.create_line(160, 550, 1100, 550, width = 6) #bottom line 

canvas.create_polygon(
    130, 120,
    160, 70, 1100, 70,
    1150, 120,
    1150, 510,
    1100, 550,
    160, 550,
    130, 520,
    width = 3,
    fill = 'antique white')

#GRIDLINES
canvas.create_line(130, 120, 1150, 120, width = 3, fill ='white') #x line
canvas.create_line(130, 520, 1150, 520, width = 3, fill ='white') #x line
canvas.create_line(130, 170, 1150, 170, width = 3, fill ='white') #x line
canvas.create_line(130, 220, 1150, 220, width = 3, fill ='white') #x line
canvas.create_line(130, 270, 1150, 270, width = 3, fill ='white') #x line
canvas.create_line(130, 320, 1150, 320, width = 3, fill ='white') #x line
canvas.create_line(130, 370, 1150, 370, width = 3, fill ='white') #x line
canvas.create_line(130, 420, 1150, 420, width = 3, fill ='white') #x line
canvas.create_line(130, 470, 1150, 470, width = 3, fill ='white') #x line
canvas.create_line(130, 520, 1150, 520, width = 3, fill ='white') #x line
canvas.create_line(160, 70, 160, 550, width = 3, fill ='white') #y line
canvas.create_line(210, 70, 210, 550, width = 3, fill ='white') #y line
canvas.create_line(260, 70,260, 550, width = 3, fill ='white') #y line
canvas.create_line(310, 70, 310, 550, width = 3, fill ='white') #y line
canvas.create_line(360, 70, 360, 550, width = 3, fill ='white') #y line
canvas.create_line(410, 70, 410, 550, width = 3, fill ='white') #y line
canvas.create_line(460, 70, 460, 550, width = 3, fill ='white') #y line
canvas.create_line(510, 70, 510, 550, width = 3, fill ='white') #y line
canvas.create_line(560, 70, 560, 550, width = 3, fill ='white') #y line
canvas.create_line(610, 70, 610, 550, width = 3, fill ='white') #y line
canvas.create_line(660, 70, 660, 550, width = 3, fill ='white') #y line
canvas.create_line(710, 70, 710, 550, width = 3, fill ='white') #y line
canvas.create_line(760, 70, 760, 550, width = 3, fill ='white') #y line
canvas.create_line(810, 70, 810, 550, width = 3, fill ='white') #y line
canvas.create_line(860, 70, 860, 550, width = 3, fill ='white') #y line
canvas.create_line(910, 70, 910, 550, width = 3, fill ='white') #y line
canvas.create_line(960, 70, 960, 550, width = 3, fill ='white') #y line
canvas.create_line(1010, 70, 1010, 550, width = 3, fill ='white') #y line
canvas.create_line(1060, 70, 1060, 550, width = 3, fill ='white') #y line
canvas.create_line(1100, 70, 1100, 550, width = 3, fill ='white') #y line

####  Compound Structures ###
canvas.pack()
base1 = PhotoImage(file="base sprite.png") #base1
canvas.create_image(250, 310, image=base1)

canvas.pack()
base2 = PhotoImage(file="base sprite.png") #base2
canvas.create_image(1015, 310, image=base2)

canvas.pack()
homeL = PhotoImage(file="base sprite (1).png") #Home
canvas.create_image(510, 500, image=homeL)

canvas.pack()
homeR = PhotoImage(file="base sprite (1).png") #Home
canvas.create_image(730, 500, image=homeR)

canvas.pack()
homeCentral = PhotoImage(file="base sprite.png") #Home
canvas.create_image(620, 490, image=homeCentral)

### labels ###
canvas.create_text(
    610,430,
    font = "Times 12 bold",
    text = "HOME")

canvas.create_text(
    240,380,
    font = "Times 12 bold",
    text = "BASE1")

canvas.create_text(
    1020,380,
    font = "Times 12 bold",
    text = "BASE2")

canvas.create_text(
    600,40,
    font = "Times 25 bold",
    text = "ACE Compound")


#sprite of the buggy
canvas.pack()
buggy = PhotoImage(file="baseNav sprite.png")
canvas.create_image(500, 340, image=buggy, tag ='buggy')

def popUp():
    newWindow = tk.Toplevel()

def getBase1Dist():
    popUp()    
    
def getBase2Dist():
    popUp()    
    

'''def getPos(): #get position of buggy
    posX = 
    posY =    
    return posX
    return posY'''

def updateMap(): #update the map with the new position of buggy
    getPos()
    canvas.delete('buggy')
    canvas.create_image(posX, posY, image=buggy, tag ='buggy')
   

def plotObstacle():
    #if wayClear == False:
        getPos()
        canvas.pack()
        obstacle = PhotoImage(file="obstacle.png") 
        canvas.create_image(posX, posY, image=obstacle, tag = 'obs')
        print("obstacle plotted")

        
####  buttons  ####
updateMap = Button(
    text='Update Map', #update map to current location
    font="Times 12",
    command= updateMap()
    )
 
updateMap.pack(side=LEFT, fill=X, expand=True)

base1DistBut = Button(
    text='Find Distance from Base1', #display Distance from Base2
    font="Times 12",
    command = getBase1Dist()
    )
 
base1DistBut.pack(side=LEFT, fill=X, expand=True)

base2DistBut = Button(
    text='Find Distance from Base2', #display Distance from Base2
    font="Times 12",
    command = getBase2Dist()
    )
 
base2DistBut.pack(side=LEFT, fill=X, expand=True)

mapReset = Button( #clearing obstacles on map
    text='Reset Map',
    font="Times 12",
    command=lambda:canvas.delete("obs")
    )
 
mapReset.pack(side=LEFT, fill=X, expand=True)
           

mainloop()
