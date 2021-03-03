import tkinter

def password():

    print ('Welcome user ! Please enter password below\n')
    print ('The password entered must be between 6-12 characters long\n')

    while True:
        password = input ('Please enter your password . . . :')
        weak = 'weak'
        med = 'medium'
        strong = 'strong'
        if len(password) >12:
            print ('password is too long It must be between 6 and 12 characters')
        elif len(password) <6:
            print ('password is too short It must be between 6 and 12 characters')
        elif len(password) >=6 and len(password) <= 12:
            print ('password ok\n')
            if password.lower()== password or password.upper()==password or password.isalnum()==password:
                print ('password is', weak)
            elif password.lower()== password and password.upper()==password or password.isalnum()==password and password.upper()==password:
                print ('password is', medium)
            else:
                password.lower()== password and password.upper()==password and password.isalnum()==password
                print ('password is', strong)
            break

password()

from tkinter import *

import csv

window = Tk()
window.title("Mars Base")

def welcome():
    my_label.config(bg="white", text="Welcome")
my_label = Label(window, bg="blue",text="Welcome to the Mars Base Interface")
my_label.grid(row=0, column=2)


input_name = Label(window, text="Username").grid(row=1, column=1)
my_text_box = Entry(window, width=30)
my_text_box.grid(row=1,column=2)

input_address = Label(window, text="Password").grid(row=2, column=1)
my_text_box = Entry(window, width=30)
my_text_box.grid(row=2,column=2)


my_button = Button(window, text="Start", command=welcome)
my_button.grid(row=3, column=2)

    # open file to read
with open('GUI.csv', 'a') as f:
    w=csv.writer(f, delmiter=',')
    w.writerow([self.input_username.get()])
    w.writerow([self.input_password.get()])


    for row in reader:
        date = row[8]
        if date[0] == "5":
            writer.writerow(row)

    # close file
    openedCsvFileToRead.close()
    openedCsvFileToWrite.close()

# my_picture = PhotoImage(file="/Users/David/Documents/marsLogo.jpg")
# canvas.create_image(20, 40, image=Tree, anchor=NW)

if __name__ == "__main__":
    analyse("GUI.csv", "GUI.csv")


window.mainloop()


from tkinter import*
import csv

class App(Frame):
    def __init__ (self, master=None):
        Frame._init_(self,master)
        self.pack()
        self.output()

    def output(self):
        Label(text='Name').pack(side=LEFT,padx=5, pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT, padx=5, pady=5)

        self.b = Button (root, text='Submit', command=self.writToFile)
        self.b.pack(side=RIGHT, padx=5, pady=5)

    def WriteToFile(self):
        with open('marsData.csv', 'a') as f:
            w=csv.writer(f,quoting=csv.QUOTE_ALL)
            w.writerow([self.e.get()])

if __name__ == 'main':
    root=TK()
    root.title('Auto Logger')
    root.geometry('1000x1000')
    app=App(master=root)
    app.mainloop()
    root.mainloop()
