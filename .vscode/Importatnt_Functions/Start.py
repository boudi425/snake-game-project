#Good luck with your functions Abdo i choosed you for a reason and i know you will be more than enough for this hard task
import random
import sys
import string
from random import shuffle
import webbrowser
import os

def Caculate_Score(score=0):
    Score_Gained = score * 3
    return Score_Gained
def random_number(First_Num=0, Second_Num=100):
    random_number_genarated = random.randint(First_Num, Second_Num)
    #yield 
    return random_number_genarated

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.punctuation)
s4 = list(string.digits)

number_of_characters = 10

shuffle(s1)
shuffle(s2)
shuffle(s3)
shuffle(s4)

part1 = round(number_of_characters * (30/100))
part2 = round(number_of_characters * (20/100))

def Strong_password(Number_of_characters=10):
    password = []
    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])
    for i in range(part2):
        password.append(s3[i])
        password.append(s4[i])
    shuffle(password)
    password = "".join(password[0:])
    return password
def Quit_Task():
    sys.exit()
def Open_Url(file_name="Game_Web.html"):
    # Specify the path to your HTML file
    html_file_path = f".vscode/Menu/{file_name}"
    # Convert the file path to an absolute path if it's not already
    absolute_path = os.path.abspath(html_file_path)
    # Open the file in the default web browser
    webbrowser.open(f"file://{absolute_path}")
