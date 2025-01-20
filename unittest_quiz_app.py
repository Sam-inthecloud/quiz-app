import unittest
from unittest.mock import patch
import sqlite3
from quiz_app import fetch_questions, run_quiz

class TestQuizApp(unittest.TestCase):
    
    def setUp(self):
        """Set up temporary database for testing"""
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE questions (
            id INTEGER PRIMARY KEY, 
            question TEXT, 
            option_a TEXT, 
            option_b TEXT, 
            option_c TEXT, 
            option_d TEXT, 
            correct_answer TEXT
        )''')
        
        # Insert 10 questions for testing
        for i in range(1, 11):
            self.cursor.execute('''
            INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (f"What is {i}+1?", '2', '3', '4', '5', 'A'))
    
        self.conn.commit()

    def tearDown(self):
        """Close the database connection after each test"""
        self.conn.close()

    def test_fetch_questions(self):
        """Test that questions are fetched correctly from the database"""
        questions = fetch_questions()
        self.assertEqual(len(questions), 10)  # Expect 10 questions
        self.assertEqual(questions[0][1], "What is the national animal of Scotland?")

    @patch('builtins.input', side_effect=['A', 'A', 'C', 'B', 'B', 'B', 'B', 'B', 'C', 'C'])  # Provide inputs for all 10 questions
    def test_run_quiz(self, mock_input):
        """Test that the quiz runs correctly"""
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_any_call("Correct! Well done.\n")
            mock_print.assert_any_call("\nYou have completed Sam's Millionaire Quiz! Your final score is 10/10")
            

    @patch('builtins.input', side_effect=['C', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B'])  # Provide inputs for 2 questions
    def test_run_quiz_wrong_answer(self, mock_input):
        """Test that the quiz handles wrong answers correctly"""
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_any_call("Wrong! The correct answer is A.\n")
            mock_print.assert_any_call("You scored less than 10. You now owe Sam £100!")

if __name__ == '__main__':
    unittest.main()
