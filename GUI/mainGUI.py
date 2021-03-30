# Author Regan Smith
# Version 3.0
# Date 29/03/2021

# libraries
import tkinter as tk
# Main Window, Here we define a page/window that will contain all our other pages, allowing us to store the names of
# pages in a list so that we can sort through them from within each other.
class App(tk.Tk):
    # initialise the page as tk which is of type tkinter.
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,*kwargs)
        # Configure Window
        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SplashPage, LoginPage, MainPage, BuggyControlPage,BaseControlPage, NetworkStatusPage, SystemStatusPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SplashPage)

    # this is how we change to the desired frame by using tkraise to bring that frame to the front of all frames.
    def show_frame(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()
# defining a new page as a class so that they can be stored within the app class.
class SplashPage(tk.Frame): # This is the first page in the list and is our splash screen.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #setting the name and icon of the window
        self.controller.title('ACE MARS PROJECT')
        # set the size and where the app appears
        app_width = 600
        app_height = 800
        self.controller.geometry(f'{app_width}x{app_height}+{740}+{100}')
        self.controller.iconphoto(False, tk.PhotoImage(file='icon.png'))

        background_image = tk.PhotoImage(file="background.png")
        background_label = tk.Label(image=background_image)
        background_label.place(x=-1, y=-1, anchor="nw", )
        background_label.image = background_image

        logo_image = tk.PhotoImage(file="splashlogo.png")
        logo_label = tk.Label(image=logo_image)
        logo_label.place(y=550)
        logo_label.image = logo_image

        # Uses 3 second delay to clear current page and changes to the login page.
        parent.after(3000, background_label.destroy)
        parent.after(3000, logo_label.destroy)
        parent.after(3001, lambda:controller.show_frame(LoginPage))

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Widgets
        title_login_page = tk.Label(self, text="WECLOME TO THE ACE MARS PROGRAM \n Please Login", font=("Helvetica",20))
        title_login_page.pack(padx=10,pady=150)
        # Incorrect Password Label
        wrong_password_label = tk.Label(self, text="Please Enter Password", font=(16))
        wrong_password_label.pack(padx=10, pady=10)
        # Password Entry
        current_password = tk.StringVar()
        login_page_entry = tk.Entry(self, textvariable=current_password)
        login_page_entry.pack(ipadx=50,ipady=5)
        # This password Allows for the use of stars inplace of characters when entering data into the password entry
        def safe_password(_):
            login_page_entry.config(show="*")
        login_page_entry.bind("<FocusIn>",safe_password)

        def password_check():
            if current_password.get() == "mars":
                current_password.set('')
                wrong_password_label['text']=""
                controller.show_frame(MainPage)
            else:
                wrong_password_label['text']='Password Incorrect, Please enter a Valid Password'

        # Page Change Button
        goto_main_page = tk.Button(self,text="Click To Login",font=(16), command=password_check)
        goto_main_page.pack(pady=5)

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Frame to hold first two buttons and Page title
        top_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        top_frame.pack(fill="x", side="top")
        title_login_page = tk.Label(top_frame, text="Main Control page \n Please Choose and option.", font=("Helvetica",22))
        title_login_page.pack(side="top",padx=10,pady=10)
        goto_buggy_control = tk.Button(top_frame, text="Buggy Control", width=37, height=16, padx=5,pady=5,bg="#006bb3",
                                        command=lambda:controller.show_frame(BuggyControlPage))
        goto_buggy_control.pack(side="left") # Button to Go to Buggy Control Page
        goto_base_control = tk.Button(top_frame, text="Base Control", width=37, height=16, padx=5,pady=5,bg="#006bb3",
                                      command=lambda:controller.show_frame(BaseControlPage))
        goto_base_control.pack(side="right") # Button to goto Base Control Page
        # Frame to hold second set of buttons
        middle_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        middle_frame.pack(fill="x")
        goto_network_status = tk.Button(middle_frame, text="Network Status", width=37, height=16, padx=5,pady=5,bg="#006bb3",
                                        command=lambda: controller.show_frame(NetworkStatusPage))
        goto_network_status.pack(side="left") # Button to goto Network Status Page
        goto_system_status = tk.Button(middle_frame, text="System Status", width=37, height=16, padx=5,pady=5,bg="#006bb3",
                                       command=lambda: controller.show_frame(SystemStatusPage))
        goto_system_status.pack(side="right") # Button to goto System Status Page
        # Frame to hold sign out button at the bottom
        bottom_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        bottom_frame.pack(fill="x",side="bottom")
        goto_login_page = tk.Button(bottom_frame, text="Sign Out", command=lambda: controller.show_frame(LoginPage))
        goto_login_page.pack(side="left")

class BuggyControlPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # code for submit report feature
        def submit_report():
            report_form.destroy()

        def report_issue():
            global report_form
            report_form = tk.Toplevel(self)
            report_form.title("Report An Issue")
            report_form.geometry("350x235")
            report_form.config(bg="grey")
            report_form_label = tk.Label(report_form, text="Please Enter Details About Your Issue", bg="grey")
            report_form_label.pack(side="top")
            report_date_label = tk.Label(report_form, text="Please Enter The Date : DD/MM/YY", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=10)
            report_date_label = tk.Label(report_form, text="Please Briefly Explain The Issue", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=50)
            report_name_label = tk.Label(report_form, text="Please Enter Your Name \n 'First , Last'", bg="grey")
            report_name_label.pack(side="top")
            report_name_entry = tk.Entry(report_form)
            report_name_entry.pack(ipadx=80)
            report_email_label = tk.Label(report_form, text="Please Enter Your email", bg="grey")
            report_email_label.pack(side="top")
            report_email_entry = tk.Entry(report_form)
            report_email_entry.pack(ipadx=80)
            report_close_button = tk.Button(report_form, text="Submit Report", command=submit_report)
            report_close_button.pack(side="bottom")

        # implementation of pop up message for both objects and locations being marked
        def kill_location():
            mark_location_label.after(10, mark_location_label.pack_forget())

        def mark_location():
            global mark_location_label
            mark_location_label = tk.Label(bottom_frame, text="Location Marked",font=("Helvetica",16))
            mark_location_label.pack(side="top")
            mark_location_label.after(3000, kill_location)

        def kill_object():
            mark_object_label.after(10, mark_object_label.pack_forget())

        def mark_object():
            global mark_object_label
            mark_object_label = tk.Label(bottom_frame, text="Object Marked",font=("Helvetica",16))
            mark_object_label.pack(side="top")
            mark_object_label.after(3000, kill_object)

        # this top frame is where we will contain our live video feed from opencv
        top_frame = tk.LabelFrame(self, borderwidth=3,padx=10, pady=170)
        top_frame.pack(fill="x", side="top")
        video_feed_label = tk.Label(top_frame, text="VIDEO FEED IS NOT CURRENT AVAIlABLE")
        video_feed_label.pack()
        load_video = tk.Button(top_frame, text="Click to Load Video Connection")
        load_video.pack()
        page_title_label = tk.Label(top_frame, text="BUGGY CONTROL", font=("Helvetica",16))
        page_title_label.pack(side="top", pady=5)

        # this frame hold all the buttons at the bottom right side of the screen
        right_frame = tk.LabelFrame(self,borderwidth=3,padx=30, pady=10)
        right_frame.pack(side="right", fill="y")
        connection_label = tk.Label(right_frame,text="Current Connection is :\nOffline",padx=5, pady=5)
        connection_label.pack(fill="x",pady=10)
        emergency_button = tk.Button(right_frame, text="EMERGENCY",bg="red",padx=5, pady=5)
        emergency_button.pack(fill="x",pady=15)
        report_issue_button = tk.Button(right_frame, text="Report Issue",padx=5, pady=5, command=report_issue)
        report_issue_button.pack(fill="x",pady=15)
        mark_location = tk.Button(right_frame, text="Mark Location",padx=5, pady=5, command=mark_location)
        mark_location.pack(fill="x",pady=15)
        mark_object = tk.Button(right_frame, text="Mark Object",padx=5, pady=5,command=mark_object)
        mark_object.pack(fill="x",pady=15)

        # Frame to hold second set of buttons
        middle_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        middle_frame.pack(fill="x")
        right_control = tk.Button(middle_frame, text="Movement Control", width=25, height=10, padx=5,pady=5)
        right_control.pack(side="right") # Button to goto System Status Page
        left_control = tk.Button(middle_frame, text="Camera Control", width=25, height=10, padx=5,pady=5)
        left_control.pack(side="left") # Button to goto Network Status Page

        # Frame to hold sign out and go back buttons at the bottom
        bottom_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        bottom_frame.pack(fill="x",side="bottom")
        goto_login_page = tk.Button(bottom_frame, text="Sign Out", command=lambda: controller.show_frame(LoginPage))
        goto_login_page.pack(side="left")
        goto_main_page = tk.Button(bottom_frame,text="Back to Main Page", command=lambda: controller.show_frame(MainPage))
        goto_main_page.pack(padx=15,side="left")

class BaseControlPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        # this top frame is where we will contain our live video feed from opencv
        top_frame = tk.LabelFrame(self, borderwidth=3,padx=10, pady=170)
        top_frame.pack(fill="x", side="top")
        video_feed_label = tk.Label(top_frame, text="VIDEO FEED IS NOT CURRENT AVAIlABLE")
        video_feed_label.pack()
        load_video = tk.Button(top_frame, text="Click to Load Video Connection")
        load_video.pack()
        page_title_label = tk.Label(top_frame, text="MAIN BASE CONTROL", font=("Helvetica",16))
        page_title_label.pack(side="top", pady=10)

        # implementation of pop up message for both objects and locations being marked
        def kill_request():
            request_pickup_label.after(10, request_pickup_label.pack_forget())

        def request_pickup():
            global request_pickup_label
            request_pickup_label = tk.Label(bottom_frame, text="Pickup Requested",font=("Helvetica",16))
            request_pickup_label.pack(side="top")
            request_pickup_label.after(3000, kill_request)

        def kill_object():
            mark_object_label.after(10, mark_object_label.pack_forget)

        def mark_object():
            global mark_object_label
            mark_object_label = tk.Label(bottom_frame, text="Object Marked",font=("Helvetica",16))
            mark_object_label.pack(side="top")
            mark_object_label.after(3000, kill_object)

        # code for submit report feature
        def submit_report():
            report_form.destroy()

        def report_issue():
            global report_form
            report_form = tk.Toplevel(self)
            report_form.title("Report An Issue")
            report_form.geometry("350x235")
            report_form.config(bg="grey")
            report_form_label = tk.Label(report_form, text="Please Enter Details About Your Issue", bg="grey")
            report_form_label.pack(side="top")
            report_date_label = tk.Label(report_form, text="Please Enter The Date : DD/MM/YY", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=10)
            report_date_label = tk.Label(report_form, text="Please Briefly Explain The Issue", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=50)
            report_name_label = tk.Label(report_form, text="Please Enter Your Name \n 'First , Last'", bg="grey")
            report_name_label.pack(side="top")
            report_name_entry = tk.Entry(report_form)
            report_name_entry.pack(ipadx=80)
            report_email_label = tk.Label(report_form, text="Please Enter Your email", bg="grey")
            report_email_label.pack(side="top")
            report_email_entry = tk.Entry(report_form)
            report_email_entry.pack(ipadx=80)
            report_close_button = tk.Button(report_form, text="Submit Report", command=submit_report)
            report_close_button.pack(side="bottom")


        # this frame hold all the buttons at the bottom right side of the screen
        right_frame = tk.LabelFrame(self,borderwidth=3,padx=30, pady=10)
        right_frame.pack(side="right", fill="y")
        connection_label = tk.Label(right_frame,text="Current Connection is :\nOffline",padx=5, pady=5)
        connection_label.pack(fill="x",pady=10)
        emergency_button = tk.Button(right_frame, text="EMERGENCY",bg="red",padx=5, pady=5)
        emergency_button.pack(fill="x",pady=15)
        report_issue_button = tk.Button(right_frame, text="Report Issue",padx=5, pady=5, command=report_issue)
        report_issue_button.pack(fill="x",pady=15)
        request_pickup = tk.Button(right_frame, text="Request Pickup",padx=5, pady=5, command=request_pickup)
        request_pickup.pack(fill="x",pady=15)
        mark_object = tk.Button(right_frame, text="Mark Object",padx=5, pady=5, command=mark_object)
        mark_object.pack(fill="x",pady=15)

        # Frame to hold second set of buttons
        middle_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        middle_frame.pack(fill="x")
        right_control = tk.Button(middle_frame, text="Movement Control", width=25, height=10, padx=5,pady=5)
        right_control.pack(side="right") # Button to goto System Status Page
        left_control = tk.Button(middle_frame, text="Camera Control", width=25, height=10, padx=5,pady=5)
        left_control.pack(side="left") # Button to goto Network Status Page

        # Frame to hold sign out and go back buttons at the bottom
        bottom_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        bottom_frame.pack(fill="x",side="bottom")
        goto_login_page = tk.Button(bottom_frame, text="Sign Out", command=lambda: controller.show_frame(LoginPage))
        goto_login_page.pack(side="left")
        goto_main_page = tk.Button(bottom_frame,text="Back to Main Page", command=lambda: controller.show_frame(MainPage))
        goto_main_page.pack(padx=15,side="left")

class NetworkStatusPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            # code for submit report feature
            def submit_report():
                report_form.destroy()

            def report_issue():
                global report_form
                report_form = tk.Toplevel(self)
                report_form.title("Report An Issue")
                report_form.geometry("350x235")
                report_form.config(bg="grey")
                report_form_label = tk.Label(report_form, text="Please Enter Details About Your Issue", bg="grey")
                report_form_label.pack(side="top")
                report_date_label = tk.Label(report_form, text="Please Enter The Date : DD/MM/YY", bg="grey")
                report_date_label.pack(side="top")
                report_date_entry = tk.Entry(report_form)
                report_date_entry.pack(ipadx=10)
                report_date_label = tk.Label(report_form, text="Please Briefly Explain The Issue", bg="grey")
                report_date_label.pack(side="top")
                report_date_entry = tk.Entry(report_form)
                report_date_entry.pack(ipadx=50)
                report_name_label = tk.Label(report_form, text="Please Enter Your Name \n 'First , Last'", bg="grey")
                report_name_label.pack(side="top")
                report_name_entry = tk.Entry(report_form)
                report_name_entry.pack(ipadx=80)
                report_email_label = tk.Label(report_form, text="Please Enter Your email", bg="grey")
                report_email_label.pack(side="top")
                report_email_entry = tk.Entry(report_form)
                report_email_entry.pack(ipadx=80)
                report_close_button = tk.Button(report_form, text="Submit Report", command=submit_report)
                report_close_button.pack(side="bottom")

            # this top frame is where we will contain our live video feed from opencv
            top_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
            top_frame.pack(fill="x", side="top")
            page_title_label = tk.Label(top_frame, text="Network System Control", font=("Helvetica", 26))
            page_title_label.pack(side="top", pady=10)
            network_status_label = tk.Label(top_frame, text="Network Status is Currently",font=("Helvetica",14))
            network_status_label.pack()
            current_status_label = tk.Label(top_frame, text="OFFLINE",fg="red", font=("Helvetica",20))
            current_status_label.pack()
            page_description = tk.Label(top_frame,
                                        text="This page is used to represent data\n relating to the network and its "
                                             "current connection,\n As well as troubleshoot network problems",
                                        font=("Helvetica", 12))
            page_description.pack(side="bottom", pady=25)


            # this frame hold all the buttons at the bottom right side of the screen
            right_frame = tk.LabelFrame(self, borderwidth=3, padx=30, pady=10)
            right_frame.pack(fill="y",side="right")
            report_issue_button = tk.Button(right_frame, text="Report Issue", padx=5, pady=5, command=report_issue)
            report_issue_button.pack(fill="x",side="bottom", pady=15)
            emergency_button = tk.Button(right_frame, text="EMERGENCY", bg="red", padx=5, pady=5)
            emergency_button.pack(side="bottom",fill="x", pady=15)



            # Frame to hold second set of buttons
            middle_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
            middle_frame.pack(fill="x")
            lan_control = tk.Button(middle_frame, text="LAN CONTROL", padx=5, pady=5)
            lan_control.pack(side="left", padx=5)  # Button to goto System Status Page

            wan_control = tk.Button(middle_frame, text="WAN CONTROL", padx=5, pady=5)
            wan_control.pack(side="left", padx=5)  # Button to goto Network Status Page


            # Frame to hold sign out and go back buttons at the bottom
            bottom_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
            bottom_frame.pack(fill="x", side="bottom")
            goto_login_page = tk.Button(bottom_frame, text="Sign Out", command=lambda: controller.show_frame(LoginPage))
            goto_login_page.pack(side="left")
            goto_main_page = tk.Button(bottom_frame, text="Back to Main Page",
                                       command=lambda: controller.show_frame(MainPage))
            goto_main_page.pack(padx=15, side="left")

class SystemStatusPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # code for submit report feature
        def submit_report():
            report_form.destroy()

        def report_issue():
            global report_form
            report_form = tk.Toplevel(self)
            report_form.title("Report An Issue")
            report_form.geometry("350x235")
            report_form.config(bg="grey")
            report_form_label = tk.Label(report_form, text="Please Enter Details About Your Issue", bg="grey")
            report_form_label.pack(side="top")
            report_date_label = tk.Label(report_form, text="Please Enter The Date : DD/MM/YY", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=10)
            report_date_label = tk.Label(report_form, text="Please Briefly Explain The Issue", bg="grey")
            report_date_label.pack(side="top")
            report_date_entry = tk.Entry(report_form)
            report_date_entry.pack(ipadx=50)
            report_name_label = tk.Label(report_form, text="Please Enter Your Name \n 'First , Last'", bg="grey")
            report_name_label.pack(side="top")
            report_name_entry = tk.Entry(report_form)
            report_name_entry.pack(ipadx=80)
            report_email_label = tk.Label(report_form, text="Please Enter Your email", bg="grey")
            report_email_label.pack(side="top")
            report_email_entry = tk.Entry(report_form)
            report_email_entry.pack(ipadx=80)
            report_close_button = tk.Button(report_form, text="Submit Report", command=submit_report)
            report_close_button.pack(side="bottom")

        # this top frame is where we will contain our live video feed from opencv
        top_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        top_frame.pack(fill="x", side="top")
        page_title_label = tk.Label(top_frame, text= "Systems Control", font=("Helvetica", 26))
        page_title_label.pack(side="top", pady=10)
        network_status_label = tk.Label(top_frame, text="System Status is Currently", font=("Helvetica", 14))
        network_status_label.pack()
        current_status_label = tk.Label(top_frame, text="OFFLINE", fg="red", font=("Helvetica", 20))
        current_status_label.pack()
        page_description = tk.Label(top_frame, text="This page is used to represent data\n and help to test the current "
                                                    "systems of the rover", font=("Helvetica", 12))
        page_description.pack(side="bottom", pady=25)

        # this frame hold all the buttons at the bottom right side of the screen
        right_frame = tk.LabelFrame(self, borderwidth=3, padx=30, pady=10)
        right_frame.pack(fill="y", side="right")
        report_issue_button = tk.Button(right_frame, text="Report Issue", padx=5, pady=5 ,command=report_issue)
        report_issue_button.pack(fill="x", side="bottom", pady=15)
        emergency_button = tk.Button(right_frame, text="EMERGENCY", bg="red", padx=5, pady=5)
        emergency_button.pack(side="bottom", fill="x", pady=15)

        # Frame to hold second set of buttons
        middle_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        middle_frame.pack(fill="x")
        battery_test = tk.Button(middle_frame, text="Battery Level", padx=5, pady=5)
        battery_test.pack(side="left", padx=5)  # Button to goto System Status Page

        weight_test = tk.Button(middle_frame, text="Current Weight", padx=5, pady=5)
        weight_test.pack(side="left", padx=5)  # Button to goto Network Status Page

        # Frame to hold sign out and go back buttons at the bottom
        bottom_frame = tk.LabelFrame(self, borderwidth=3, padx=10, pady=10)
        bottom_frame.pack(fill="x", side="bottom")
        goto_login_page = tk.Button(bottom_frame, text="Sign Out", command=lambda: controller.show_frame(LoginPage))
        goto_login_page.pack(side="left")
        goto_main_page = tk.Button(bottom_frame, text="Back to Main Page",
                                   command=lambda: controller.show_frame(MainPage))
        goto_main_page.pack(padx=15, side="left")

app = App()

app.mainloop()