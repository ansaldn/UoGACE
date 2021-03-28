# Author Regan Smith
# Version 1.0
# Date 21/03/2021

# libraries
from tkinter import *
from PIL import ImageTk, Image

# main page
main_page = Tk()
main_page.title('ACE MARS PROJECT')

# high and width of form
app_width = 600
app_height = 800
# size and where the app appears
main_page.geometry(f'{app_width}x{app_height}+{740}+{100}')

# Buggy Control Frame
frame1 = LabelFrame(main_page, padx=10, pady=10)
frame1.grid(row=0,column=0)
button1 =Button(frame1,text="Buggy Control", bg="#3498db",width=37, height=16, padx=5, pady=5 ).pack()

# Base Control Frame
frame2 = LabelFrame(main_page, padx=10, pady=10)
frame2.grid(row=0,column=1)
button2 =Button(frame2,text="Base Control", bg="#3498db", width=37, height=16, padx=5, pady=5).pack()

# Network Status Frame
frame3 = LabelFrame(main_page, padx=10, pady=10)
frame3.grid(row=1,column=0)
button3 =Button(frame3,text="Network Status", bg="#3498db",width=37, height=16, padx=5, pady=5 ).pack()

# System Status Frame
frame4 = LabelFrame(main_page, padx=10, pady=10)
frame4.grid(row=1,column=1)
button4 =Button(frame4,text="System Status", bg="#3498db",width=37, height=16, padx=5, pady=5).pack()

# Label for separation
label1 = Label(main_page, width="10", height="10")
label1.grid(row=2,column=0)

# Sign Out Frame
frame5 = LabelFrame(main_page, pady=10, padx=10)
frame5.grid(row=3,column=0)
button5 =Button(frame5,text="Sign Out", bg="white",width=20, height=2, padx=5, pady=5).pack()

main_page.mainloop()
