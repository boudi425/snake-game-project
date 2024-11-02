from pyperclip import copy, paste
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import random
def clear_screen():
    os.system("cls")
Conn = sqlite3.connect("Data.db")
Cur = Conn.cursor()
with open("Data_Query.sql", "r") as File:
    Query = File.read()
Cur.execute(Query)
Conn.commit()
class Sign_Up_User:
    def Sign_up_Username(self):
        print("Hello, This is the sign up page")
        input("Press Enter to continue")
        print("Enter your name: ")
        while True:
            Sign_up_Username = input("> ")
            if len(Sign_up_Username) <= 5:
                print("Please Enter a name longer than 5")
            else:
                return Sign_up_Username
            
    def Sign_Up_Password(self):
        print("Enter your password: ")
        while True:
            Sign_up_Password = input("> ")
            if len(Sign_up_Password) <= 8:
                print("Please Enter a name longer than 8")
            else:
                return Sign_up_Password
            
class Login_User:
    def Login_Username(self):
        print("Hello This is the Login page")
        input("Press Enter to continue..")
        print("Enter your name: ")
        while True:
            Name_login = input("> ")
            if len(Name_login) <= 5:
                print("Please Enter at a least more than 5 character")
            
            else:
                return Name_login
    def Login_password(self):
        print("Enter your password:")
        while True:
            password_login = input(">")
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
        input("Press Enter to continue......... ")
        clear_screen()
        print("Please Choose from the Following: ")
        print("1.Sign up")
        print("2. Login")
        print("3. Quit")
        while True:
            choice = input("> ")
            if choice == "1" or choice.capitalize().startswith("S"):
                self.set_up_sign_up()
                self.set_up_Login()
                break
            elif choice == "2" or choice.capitalize().startswith("L"):
                self.set_up_Login()
                break
            else:
                self.Quit()    
                      
    def set_up_sign_up(self):
        while True:
            Username = self.Sign_Up.Sign_up_Username()
            Name = Cur.execute("SELECT Name FROM Data WHERE Name = ?", (Username,))
            result = Name.fetchone()
            if Username == result:
                print("SOMEONE IS ALREADY HAS THIS NAME PLEASE CHANGE IT")
                continue
            else:
                break
        Password = self.Sign_Up.Sign_Up_Password()
        Cur.execute("INSERT INTO Data (Name, Password, Score) VALUES (?, ?, 0)", (Username, Password,))
        Conn.commit()
            
    def set_up_Login(self):
        global Login_Name
        Names = Cur.execute("SELECT Name FROM Data")
        if len(Names.fetchall()) == 0:
            print("NO NAMES IN THE DB PLEASE SIGN UP FIRST")
            self.set_up_sign_up()
        while True:
            try:
                Login_Name = self.Login.Login_Username()
                True_Login_Name = Cur.execute("SELECT Name FROM Data WHERE Name = ?", (Login_Name.capitalize(),))
                Result = True_Login_Name.fetchone()
                if Login_Name == Result[0]:
                    print("Login Successfully....")
                    break
                else:
                    print("Login Failed please Try again")
            except sqlite3.Error:
                print("I hate myself")
        self.start_game()
    def start_game(self):
        print("I will ask general questions and i want you to answer it")
        print("You have only 3 attempts so be careful")
        input("Press Enter to Start")
        Questions = Cur.execute("SELECT question FROM Questions")
        Questions_List = Questions.fetchall() 
        Questions_Len = len(Questions_List)
        Num_Guesses = 3
        Score = 0
        while True:
            Index = random.randint(0, Questions_Len-1)
            print(f"{Questions_List[Index]}")
            print("Enter your answer: ")
            Answer = input("> ")
            True_Answer = Cur.execute("SELECT answer FROM Questions WHERE question = ?", (Questions_List[Index])).fetchone()
            if Answer.capitalize() == True_Answer[0]:
                print("You Did it Correct !")
                Score += 3
            elif Answer.capitalize() != True_Answer[0] and Num_Guesses == 0:
                if Score < 0:
                    Score = 0
                Cur.execute("UPDATE Data SET Score = ? WHERE Name = ? ", (Score, Login_Name))
                Scores = Cur.execute("SELECT Score FROM Data WHERE Name = ?", (Login_Name,))
                print(f"Your score is {Scores.fetchone()}")
                self.Quit()
            elif Answer.capitalize() != True_Answer[0]:
                print(f"Wrong answer, The correct answer is {True_Answer[0]}")
                Score -= 3
                Num_Guesses -= 1
    def Quit(self):
        print("Thanks for using my game")
        Conn.commit()
        Conn.close()
        sys.exit()
        
        
Sys = System()
Sys.set_up_Users()