## GUI Introduction
Documnentation of the GUI process and Code implementation for the ACE Project.

## Software Used
-[x] Design Tool : Framer.io

-[x] Software : Visual Studio, Visual Studio Code, Pycharm, Sublime Text

-[x] Language : Python
              - libraries : tkinter, csv, Pillow
## Description
This is the GUI branch of the larger project, ACE(Advanced Computer Engineering). The GUI branch of the project involves; 
  - Designing models for a GUI application to allow for functionality of the different branches of the project.
  - Developing Code to allow for implementation of designed models into a functional application.

The GUI for the project is inteded to be applied to a one app tablet in which users can sign in and control different aspects of the project over a long distance. 
For example, the application must allow for movement control of the buggy in various ways such as driving, controlling the arm, and turning the camera.

The application was developed with Python using the tkinter libary to implement useful widgets to help control functions that needed to be implemented.
## Design
To Develop our wire frame diagrams for the application we used a program called  Frame.io, this allows us to implement animated versions of our wireframe designs to better represent our vision.

A link to the wireframe design for the GUI can be found here:
https://framer.com/share/ACE-GUI--uqXDT6NO8jMDT6XoKdXz/Aj17HOaoW

## Visuals

Visual Representation of the Pages within the application as implemented within the code using tkinter.

![image](https://user-images.githubusercontent.com/75033878/112982932-f80fd680-9154-11eb-804c-b6cc4160b63d.png)

## Navigation

Navigation within the application is done through buttons. 


- Click To Login : This button checks the entry box above for the correct password and will change the frame to the Main Page if the password is correct. If the Password is incorrect the the user will be presented with an error message stating that and "Incorrect Password Has Been Entered".

- Sign Out : Each page apart from the splash and the login have a "Sign Out" button which is always located in the bottom left hand of the screen, upon clicking this button the user will be sent back to the login page and have to re-enter their password to gain access.

- Buggy Control & Base Control : These are two buttons bring you to their respective pages that share similar properties and widgets, they are distinguishable by the text on the button that displays the name. Both of these Pages includes a "Sign Out" button and a "Back to Main Page" button.

- Network Status & System Status : These two pages are also similar and work the same way each having an independant button that takes you to the assigned page, they are distinguishable by the text on the button that displays the name. Both of these Pages includes a "Sign Out" button and a "Back to Main Page" button.

- Back To Main Page : This button is on the Four main functionality pages, this button will return the user to the main control page and allows the to then select another page to goto.

- Report Issue : This button is included on the four main functionality pages, when clicked it will produce a new window ontop of the current window with a form that the user can fill out to breifly report an issue they're having with the application.

- Emergency : This Button would have been used with hardware functionality as a measure to ensure safety of the system when something wrong occurs, in the current GUI application it has no use.

## Code
### Python
To allow the GUI to seamlessly Change pages a function was implemented within the app class that stored a list of values. This function could later be called with a value to update the current frame to a new frame, meaning that pages could be assigned as their own classes with initialisers so that when the frame is changed to that class they would load their widgets and functions. An example of this code is show below
    
    # Assign a list within class app with name frames.
            self.frames = {}
            # Store the class names of the pages as values in the list of frames.
        for F in (SplashPage, LoginPage, MainPage, BuggyControlPage,BaseControlPage, NetworkStatusPage, SystemStatusPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Load the first page
        self.show_frame(SplashPage)

    # Change to the desired frame by using tkraise to bring that frame to the front of all frames.
    def show_frame(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()



