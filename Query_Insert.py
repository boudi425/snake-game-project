import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("Data.db")
cur = conn.cursor()

# Creating the table if it doesn't exist already
cur.execute('''
CREATE TABLE IF NOT EXISTS Questions (
    question TEXT,
    answer TEXT
)
''')

# List of questions and corresponding answers
data = [
    ("Which country has the largest population in the world?", "China"),
    ("What is the longest river in the world?", "The Nile River"),
    ("Which desert is the largest in the world?", "The Sahara Desert"),
    ("Who was the first president of the United States?", "George Washington"),
    ("In which year did the Titanic sink?", "1912"),
    ("Which ancient civilization built the Machu Picchu?", "The Inca civilization"),
    ("What is the chemical symbol for gold?", "Au"),
    ("How many bones are in the human body?", "206"),
    ("What is the largest organ in the human body?", "The skin"),
    ("Who is known as the father of modern physics?", "Albert Einstein"),
    ("Which artist painted the 'Mona Lisa'?", "Leonardo da Vinci"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the fastest land animal?", "The cheetah"),
    ("Which bird is known for its ability to mimic sounds?", "The parrot"),
    ("What is the tallest type of tree in the world?", "Redwood"),
    ("In which sport is the 'Green Jacket' awarded?", "Golf"),
    ("What country does the football player Lionel Messi come from?", "Argentina"),
    ("How many players are on a soccer team on the field?", "11")
]

# Insert data into the table
cur.executemany("INSERT INTO Questions (question, answer) VALUES (?, ?)", data)

# Commit the changes and close the connection
conn.commit()
conn.close()
