from tkinter import *
import sqlite3
import sys
import os
Window = Tk()
Window.geometry("600x600")
Window.title("Snake Game menu")
Conn = sqlite3.connect("Player_Data.db")
Cur = Conn.cursor()
with open("Menu_DB_Queries.sql", "r") as Sql_Query:
    Query = Sql_Query.read()
Cur.execute(Query)
Conn.commit()

class Menu:
    def start_menu(self):
        Heading = Label(Window, text="Welcome to the game", font=("Helvetica", 16, "bold"), justify=CENTER, background="black")
        Start_button = Button(Window, text="Start Game", width=200, height=100, background="red", font=("Arial", 20, "blod"))
        Leaderboard_button = Button(Window, text="Leaderboard", width=200, height=100, background="yellow", font=("Arial", 20, "blod"))
        Quit_button = Button(Window, text="Quit Game", width=200, height=100, background="blue", font=("Arial", 20, "blod"), command=self.quit_message())
    def quit_message(self, quit_file):
        Quit_window = Tk()
        Quit_window.geometry("300x300")
        quit_heading = Label(Quit_window, text="Thanks for using my program", font=("Helvetica", 16, "bold"), justify=CENTER, background="black")
        Quit_Button =  Button(Quit_window, text="Quit", font=("Arial", 20, "blod"), command=Quit_window.destroy)
        Feedback_button = Button(Quit_window, text="Give A Feedback!", font=("Arial", 20, "blod"), command=Open_url())
        
#Shows the Start button, leaderboard button, quit button
#Every one of these will do it's job and for sure the start one will be more complex
#We will need Entries , Sumbit buttons , Back button , Alot of windows i think
#also,A restart game menu for sure sqlite3 will be used in database i will see if i'll use matplotlib
#But i don't think i will need it and for the last step i will need to desgin it with some colors