# Quiz App

This is a simple quiz application built with Python and SQLite. It allows users to take quizzes, store their answers, and track their scores. The application is designed to be run locally, and it includes a set of automated tests to ensure the functionality of the app.

## Features

- Take quizzes with multiple-choice questions.
- Store answers and calculate scores.
- Run automated tests to validate the app's functionality.
- Simple integration with a database to store quiz data.

## Tech Stack

- **Python**: The main programming language used to build the app.
- **SQL**: Used for storing quiz data (e.g., questions, answers, and scores).
- **unittest**: Python's built-in testing framework for unit tests.

## Setup

### Prerequisites

- Python 3.x
- SQL database (e.g., SQLite)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Sam-inthecloud/quiz-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd quiz-app
   ```

3. Set up the database (if necessary). You can modify the `quiz.db` file or configure a different database as needed.

### Running the Application

To run the app, simply execute the main Python script:

```bash
python app.py
```

### Running Tests

To run the automated tests using `unittest`, use the following command:

```bash
python -m unittest discover -s tests -p "unittest_quiz_app.py"
```

This will discover and run all the tests in the `tests` folder.

## CI/CD

The project is integrated with GitHub Actions for continuous integration. The CI pipeline automatically runs the tests whenever changes are pushed to the repository. This ensures that all tests pass before code is merged.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

