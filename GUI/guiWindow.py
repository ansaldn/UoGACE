# Created by David Ansa
# VERSION 1.0
# DATE: 01/03/21

#Libraries
import tkinter
import csv

#Button Functions
def callback(): #A function that prints a message to the screen for button.
    if entry1.get()==entry2.get():
        display.configure(text="successful")
        window.destroy()
        window1()
    else:
        display.configure(text="Unsuccessful")

def callback1():
    window1.destroy()
    window2()

#Window Functions
def window1():
    window1 = tkinter.Tk() #set window title
    window1.title("Main Menu") #set window size
    window1.geometry("500x500") #set window colour
    window1.configure(background="white")
    button5 = tkinter.Button(window2, text="Submit", command=callback1)
    button5.pack()
    window1.mainloop()

def window2():
    window2 = tkinter.Tk() #creatd a new window
    window2.title("Home Screen") #set window title
    window2.configure(background="blue") #set window colour
    window2.geometry("500x500") #set window size
    window2.mainloop()

#First Window
window = tkinter.Tk() #Creates a new window
window.title("Mars Controller") #set window title
window.geometry("500x500") #set window size
window.configure(background="white") #set window colour
 
#create widget(s)
label = tkinter.Label(window, text="Username")
entry = tkinter.Entry(window)
label1 = tkinter.Label(window, text="Password")
entry1 = tkinter.Entry(window)
label2 = tkinter.Label(window, text="Re-Enter Password")
entry2 = tkinter.Entry(window)
display = tkinter.Label(window)    

#Add widget(s) into window
label.pack()
entry.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
display.pack()
button = tkinter.Button(window, text="Submit", command=callback)
button.pack()


window.mainloop()
    
#create the window and start the app
#This app will transfer data from the tkinter to CSV



def WriteToFile():
    with open ("courseEntry.csv", "a") as f:
        GET = '\n' +entry.get() +','+ entry1.get() +',' +entry2.get()
        f.write(GET)
        f.close

def ReadFromFile():
    with open ("CourseEntry.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print (row)

#create widget(s)
label = tkinter.Label(window2, text="name")
entry = tkinter.Entry(window2)
label1 = tkinter.Label(window2, text="course")
entry1 = tkinter.Entry(window2)
label2 = tkinter.Label(window2, text="address")
entry2 = tkinter.Entry(window2)
Label3 = tkinter.Label(window2, text="search")
entry3 = tkinter.Entry(window2)
button = tkinter.Button(window2, text="Upload", command=WriteToFile)
button1 = tkinter.Button(window2, text="Retrieve", command=ReadFromFile)
button2 = tkinter.Button(window2, text="search")


label.pack()
entry.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
button1.pack()
Label3.pack()
entry3.pack()
button2.pack()



