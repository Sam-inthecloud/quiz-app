import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Uncomment to recreate the table

"""
# Create the questions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )
''')

print("Table created successfully.")
"""

# Questions for databse
questions = [
    ("What is the national animal of Scotland?", "Unicorn", "Lion", "Dragon", "Dolphin", "A"),
    ("Which country has a place named 'Dull'?", "Scotland", "Australia", "USA", "Germany", "A"),
    ("What is a group of flamingos called?", "A Flock", "A Parade", "A Flamboyance", "A March", "C"),
    ("What was the first soft drink consumed in space?", "Pepsi", "Coca-Cola", "Fanta", "Sprite", "B"),
    ("What is illegal to own in Switzerland if you only have one?", "A Rabbit", "A Goldfish", "A Parrot", "A Hamster", "B"),
    ("What is the collective noun for a group of pandas?", "A Herd", "An Embarrassment", "A Cuddle", "A Bamboo", "B"),
    ("Which animal can hold its breath longer than a dolphin?", "A Beaver", "A Sloth", "A Tortoise", "An Otter", "B"),
    ("What color is hippo sweat?", "Clear", "Pink", "Yellow", "Green", "B"),
    ("What’s the tiny piece at the end of a shoelace called?", "A Tiplet", "A Tog", "An Aglet", "A Loop", "C"),
    ("What’s the only fruit that has its seeds on the outside?", "Raspberry", "Blueberry", "Strawberry", "Blackberry", "C")
]

# Insert  questions into the table
cursor.executemany('''
    INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
''', questions)
conn.commit()
print("Questions have been inserted successfully.")
#Close the connection
conn.close()
