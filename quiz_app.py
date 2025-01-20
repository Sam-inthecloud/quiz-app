import sqlite3

def fetch_questions():
    """Fetch all questions from the database"""
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def run_quiz():
    """Runs the quiz, asks questions, and calculates the score."""
    questions = fetch_questions()
    score = 0
    
    print("\nWelcome to Sam's Quiz to win a Million Pounds! Answer the following questions for your chance to be a millionaire:\n")
    
    for question in questions:
        print(f"\n{question[1]}")
        print(f"A. {question[2]} B. {question[3]} C. {question[4]} D. {question[5]}")
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        # Check answer
        if answer == question[6]:
            print("Correct! Well done.\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question[6]}.\n")
    
    # Final Score
    print(f"\nYou have completed Sam's Millionaire Quiz! Your final score is {score}/{len(questions)}")
    
    # Check performance
    if score == len(questions):
        print("Congratulations! You answered all questions correctly. You are now a millionaire! Send me your bank details including the 3 digits at the back.")
    elif score < 10:
        print("You scored less than 10. You now owe Sam £100!")
    else:
        print("Great effort! Keep improving your score!")

# Run the quiz
run_quiz()
