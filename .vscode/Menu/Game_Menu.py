# Importing Modules
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import sys
import os
from pathlib import Path

# Get the parent folder's path
parent_path = Path(__file__).parent.parent
sys.path.append(str(parent_path))
from Importatnt_Functions import Start
Window = Tk() # The screen
Window.title("Snake Game menu") # Screen Title
Window.config(bg="DarKGreen")
Conn = sqlite3.connect("Player_Data.db") #Connect/Opens the Database
Cur = Conn.cursor() # Get The cursor for more complex methods
def start_project():
    with open("Menu_DB_Queries.sql", "r") as Sql_Query:
        Query = Sql_Query.read() #Read the Main Query 
    Cur.execute(Query) # Create the Table
    Conn.commit() # Commit the Change
#-------------------------------------------------):
class Menu: # Class for more Functionality
    def start_menu(self): # Make the Start Menu
        Heading = Label(Window, text="Welcome to the game",font=("Helvetica", 40, "bold"), justify=CENTER, background="Blue")
        Heading.pack()
        Start_button = Button(Window, text="Start Game", background="red", font=("Arial", 20), cursor="hand2")
        Start_button.pack(side=tk.TOP, pady=20)
        Leaderboard_button = Button(Window, text="Leaderboard", background="yellow", font=("Arial", 20), cursor="hand2")
        Leaderboard_button.pack(side=tk.TOP, padx=20)
        Quit_button = Button(Window, text="Quit Game", background="red", font=("Arial", 20), cursor="hand2", command=self.quit_message)
        Quit_button.pack(side=tk.TOP, pady=20)
        Window.mainloop()
        #Doing the Graphices and Buttons !
    def start_game_Window(self): # The actual Start Game Menu for the game
        Start_Game_Window = Tk()
        Start_Game_Window.geometry("600x600")
        Start_Game_Window.title("Snake Game")
        Heading = Label(Start_Game_Window, text="Start Game Menu", font=("Helvetica", 16, ), justify=CENTER, background="black")
        #----------------------------------------------------------------------------------
        Name = Text(Start_Game_Window, text="Enter your name ", font=("Helvetica", 16, ), color="blue")
        Name_Entry = Entry(Start_Game_Window, font=("Helvetica", 16, ), color="blue")
        Password = Text(Start_Game_Window, text="Enter your Password ", font=("Helvetica", 16, ), color="blue")
        Password_Entry = Entry(Start_Game_Window, font=("Helvetica", 16, ), color="blue", show="*")
        # Name Input for the Data Analyze
        #-------------------------------------------------------------------
        Diffcuilty = Label(Start_Game_Window, text="Choose Your Diffcuilty", font=("Helvetica", 16, ))
        Combox_Str = StringVar()
        Diffcuilty_ComboBox = ttk.Combobox(Start_Game_Window, width=10, textvariable=Diffcuilty_ComboBox)
        Diffcuilty_ComboBox["values"] = ("Easy", "Medium", "Hard", "Extreme")
        #Combobox for limitng choices for the user , For more simple Manipulation and for less Errors
        button = ttk.Button(Start_Game_Window, text="Sumbit", command=self.Insert_Data(Start_Game_Window))
        #Sumbit Button for the insert of the data
    def quit_message(self, quit_file="Game_Web.html"): #Quit Meny With A good feedback and a Web Page!
        Quit_window = Tk()
        Quit_window.geometry("300x300")
        quit_heading = Label(Quit_window, text="Thanks for using my program", font=("Helvetica", 16, ), justify=CENTER, background="black")
        Quit_Button =  Button(Quit_window, text="Quit", font=("Arial", 20), command=Quit_window.destroy)
        #Close the Whole programm when clicked on Quit
        Feedback_button = Button(Quit_window, text="Give A Feedback!", font=("Arial", 20), command=Start.Open_Url())
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
def Test_Importing():
    return "I DID IT!!!"
menu = Menu()
menu.start_menu()
#Shows the Start button, leaderboard button, quit button
#Every one of these will do it's job and for sure the start one will be more complex
#We will need Entries , Sumbit buttons , Back button , Alot of windows i think
#also,A restart game menu for sure sqlite3 will be used in database i will see if i'll use matplotlib
#But i don't think i will need it and for the last step i will need to desgin it with some colors