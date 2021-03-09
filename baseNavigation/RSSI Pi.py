
#Wifi Heat Map + RSSI TEST
#baseNavigation
#VERSION 1.0
#Created by: Naa Kotey
#Date 09/02/21

#PURPOSE: create a interactive gui map of the compund
#layer on a wifi heat map of WAPs
#Update map GUI with the position of the rover via RSSI

from tkinter import *#gui plugin
from tkinter import ttk
import subprocess
from uuid import getnode
#import pil #tkinter pillow
#from pil import ImageTk, Image
from tkinter import filedialog
#The more acess points, the more accurate the picture
#proof of concept for windows
#dB via wifi

#scan and display the available wifi

networkRaw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
networkDecoded = networkRaw.decode('ascii') # makes the information readable to the user
print(networkDecoded)

#get mac address
mac = getnode()
print(mac) #this is meaningless
print(hex(mac))
macString = ':' .join(("%012X" % mac) [i:i+2] for i in range(0,12,2))
print('[' + macString + ']')

myMac = macString

#def get_RSSI(myMac):
    
#map gui
'''
root = Tk()
root.title('ACE Compound') #title
root.geometry('700x600') #dimensions
canvas.create_rectangle
#root.config('bg #212322') #background colour
'''

canvas = Canvas(width=1200, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)                
     
canvas.create_rectangle(80, 80, 1100, 600, width=5, fill='white') #perimeter
canvas.create_rectangle(280, 280, 400, 400, width=5, fill='white')#base1
canvas.create_rectangle(580, 280, 400, 400, width=5, fill='white')#base2
canvas.create_rectangle(900, 80, 700, 500, width=5, fill='white')#home
     
widget = Label(canvas, text='ACE Compound', fg='black')# title1
widget.pack()
canvas.create_window(50, 50, window=widget)     
mainloop()