import sqlite3
import pandas as pd
conn = sqlite3.connect("Player_Data.db")
cur = conn.cursor()

# List of questions
questions = [
    "Which country has the largest population in the world?",
    "What is the longest river in the world?",
    "Which desert is the largest in the world?",
    "Who was the first president of the United States?",
    "In which year did the Titanic sink?",
    "Which ancient civilization built the Machu Picchu?",
    "What is the chemical symbol for gold?",
    "How many bones are in the human body?",
    "What is the largest organ in the human body?",
    "Who is known as the father of modern physics?",
    "Which artist painted the 'Mona Lisa'?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the fastest land animal?",
    "Which bird is known for its ability to mimic sounds?",
    "What is the tallest type of tree in the world?",
    "In which sport is the 'Green Jacket' awarded?",
    "What country does the football player Lionel Messi come from?",
    "How many players are on a soccer team on the field?"
]

# List of answers
answers = [
    "China",
    "The Nile River",
    "The Sahara Desert",
    "George Washington",
    "1912",
    "The Inca civilization",
    "Au",
    "206",
    "The skin",
    "Albert Einstein",
    "Leonardo da Vinci",
    "William Shakespeare",
    "The cheetah",
    "The parrot",
    "Redwood",
    "Golf",
    "Argentina",
    "11"
]

for q in questions:
    for a in answers:
        df = pd.read_sql_query("INSERT INTO Questions VALUES (?, ?)", params=(q, a))
        conn.commit()
conn.close()