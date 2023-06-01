# Flask Intro Exercises
This repository contains two simple Flask exercises aimed to help beginners get comfortable with setting up a basic Flask application and creating various routes for user requests. The exercises involve creating a greeting application and a basic calculator.

### Setting up your environment
Before you start, you'll need Python and Flask installed on your machine.

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Install Flask by running the command below in your terminal:
 `pip install flask`

### Getting started

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project in your terminal.
3. Run the command export FLASK_APP=app.py to tell Flask which application it should work with.
4. Run the command flask run to start your application.

## Exercise 1: Greet
In the greet folder, you'll find a simple Flask app that responds to these routes:

/welcome: Returns the string "welcome".
/welcome/home: Returns the string "welcome home".
/welcome/back: Returns the string "welcome back".

To test this application:

- Navigate to the greet folder in your terminal.
- Run the command:
`python -m unittest test.py`

## Exercise 2: Calc
The calc folder contains a Flask application that performs simple mathematical operations. The application responds to four different routes. Each route performs a math operation with two numbers, a and b, which are passed in as URL GET-style query parameters.

- /add: Adds a and b and returns the result.
- /sub: Subtracts b from a and returns the result.
- /mult: Multiplies a and b and returns the result.
- /div: Divides a by b and returns the result.

For example, a URL like http://localhost:5000/add?a=10&b=20 should return "30".

Helper functions for these operations are provided in the file operations.py.

Happy coding!