#!/usr/bin/python3
import tkinter as tk
from random import randint
from tkinter import messagebox
from backend import *


class ManagerApp:
    def __init__(self, master=None):
        # build ui

        # Home Page GUI Frame
        self.bgFrame = tk.Frame(master, container="false")
        self.bgFrame.configure(background="#006747", height=480, width=854)
        self.homeFrame = tk.Frame(self.bgFrame)
        self.homeFrame.configure(background="#eeeeee", height=200, width=200)
        self.titleHome = tk.Label(self.homeFrame)
        self.titleHome.configure(
            font="{Raleway} 24 {bold}",
            text='Password Manager')
        self.titleHome.place(anchor="n", relx=0.5, rely=0.05, x=0, y=0)
        self.genNavButton = tk.Button(self.homeFrame, command=lambda: self.genFrame.tkraise())
        self.genNavButton.configure(
            background="#006747",
            foreground="#ffffff",
            font="{Raleway} 12 {bold}",
            text='Generate or Store\nPasswords')
        self.genNavButton.place(
            anchor="center",
            height=250,
            relx=0.35,
            rely=0.5,
            width=200,
            x=0,
            y=0)
        self.retrNavButton = tk.Button(self.homeFrame, command=lambda: self.retrFrame.tkraise())
        self.retrNavButton.configure(
            background="#006747",
            foreground="#ffffff",
            font="{Raleway} 12 {bold}",
            text='Retrieve\nPasswords')
        self.retrNavButton.place(
            anchor="center",
            height=250,
            relx=0.65,
            rely=0.5,
            width=200,
            x=0,
            y=0)
        self.logoutButton = tk.Button(self.homeFrame, command=lambda: self.logout())
        self.logoutButton.configure(
            background="#CFC493",
            font="{Raleway} 12 {bold italic}",
            text='Logout')
        self.logoutButton.place(anchor="center", relx=0.9, rely=0.9, x=0, y=0)
        self.homeFrame.place(
            anchor="center",
            relheight=0.98,
            relwidth=0.98,
            relx=0.5,
            rely=0.5,
            x=0,
            y=0)
        # End Home Page Frame

        # Password Generation GUI Frame
        self.genFrame = tk.Frame(self.bgFrame)
        self.genFrame.configure(height=200, width=200)
        self.titleGenerate = tk.Label(self.genFrame)
        self.titleGenerate.configure(
            font="{Raleway} 24 {bold}",
            text='Generate & Store Passwords')
        self.titleGenerate.place(anchor="n", relx=0.5, rely=0.05, x=0, y=0)
        self.genBackButton = tk.Button(self.genFrame, command=lambda: self.returnHome())
        self.genBackButton.configure(
            background="#CFC493",
            font="{Raleway} 12 {bold italic}",
            text='Back')
        self.genBackButton.place(
            anchor="center",
            relx=0.9,
            rely=0.9,
            width=75,
            x=0,
            y=0)
        self.numCharLabel = tk.Label(self.genFrame)
        self.numCharLabel.configure(
            font="{Raleway} 12 {}",
            text='How many characters? (Max. 64)')
        self.numCharLabel.place(anchor="nw", relx=0.06, rely=0.25, x=0, y=0)
        self.numCharEntry = tk.Entry(self.genFrame)
        self.numCharEntry.place(
            anchor="nw",
            relx=0.17,
            rely=0.31,
            width=30,
            x=0,
            y=0)
        self.genButton = tk.Button(self.genFrame, command=lambda: self.genPassword())
        self.genButton.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Generate')
        self.genButton.place(anchor="nw", relx=0.14, rely=0.37, x=0, y=0)
        self.pwOutput = tk.Entry(self.genFrame, state="disabled")
        self.pwOutput.configure(
            background="#eeeeee",
            borderwidth=0,
            foreground="#000000")
        self.pwOutput.place(
            anchor="nw",
            relx=0.05,
            rely=0.48,
            width=250,
            x=0,
            y=0)
        self.clearGenEntry = tk.Button(self.genFrame, command=lambda: self.clearGenPassword())
        self.clearGenEntry.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Clear')
        self.clearGenEntry.place(
            anchor="nw",
            relx=0.08,
            rely=0.55,
            width=85,
            x=0,
            y=0)
        self.copyGenEntry = tk.Button(self.genFrame, command=lambda: self.copyToClipboard())
        self.copyGenEntry.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Copy')
        self.copyGenEntry.place(
            anchor="nw",
            relx=0.2,
            rely=0.55,
            width=85,
            x=0,
            y=0)
        self.genPasswordTitle = tk.Label(self.genFrame)
        self.genPasswordTitle.configure(
            font="{Raleway} 12 {bold italic}",
            text='Generate Password')
        self.genPasswordTitle.place(anchor="nw", relx=0.1, rely=0.18, x=0, y=0)
        self.storeUsernameEntry = tk.Entry(self.genFrame)
        self.storeUsernameEntry.place(
            anchor="nw", relx=0.75, rely=0.265, x=0, y=0)
        self.storeUsernameLabel = tk.Label(self.genFrame)
        self.storeUsernameLabel.configure(
            font="{Raleway} 12 {}", text='Username:')
        self.storeUsernameLabel.place(
            anchor="nw", relx=0.64, rely=0.25, x=0, y=0)
        self.storePasswordTitle = tk.Label(self.genFrame)
        self.storePasswordTitle.configure(
            font="{Raleway} 12 {bold italic}",
            text='Store Password')
        self.storePasswordTitle.place(
            anchor="nw", relx=0.7, rely=0.18, x=0, y=0)
        self.storeWebsiteLabel = tk.Label(self.genFrame)
        self.storeWebsiteLabel.configure(
            font="{Raleway} 12 {}", text='Website:')
        self.storeWebsiteLabel.place(
            anchor="nw", relx=0.64, rely=0.33, x=0, y=0)
        self.storeWebsiteEntry = tk.Entry(self.genFrame)
        self.storeWebsiteEntry.place(
            anchor="nw", relx=0.75, rely=0.345, x=0, y=0)
        self.storePasswordLabel = tk.Label(self.genFrame)
        self.storePasswordLabel.configure(
            font="{Raleway} 12 {}", text='Password:')
        self.storePasswordLabel.place(
            anchor="nw", relx=0.64, rely=0.41, x=0, y=0)
        self.storePasswordEntry = tk.Entry(self.genFrame)
        self.storePasswordEntry.place(
            anchor="nw", relx=0.75, rely=0.425, x=0, y=0)
        self.storeConfirmPWLabel = tk.Label(self.genFrame)
        self.storeConfirmPWLabel.configure(
            font="{Raleway} 12 {}", text='Confirm Password:')
        self.storeConfirmPWLabel.place(
            anchor="nw", relx=0.56, rely=0.49, x=0, y=0)
        self.storeConfirmPWEntry = tk.Entry(self.genFrame)
        self.storeConfirmPWEntry.place(
            anchor="nw", relx=0.75, rely=0.505, x=0, y=0)
        self.clearStoreEntry = tk.Button(self.genFrame, command=lambda: self.clearStoredInfo())
        self.clearStoreEntry.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Clear')
        self.clearStoreEntry.place(
            anchor="nw",
            relx=0.65,
            rely=0.58,
            width=85,
            x=0,
            y=0)
        self.storeLoginEntry = tk.Button(self.genFrame, command=lambda: self.storePassword())
        self.storeLoginEntry.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Store')
        self.storeLoginEntry.place(
            anchor="nw",
            relx=0.77,
            rely=0.58,
            width=85,
            x=0,
            y=0)
        self.storeSuccessLabel = tk.Label(self.genFrame)
        self.storeSuccessLabel.configure(
            font="{Raleway} 12 {bold italic}",
            text='Login Information Stored!')
        self.storeFailLabel = tk.Label(self.genFrame)
        self.storeFailLabel.configure(
            font="{Raleway} 12 {bold italic}",
            text='Please fill out all fields.')
        self.storeNoPWMatchLabel = tk.Label(self.genFrame)
        self.storeNoPWMatchLabel.configure(
            font="{Raleway} 12 {bold italic}",
            text='Passwords do not match.')
        self.genFrame.place(
            anchor="center",
            relheight=0.98,
            relwidth=0.98,
            relx=0.5,
            rely=0.5,
            x=0,
            y=0)
        # End Generation Frame

        # Password retrieval GUI frame
        self.retrFrame = tk.Frame(self.bgFrame)
        self.retrFrame.configure(height=200, width=200)
        self.titleRetrieve = tk.Label(self.retrFrame)
        self.titleRetrieve.configure(
            font="{Raleway} 24 {bold}",
            text='Retrieve Passwords')
        self.titleRetrieve.place(anchor="n", relx=0.5, rely=0.05, x=0, y=0)
        self.retrBackButton = tk.Button(self.retrFrame, command=lambda: self.returnHome())
        self.retrBackButton.configure(
            background="#CFC493",
            font="{Raleway} 12 {bold italic}",
            text='Back')
        self.retrBackButton.place(
            anchor="center",
            relx=0.9,
            rely=0.9,
            width=75,
            x=0,
            y=0)
        self.clearRetrEntryButton = tk.Button(self.retrFrame, command=lambda: self.clearLoginInfoEntry())
        self.clearRetrEntryButton.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Clear')
        self.clearRetrEntryButton.place(
            anchor="nw", relx=0.13, rely=0.5, width=85, x=0, y=0)
        self.retrPasswordButton = tk.Button(self.retrFrame, command=lambda: self.retrievePassword())
        self.retrPasswordButton.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Retrieve')
        self.retrPasswordButton.place(
            anchor="nw", relx=0.25, rely=0.5, width=85, x=0, y=0)
        self.enterInfoLabel = tk.Label(self.retrFrame)
        self.enterInfoLabel.configure(
            font="{Raleway} 12 {bold italic}",
            text='Enter Login Information')
        self.enterInfoLabel.place(anchor="nw", relx=0.12, rely=0.18, x=0, y=0)
        self.webRetrOutput = tk.Entry(self.retrFrame, state="disabled")
        self.webRetrOutput.configure(background="#eeeeee", borderwidth=0)
        self.webRetrOutput.place(
            anchor="nw",
            relx=0.65,
            rely=0.265,
            width=250,
            x=0,
            y=0)
        self.webEnterLabel = tk.Label(self.retrFrame)
        self.webEnterLabel.configure(font="{Raleway} 12 {}", text='Website:')
        self.webEnterLabel.place(anchor="nw", relx=0.1, rely=0.25, x=0, y=0)
        self.retrLoginLabel = tk.Label(self.retrFrame)
        self.retrLoginLabel.configure(
            font="{Raleway} 12 {bold italic}",
            text='Retrieved Login Information')
        self.retrLoginLabel.place(anchor="nw", relx=0.65, rely=0.18, x=0, y=0)
        self.unEnterLabel = tk.Label(self.retrFrame)
        self.unEnterLabel.configure(font="{Raleway} 12 {}", text='Username:')
        self.unEnterLabel.place(anchor="nw", relx=0.09, rely=0.33, x=0, y=0)
        self.unRetrOutput = tk.Entry(self.retrFrame, state="disabled")
        self.unRetrOutput.configure(background="#eeeeee", borderwidth=0)
        self.unRetrOutput.place(
            anchor="nw",
            relx=0.65,
            rely=0.345,
            width=250,
            x=0,
            y=0)
        self.pwRetrLabel = tk.Label(self.retrFrame)
        self.pwRetrLabel.configure(font="{Raleway} 12 {}", text='Password:')
        self.pwRetrLabel.place(anchor="nw", relx=0.54, rely=0.41, x=0, y=0)
        self.pwRetrOutput = tk.Entry(self.retrFrame, state="disabled")
        self.pwRetrOutput.configure(background="#eeeeee", borderwidth=0)
        self.pwRetrOutput.place(
            anchor="nw",
            relx=0.65,
            rely=0.425,
            width=250,
            x=0,
            y=0)
        self.clearRetrButton = tk.Button(self.retrFrame, command=lambda: self.clearRetrievedInfo())
        self.clearRetrButton.configure(
            background="#006747",
            font="{Raleway} 12 {bold}",
            foreground="#ffffff",
            text='Clear')
        self.clearRetrButton.place(
            anchor="nw",
            relx=0.75,
            rely=0.5,
            width=85,
            x=0,
            y=0)
        self.webRetrLabel = tk.Label(self.retrFrame)
        self.webRetrLabel.configure(font="{Raleway} 12 {}", text='Website:')
        self.webRetrLabel.place(anchor="nw", relx=0.55, rely=0.25, x=0, y=0)
        self.unRetrLabel = tk.Label(self.retrFrame)
        self.unRetrLabel.configure(font="{Raleway} 12 {}", text='Username:')
        self.unRetrLabel.place(anchor="nw", relx=0.54, rely=0.33, x=0, y=0)
        self.webEnterEntry = tk.Entry(self.retrFrame)
        self.webEnterEntry.place(anchor="nw", relx=0.2, rely=0.265, x=0, y=0)
        self.unEnterEntry = tk.Entry(self.retrFrame)
        self.unEnterEntry.place(anchor="nw", relx=0.20, rely=0.345, x=0, y=0)
        self.retrFrame.place(
            anchor="center",
            relheight=0.98,
            relwidth=0.98,
            relx=0.5,
            rely=0.5,
            x=0,
            y=0)
        # End Retrieval Frame

        # Login Screen GUI Frame
        self.loginFrame = tk.Frame(self.bgFrame)
        self.loginFrame.configure(background="#eeeeee", height=200, width=200)
        self.titleLogin = tk.Label(self.loginFrame)
        self.titleLogin.configure(
            font="{Raleway} 24 {bold}",
            text='Password Manager')
        self.titleLogin.place(anchor="n", relx=0.5, rely=0.05, x=0, y=0)
        self.unEntry = tk.Entry(self.loginFrame)
        self.unEntry.place(
            anchor="center",
            relx=0.55,
            rely=0.45,
            width=200,
            x=0,
            y=0)
        self.pwEntry = tk.Entry(self.loginFrame)
        self.pwEntry.configure(show="•")
        self.pwEntry.place(
            anchor="center",
            relx=0.55,
            rely=0.55,
            width=200,
            x=0,
            y=0)
        self.unLabel = tk.Label(self.loginFrame)
        self.unLabel.configure(font="{Raleway} 12 {}", text='Username:')
        self.unLabel.place(anchor="center", relx=0.37, rely=0.45, x=0, y=0)
        self.pwLabel = tk.Label(self.loginFrame)
        self.pwLabel.configure(font="{Raleway} 12 {}", text='Password:')
        self.pwLabel.place(anchor="center", relx=0.37, rely=0.55, x=0, y=0)
        self.loginButton = tk.Button(self.loginFrame, command=lambda: self.login())
        self.loginButton.configure(
            background="#CFC493",
            font="{Raleway} 12 {bold italic}",
            text='Login')
        self.loginButton.place(
            anchor="center",
            height=40,
            relx=0.6,
            rely=0.8,
            width=150,
            x=0,
            y=0)
        self.loginButton.bind("<1>")
        self.wrongLoginLabel = tk.Label(self.loginFrame)
        self.wrongLoginLabel.configure(
            font="{Raleway} 12 {italic}",
            foreground="#f81d22",
            text='Incorrect username or password!')
        self.loginPromptLabel = tk.Label(self.loginFrame)
        self.loginPromptLabel.configure(
            font="{RalewayLight} 12 {italic}",
            text='Create an Account or Log in')
        self.loginPromptLabel.place(
            anchor="center", relx=0.5, rely=0.38, x=0, y=0)
        self.createAccButton = tk.Button(self.loginFrame, command=lambda: self.createAccount())
        self.createAccButton.configure(
            background="#CFC493",
            font="{Raleway} 12 {bold italic}",
            text='Create Account')
        self.createAccButton.place(
            anchor="center",
            height=40,
            relx=0.4,
            rely=0.8,
            width=150,
            x=0,
            y=0)
        self.loginFrame.place(
            anchor="center",
            relheight=0.98,
            relwidth=0.98,
            relx=0.5,
            rely=0.5,
            x=0,
            y=0)
        self.bgFrame.pack(expand="true", fill="both", side="top")

        # Main widget
        self.mainwindow = self.bgFrame

    def run(self):
        self.mainwindow.mainloop()

    # Variable declaration for use in SQL server interfacing functions.
    userID = ''
    sqlUsername = ''
    sqlPassword = ''

    # Logs into the SQL database and returns appropriate errors.
    def login(self):
        self.sqlUsername = self.unEntry.get()
        self.sqlPassword = self.pwEntry.get()
        self.userID = login(cursor, self.sqlUsername, self.sqlPassword)
        self.userID = str(self.userID)
        if self.userID == "Username doesn't exist" or self.userID == 'Password incorrect':
            self.wrongLoginLabel.place(anchor="center", relx=0.5, rely=0.65, x=0, y=0)
        else:
            self.wrongLoginLabel.destroy()
            self.homeFrame.tkraise()

    # Creates login for the SQL database and returns appropriate errors/passes.
    def createAccount(self):
        guiUsername = self.unEntry.get()
        guiPassword = self.pwEntry.get()
        self.userID = createAccount(cursor, guiUsername, guiPassword)
        self.userID = str(self.userID)
        if self.userID == 'Username already exists':
            messagebox.showinfo('Account not created!', 'Username already exists!')
        elif self.userID == "Password isn't long enough":
            messagebox.showinfo('Account not created!', 'Password must be at least 8 characters!')
        elif self.userID == "Password is too long":
            messagebox.showinfo('Account not created!', 'Password must be less than 255 characters!')
        elif self.userID == "Password isn't complex enough, requires at leas 1 Uppercase letter1 complex character and 1 lowercase letter":
            messagebox.showinfo('Account not created!', "Password must have at least 1 Uppercase letter, 1 Lowercase letter, and 1 Complex Character.")
        else:
            messagebox.showinfo('Account created!', "Account created! Please close this box and press Login.")

    # Basic function to return to login page and clear login data when logout button is pressed.
    def logout(self):
        self.userID = ''
        self.sqlPassword = ''
        self.sqlUsername = ''
        self.loginFrame.tkraise()
        self.unEntry.delete(0, 'end')
        self.pwEntry.delete(0, 'end')

    # Basic function to return to home page when a back button is pressed.
    def returnHome(self):
        self.clearGenPassword()
        self.clearLoginInfoEntry()
        self.clearStoredInfo()
        self.clearRetrievedInfo()
        self.homeFrame.tkraise()

    # Generates a password up to 64 characters, returns it to GUI, and stores in genResultPW variable as string.
    def genPassword(self):
        pwLength = int(self.numCharEntry.get())
        if pwLength > 64:
            self.numCharLabel.config(foreground="red", text="Please enter a number less than 65.")
            self.numCharEntry.delete(0, 'end')
            self.pwOutput.delete(0, 'end')
            return
        self.numCharLabel.config(foreground="black", text="How many characters? (Max. 64)")
        genResultPW = ''
        for x in range(pwLength):
            genResultPW += chr(randint(33, 126))
        self.pwOutput.config(state="normal")
        self.pwOutput.insert(0, genResultPW)
        self.pwOutput.config(state="readonly")

    # Stores all login information in the SQL database based on UserID
    def storePassword(self):
        username = self.storeUsernameEntry.get()
        website = self.storeWebsiteEntry.get()
        password = self.storePasswordEntry.get()
        confirmPW = self.storeConfirmPWEntry.get()
        if not username or not website or not password or not confirmPW:
            messagebox.showinfo("Info Not Stored!", "Please fill out all fields.")
        elif password != confirmPW:
            messagebox.showinfo("Info Not Stored!", "Passwords do not match.")
        else:
            output = insert(cursor, self.sqlUsername, self.sqlPassword, password, website, username, self.userID)
        if output == "How did you even break this?":
            messagebox.showinfo("Storage failed!", "Information not stored. Please logout and try again.")
        else:
            messagebox.showinfo("Info Stored!", "Your login information has been stored.")
            self.clearStoredInfo()

    # Retrieves data from the SQL database based on GUI input provided by user.
    def retrievePassword(self):
        self.clearRetrievedInfo()
        username = self.unEnterEntry.get()
        website = self.webEnterEntry.get()
        if not username or not website:
            messagebox.showinfo('Retrieval Failed', 'Please fill out all fields.')
        else:
            queryOutput = query(cursor, self.sqlUsername, self.sqlPassword, website, username, self.userID)
        if queryOutput == "How did you even break this?":
            messagebox.showinfo("Retrieval failed!", "Information not retrieved. Please logout and try again.")
        elif queryOutput == "No password found":
            messagebox.showinfo("Retrieval failed!", "No password found. Please check your info and try again.")
        else:
            self.webRetrOutput.config(state="normal")
            self.webRetrOutput.insert(0, website)
            self.webRetrOutput.config(state="readonly")
            self.unRetrOutput.config(state="normal")
            self.unRetrOutput.insert(0, username)
            self.unRetrOutput.config(state="readonly")
            self.pwRetrOutput.config(state="normal")
            self.pwRetrOutput.insert(0, queryOutput)
            self.pwRetrOutput.config(state="readonly")

    # Clears the generated password after generation. No effect if blank.
    def clearGenPassword(self):
        self.pwOutput.config(state="normal")
        self.pwOutput.delete(0, 'end')
        self.pwOutput.config(state="readonly")
        self.numCharEntry.delete(0, 'end')

    # Copies generated password to the clipboard.
    def copyToClipboard(self):
        root.clipboard_clear()
        root.clipboard_append(self.pwOutput.get())

    # Clears info in the Store Password entry boxes
    def clearStoredInfo(self):
        self.storeConfirmPWEntry.delete(0, 'end')
        self.storePasswordEntry.delete(0, 'end')
        self.storeUsernameEntry.delete(0, 'end')
        self.storeWebsiteEntry.delete(0, 'end')

    # Clears login info entered for retrieval
    def clearLoginInfoEntry(self):
        self.webEnterEntry.delete(0, 'end')
        self.unEnterEntry.delete(0, 'end')

    # Clears retrieved login information
    def clearRetrievedInfo(self):
        self.webRetrOutput.config(state="normal")
        self.webRetrOutput.delete(0, 'end')
        self.webRetrOutput.config(state="readonly")
        self.unRetrOutput.config(state="normal")
        self.unRetrOutput.delete(0, 'end')
        self.unRetrOutput.config(state="readonly")
        self.pwRetrOutput.config(state="normal")
        self.pwRetrOutput.delete(0, 'end')
        self.pwRetrOutput.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerApp(root)
    app.run()