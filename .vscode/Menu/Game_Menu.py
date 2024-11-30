# Importing Modules
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import sqlite3
import sys
import os
Window = Tk() # The screen
Window.geometry("600x600") # Screen Dimensions
Window.title("Snake Game menu") # Screen Title
Conn = sqlite3.connect("Player_Data.db") #Connect/Opens the Database
Cur = Conn.cursor() # Get The cursor for more complex methods
with open("Menu_DB_Queries.sql", "r") as Sql_Query:
    Query = Sql_Query.read() #Read the Main Query 
Cur.execute(Query) # Create the Table
Conn.commit() # Commit the Change
#-------------------------------------------------

class Menu: # Class for more Functionality
    def start_menu(self): # Make the Start Menu
        Heading = Label(Window, text="Welcome to the game", font=("Helvetica", 16, "bold"), justify=CENTER, background="black")
        Start_button = Button(Window, text="Start Game", width=200, height=100, background="red", font=("Arial", 20, "blod"))
        Leaderboard_button = Button(Window, text="Leaderboard", width=200, height=100, background="yellow", font=("Arial", 20, "blod"))
        Quit_button = Button(Window, text="Quit Game", width=200, height=100, background="blue", font=("Arial", 20, "blod"), command=self.quit_message())
        #Doing the Graphices and Buttons !
    def start_game_Window(self): # The actual Start Game Menu for the game
        Start_Game_Window = Tk()
        Start_Game_Window.geometry("600x600")
        Start_Game_Window.title("Snake Game")
        Heading = Label(Start_Game_Window, text="Start Game Menu", font=("Helvetica", 16, "bold"), justify=CENTER, background="black")
        #----------------------------------------------------------------------------------
        Name = Text(Start_Game_Window, text="Enter your name ", font=("Helvetica", 16, "bold"), color="blue")
        Name_Entry = Entry(Start_Game_Window, font=("Helvetica", 16, "bold"), color="blue")
        Password = Text(Start_Game_Window, text="Enter your Password ", font=("Helvetica", 16, "bold"), color="blue")
        Password_Entry = Entry(Start_Game_Window, font=("Helvetica", 16, "bold"), color="blue", show="*")
        # Name Input for the Data Analyze
        #-------------------------------------------------------------------
        Diffcuilty = Label(Start_Game_Window, text="Choose Your Diffcuilty", font=("Helvetica", 16, "bold"))
        Combox_Str = StringVar()
        Diffcuilty_ComboBox = ttk.Combobox(Start_Game_Window, width=10, textvariable=Diffcuilty_ComboBox)
        Diffcuilty_ComboBox["values"] = ("Easy", "Medium", "Hard", "Extreme")
        #Combobox for limitng choices for the user , For more simple Manipulation and for less Errors
        button = ttk.Button(Start_Game_Window, text="Sumbit", command=self.Insert_Data(Start_Game_Window))
        #Sumbit Button for the insert of the data
    def quit_message(self, quit_file): #Quit Meny With A good feedback and a Web Page!
        Quit_window = Tk()
        Quit_window.geometry("300x300")
        quit_heading = Label(Quit_window, text="Thanks for using my program", font=("Helvetica", 16, "bold"), justify=CENTER, background="black")
        Quit_Button =  Button(Quit_window, text="Quit", font=("Arial", 20, "blod"), command=Quit_window.destroy)
        #Close the Whole programm when clicked on Quit
        Feedback_button = Button(Quit_window, text="Give A Feedback!", font=("Arial", 20, "blod"), command=Open_url(quit_file))
    def Insert_Data(self, Master):
        Text_name = Entry.get()
        Password = Entry.get()
        if Text_name.strip() == "":
            messagebox.showwarning("Warning", "Entry is Empty")
            return
        if Password.strip() == "":
            messagebox.showwarning("Warning", "Entry is Empty")
            return
        try:
            while True:
                Names = Cur.execute("SELECT Name FROM Data").fetchall()
                if Text_name in Names:
                    messagebox.showwarning("Warning", f"The username: {Text_name} is already used Try Something else!")
                else:
                    break
            Cur.execute("INSERT INTO Data (Name, Password, Score) VALUES (?, ?, ?)", (Text_name, Password, 0))
            messagebox.showinfo("Success", f"The user {Text_name} has been inserted")
            Entry.delete(0, "end")
        except Exception:
            print(f"Failed to Insert")
    def Get_Diffcuilty(self):
        Combo_Box_Choice = ttk.Combobox.get()
        return Combo_Box_Choice
        #Open the Web if the user choosed 'Give A Feedback!'
#Shows the Start button, leaderboard button, quit button
#Every one of these will do it's job and for sure the start one will be more complex
#We will need Entries , Sumbit buttons , Back button , Alot of windows i think
#also,A restart game menu for sure sqlite3 will be used in database i will see if i'll use matplotlib
#But i don't think i will need it and for the last step i will need to desgin it with some colors