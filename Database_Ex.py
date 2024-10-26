from pyperclip import copy, paste
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import random
def clear_screen():
    os.system("cls")
Conn = sqlite3.connect("Player_Data.db")
Cur = Conn.cursor()
Cur.executescript("Data_Query.sql")
class Sign_Up_User:
    def Sign_up_Username(self):
        print("Hello, This is the sign up page")
        input("Press Enter to continue")
        print("Enter your name: ")
        while True:
            Sign_up_Username = input("> ")
            if len(Sign_up_Username) < 5:
                print("Please Enter a name longer than 5")
            else:
                return Sign_up_Username
            
    def Sign_Up_Password(self):
        print("Enter your password: ")
        while True:
            Sign_up_Password = input("> ")
            if len(Sign_up_Password) < 8:
                print("Please Enter a name longer than 8")
            else:
                return Sign_up_Password
            
class Login_User:
    def Login_Username():
        print("Hello This is the Login page")
        input("Press Enter to continue..")
        print("Enter your name: ")
        Name_login = input(">")
        while True:
            Name_login = input("> ")
            if len(Name_login) <= 5:
                print("Please Enter at a least more than 5 character")
            
            else:
                return Name_login
    def Login_password(self):
        print("Enter your password:")
        while True:
            password_login = input("> ")
            if len(password_login) <= 8:
                print("Please Enter at a least more than 8 characters")
            else:
                return password_login
class System:
    def __init__(self):
        self.Sign_Up = Sign_Up_User()
        self.Login = Login_User()
    def set_up_Users(self):
        print("This is a guessing game")
        print("If you guess correctly , you will get 5 points")
        print("Otherwise you did get the guess wrong you will lose 3 points")
        print("And to make it fair you have attempts to do it up to 3 attempts")
        print("Your score will be saved so make sure to sign up and login...")
        input("Press Enter to continue")
        clear_screen()
        print("Please Choose from the Following: ")
        print("1.Sign up")
        print("2. Login")
        print("3. Quit")
        while True:
            choice = input(">")
            if choice == "1" or choice.capitalize().startswith("S"):
                self.set_up_sign_up()
                self.set_up_Login()
                self.start_game()
            elif choice == "2" or choice.capitalize().startswith("L"):
                self.set_up_Login()
                self.start_game()
            else:
                self.Quit()    
                      
    def set_up_sign_up(self):
            Username = self.Sign_Up.Sign_up_Username()
            Password = self.Sign_Up.Sign_Up_Password()
            df = pd.read_sql_query(f"INSERT INTO Data VALUES ({Username}, {Password}, 0)", Conn)
            Conn.commit()
            
    def set_up_Login(self):
        df = pd.read_sql_query("SELECT NAME FROM Data", Conn)
        if len(df) == 0:
            print("NO SIGN UP NAME IS HERE PLEASE GO AND SIGN UP!")
            return 
        while True:
            try:
                Username_Login = self.Login.Login_Username()
                query = "SELECT Name, Password, Score FROM Data WHERE Name = ?"
                df = pd.read_sql_query(query, Conn, params=(Username_Login,))
                if df.empty:
                    print("Please enter a valid name.")
                else:
                    print("Login successful!")
                    break 
            except sqlite3.Error:
                print("Please Enter a valid name")
            finally:
                Conn.close()
    def start_game(self):
        print("I will ask general questions and i want you to answer it")
        print("You have only 3 attempts so be careful")
        Questions = Cur.execute("SELECT Question FROM Questions")
        Questions_List = Questions.fetchall()
        Questions_Len = len(Questions_List)
        while True:
            Index = random.randint(0, Questions_Len)
            Num_Guesses = 3
            Score = 0
            print(f"{Questions_List[Index]}")
            print("Enter your answer: ")
            while Num_Guesses < 0:
                Answer = input(">")
                True_Answer = pd.read_sql_query("SELECT Answer FROM Questions WHERE Question = ?", Conn, params=(Questions_List[Index]))
                if Answer == True_Answer:
                    print("You Did it Correct !")
                    Score += 3
                elif Answer != True_Answer and Num_Guesses == 0:
                    self.Quit()
                    
                else:
                    print("Wrong answer, Try again")
                    Score -= 3
                    Num_Guesses -= 1
    def Quit(self):
        sys.exit()