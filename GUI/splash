# Author Regan Smith
# Version 1.0
# Date 21/03/2021

# libraries
from tkinter import *
from PIL import ImageTk, Image

# splash page
splash_page = Tk()
# high and width of form
app_width = 600
app_height = 800
# size and where the app appears
splash_page.geometry(f'{app_width}x{app_height}+{740}+{100}')
splash_page.overrideredirect(True) # Hides title bar
# Define background image
splash_page_background = ImageTk.PhotoImage(file="background.jpg")
# Define background canvas
splash_page_canvas = Canvas(splash_page, width=600, height=800)
splash_page_canvas.pack(fill="both", expand=True)
# insert image and Text
splash_page_canvas.create_image(0,0, image=splash_page_background, anchor="nw")
# Title Labels
splash_page_canvas.create_text(300, 150, text="ADVANCED COMPUTER ENGINEERING", font=("Helvetica",22))
splash_page_canvas.create_text(300, 200, text="MARS ROVER PROJECT", font=("Helvetica",22))

def main_window():
    # remove splash page
    splash_page.destroy()
    # main page
    main_page = Tk()
    main_page.title('ACE : MARS PROJECT')
    main_page.geometry(f'{app_width}x{app_height}+{740}+{100}')

# splash screen timer
splash_page.after(3000, main_window)

mainloop()
