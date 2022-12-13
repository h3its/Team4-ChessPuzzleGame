from main import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
from db import ChessDB
from service import InvalidLoginException, UserNotFoundException, ChessService


class Login:

    def __init__(self, service, LWIN):
        self.service = service
        self.LWIN = LWIN
        # Size of display Window
        self.LWIN.geometry('460x460')
        # Prohibits resizing of the Window
        self.LWIN.resizable(0, 0)
        # Names the title bar
        self.LWIN.title('Login')
        # Sets Window as a 460 by 460 frame
        self.login_window = Frame(
            self.LWIN, bg='black', width='460', height='460')

        # Fills frame with black
        self.login_window.pack(fill='both', expand='yes')

        ####### TITLE #########
        # Sets title background to green
        self.title_bg = Label(
            self.login_window, bg='#779556')
        # Fills frame
        self.title_bg.pack(ipadx=20, ipady=50, fill=X, expand="yes", anchor=N)
        # Creates Title label and sets placement
        self.title_label = Label(self.login_window, text='Chess Puzzle Game',
                                 bg='#779556', fg='white', font=('comic sans', 25, 'bold'))
        self.title_label.place(x=72, y=45)
        # Adds queen images on left side of the Title label
        self.queen_image1 = Image.open('assets/queen.png')
        resize_queen = self.queen_image1.resize((64, 64))
        queen_photo = ImageTk.PhotoImage(resize_queen)
        self.left_image_label = Label(
            self.login_window, image=queen_photo)
        self.left_image_label.image = queen_photo
        self.left_image_label.place(x=5, y=25)
        # Adds queen images on right side of the Title label
        self.right_image_label = Label(
            self.login_window, image=queen_photo, bg='white')
        self.right_image_label.image = queen_photo
        self.right_image_label.place(x=386, y=25)

        # Creates login label and sets placement
        self.login_label = Label(self.login_window, text='Login',
                                 bg='black', fg='white', font=('comic sans', 17, 'bold'))
        self.login_label.place(x=200, y=150)

        # Creates username label and sets placement
        self.email_label = Label(
            self.login_window, text='Email', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.email_label.place(x=75, y=210)
        self.email_entry = Entry(self.login_window, highlightthickness=0,
                                 relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'))
        self.email_entry.place(x=140, y=210, width=200)

        # Creates password label and sets placement
        self.password_label = Label(
            self.login_window, text='Password', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.password_label.place(x=40, y=250)
        self.password_entry = Entry(self.login_window, highlightthickness=0,
                                    relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'), show='*')
        self.password_entry.place(x=140, y=250, width=200)

        # SHOW AND HIDE PASSWORD #
        # Sets the "Hide Password" image and labels for the "Show" function
        self.show_image = Image.open('assets/Hide.png')
        self.show_photo = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(
            self.login_window, image=self.show_photo, bg='black', activebackground='black', cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.show_photo
        self.show_button.place(x=345, y=255)
        self.login_label1 = Label(self.login_window, text='Show',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label1.place(x=360, y=240)
        self.login_label2 = Label(self.login_window, text='Password',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label2.place(x=360, y=255)

        # "Show Password" image
        self.hide_image = Image.open('assets/Show.png')
        self.hide_photo = ImageTk.PhotoImage(self.hide_image)

        # Sets an image for the login button and sets placement
        self.button_image = Image.open('assets/LoginButtonImage.png')
        button_photo = ImageTk.PhotoImage(self.button_image)
        self.login_button_label = Label(
            self.login_window, image=button_photo, bg='black')
        self.login_button_label.image = button_photo
        self.login_button_label.place(x=125, y=295)

        # Creates a login button and sets placement
        self.login_button = Button(self.login_button_label, text='LOGIN', font=(
            'comic sans', 13, 'bold'), width=20, bd=0, bg='#779556', cursor='hand2', activebackground='#779556', fg='white', command=self.login_submit)
        self.login_button.place(x=12, y=10)

        # Creates a forgot password link
        self.forgot_button = Button(self.login_window, text='Forgot Password?', font=(
            'comic sans', 8, 'bold italic underline'), fg='grey', width=15, bd=0, bg='black', activebackground='black', cursor='hand2', command=self.forget_password)
        self.forgot_button.place(x=240, y=355)

        # Creates a sign up password link
        self.create_button = Button(self.login_window, text='Create Account', font=(
            'comic sans', 8, 'bold italic underline'), fg='grey', width=15, bd=0, bg='black', activebackground='black', cursor='hand2', command=self.create_account)
        self.create_button.place(x=110, y=355)

        # Creates a skip link
        self.skip_button = Button(self.login_window, text='Skip for Now', font=(
            'comic sans', 10, 'bold underline'), fg='grey', width=15, bd=0, bg='black', activebackground='black', cursor='hand2', command=self.skip)
        self.skip_button.place(x=170, y=400)

    ######### FUNCTIONS #########

    # Displays password characters and switches button to the "hide" button

    def show(self):
        self.hide_button = Button(self.login_window, image=self.hide_photo,
                                  bg='black', activebackground='black', cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.hide_photo
        self.hide_button.place(x=345, y=255)
        self.password_entry.config(show='')
        self.login_label1 = Label(self.login_window, text='Hide   ',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label1.place(x=360, y=240)
        self.login_label2 = Label(self.login_window, text='Password',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label2.place(x=360, y=255)

    # Hides password characters amongst asterisks and switches button to the "show" button
    def hide(self):
        self.show_button = Button(
            self.login_window, image=self.show_photo, bg='black', activebackground='black', cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.show_photo
        self.show_button.place(x=345, y=255)
        self.password_entry.config(show='*')
        self.login_label1 = Label(self.login_window, text='Show',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label1.place(x=360, y=240)
        self.login_label2 = Label(self.login_window, text='Password',
                                  bg='black', fg='white', font=('comic sans', 8, 'bold'))
        self.login_label2.place(x=360, y=255)

    # Allows user to skip the sign-up/login process and go directly to the game
    def skip(self):
        self.show_button = Button(
            self.login_window, image=self.show_photo, bg='black', activebackground='black', cursor='hand2', bd=0, command=LWIN.withdraw())
        """Opens the game"""
        main(self.service, None)
        LWIN.quit()

    # Allows user to create a new password

    def forget_password(self):
        # Creates the forgot password window itself
        self.forget_window = Toplevel()
        self.forget_window.geometry('460x460')
        self.forget_window.title('Forgot Password')
        self.forget_window.config(background='black')
        self.forget_window.resizable(0, 0)
        ####### TITLE #########
        # Sets title background to green
        self.title3_bg = Label(
            self.forget_window, bg='#779556')
        # Fills frame
        self.title3_bg.pack(ipadx=20, ipady=50, fill=X, expand="yes", anchor=N)
        # Creates Title label and sets placement
        self.title3_label = Label(self.forget_window, text='Chess Puzzle Game',
                                  bg='#779556', fg='white', font=('comic sans', 25, 'bold'))
        self.title3_label.place(x=72, y=45)
        # Adds queen images on left side of the Title label
        self.queen_image1 = Image.open('assets/queen.png')
        resize_queen = self.queen_image1.resize((64, 64))
        queen_photo = ImageTk.PhotoImage(resize_queen)
        self.left_image_label = Label(
            self.forget_window, image=queen_photo)
        self.left_image_label.image = queen_photo
        self.left_image_label.place(x=5, y=25)
        # Adds queen images on right side of the Title label
        self.right_image_label = Label(
            self.forget_window, image=queen_photo, bg='white')
        self.right_image_label.image = queen_photo
        self.right_image_label.place(x=386, y=25)
        # Creates Forgot Password Title
        self.ftitle_label = Label(
            self.forget_window, text='Forget Password?', bg='black', fg='grey', font=('comic sans', 17, 'bold'))
        self.ftitle_label.place(x=130, y=140)
        self.ftitle_label = Label(
            self.forget_window, text='Create a new password down below', bg='black', fg='grey', font=('comic sans', 15, 'bold'))
        self.ftitle_label.place(x=60, y=180)
        #######Creates entry fields for the user########
        # Creates the email label and entry field
        self.email_label = Label(
            self.forget_window, text='Email', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.email_label.place(x=143, y=240)
        self.email_entry = Entry(self.forget_window, highlightthickness=0,
                                 relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'))
        self.email_entry.place(x=200, y=240, width=200)
        # Creates the new password label and entry field
        self.password_label = Label(
            self.forget_window, text='New Password', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.password_label.place(x=68, y=280)
        self.password_entry = Entry(self.forget_window, highlightthickness=0,
                                    relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'), show='*')
        self.password_entry.place(x=200, y=280, width=200)
        # Creates the confirm password label and entry field
        self.confirm_label = Label(
            self.forget_window, text='Confirm Password', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.confirm_label.place(x=40, y=320)
        self.confirm_entry = Entry(self.forget_window, highlightthickness=0,
                                   relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'), show='*')
        self.confirm_entry.place(x=200, y=320, width=200)
        # Sets Submit button image
        self.submit1_image = Image.open('assets/LoginButtonImage.png')
        submit1_photo = ImageTk.PhotoImage(self.submit1_image)
        self.submit1_button_label = Label(
            self.forget_window, image=submit1_photo, bg='black')
        self.submit1_button_label.image = submit1_photo
        self.submit1_button_label.place(x=180, y=370)
        # Creates a submit button and sets placement
        self.submit1_button = Button(self.submit1_button_label, text='SUBMIT', font=(
            'comic sans', 13, 'bold'), width=20, bd=0, bg='#779556', cursor='hand2', activebackground='#779556', fg='white')
        self.submit1_button.place(x=12, y=10)

    # TODO: implement this jawn and wire it up to some button ...
    # def login(self, yyy)

    def create_account(self):
        # TODO: somewhere here self.service.signup(xxxxx)
        # Creates the create account window itself
        # print("CREATE ACCOUNT")
        self.create_window = Toplevel()
        self.create_window.geometry('460x460')
        self.create_window.title('Create Account')
        self.create_window.config(background='black')
        self.create_window.resizable(0, 0)
        # Creates create account Title
        self.create_label = Label(
            self.create_window, text='Create Account', bg='black', fg='grey', font=('comic sans', 17, 'bold'))
        self.create_label.place(x=135, y=165)
        ####### TITLE #########
        # Sets title background to green
        self.title_bg = Label(
            self.create_window, bg='#779556')
        # Fills frame
        self.title_bg.pack(ipadx=20, ipady=50, fill=X, expand="yes", anchor=N)
        # Creates Title label and sets placement
        self.title_label = Label(self.create_window, text='Chess Puzzle Game',
                                 bg='#779556', fg='white', font=('comic sans', 25, 'bold'))
        self.title_label.place(x=72, y=45)
        # Adds queen images on left side of the Title label
        self.queen_image1 = Image.open('assets/queen.png')
        resize_queen = self.queen_image1.resize((64, 64))
        queen_photo = ImageTk.PhotoImage(resize_queen)
        self.left_image_label = Label(
            self.create_window, image=queen_photo)
        self.left_image_label.image = queen_photo
        self.left_image_label.place(x=5, y=25)
        # Adds queen images on right side of the Title label
        self.right_image_label = Label(
            self.create_window, image=queen_photo, bg='white')
        self.right_image_label.image = queen_photo
        self.right_image_label.place(x=386, y=25)
        #######Creates entry fields for the user########
        # Creates the email label and entry field
        # self.email_label = Label(
        #    self.create_window, text='Email', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        # self.email_label.place(x=143, y=160)
        # self.email_entry = Entry(self.create_window, highlightthickness=0,
        #                         relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'))
        # self.email_entry.place(x=200, y=160, width=200)
        # Creates the email label and entry field
        self.email_label = Label(
            self.create_window, text='Email', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.email_label.place(x=142, y=240)
        self.email_entry = Entry(self.create_window, highlightthickness=0,
                                 relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'))
        self.email_entry.place(x=200, y=240, width=200)
        # Creates the new password label and entry field
        self.password_label = Label(
            self.create_window, text='New Password', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.password_label.place(x=68, y=280)
        self.password_entry = Entry(self.create_window, highlightthickness=0,
                                    relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'), show='*')
        self.password_entry.place(x=200, y=280, width=200)
        # Creates the confirm password label and entry field
        self.confirm_label = Label(
            self.create_window, text='Confirm Password', bg='black', fg='grey', font=('comic sans', 13, 'bold'))
        self.confirm_label.place(x=40, y=320)
        self.confirm_entry = Entry(self.create_window, highlightthickness=0,
                                   relief=FLAT, bg='white', fg='black', font=('comic sans', 13, 'bold'), show='*')
        self.confirm_entry.place(x=200, y=320, width=200)
        # Sets Submit button image
        self.submit2_image = Image.open('assets/LoginButtonImage.png')
        submit2_photo = ImageTk.PhotoImage(self.submit2_image)
        self.submit2_button_label = Label(
            self.create_window, image=submit2_photo, bg='black')
        self.submit2_button_label.image = submit2_photo
        self.submit2_button_label.place(x=180, y=370)
        # Creates a submit button and sets placement
        self.submit2_button = Button(self.submit2_button_label, text='SUBMIT', font=(
            'comic sans', 13, 'bold'), width=20, bd=0, bg='#779556', cursor='hand2', activebackground='#779556', fg='white',
            command=self.create_account_submit)
        self.submit2_button.place(x=12, y=10)

    def login_submit(self):
        # self.service.login -> handle the InvalidLoginException
        if self.username_entry.get() == '' or self.password_entry.get() == '':
            return

        try:
            email = self.username_entry.get()
            password = self.password_entry.get()
            self.service.login(email, password)
            print("LOGIN SUCCESSFUL!!!")
            main(self.service, email)
            LWIN.quit()
        except InvalidLoginException:
            messagebox.showerror('Login Failed', 'Login failed!')
            print("LOGIN FAILED!!!")

    def create_account_submit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        password2 = self.confirm_entry.get()

        if password != password2:
            messagebox.showerror('Error', 'Passwords do not match!')
        elif email in service.get_users():
            messagebox.showerror('Error', 'Email already in use!')
        else:
            self.service.signup(email, password)
            self.create_window.destroy()


db = ChessDB(dbname="postgres", user="postgres",
             password="example", host="localhost", port=5432)
service = ChessService(db)
LWIN = Tk()
Login(service, LWIN)
LWIN.mainloop()