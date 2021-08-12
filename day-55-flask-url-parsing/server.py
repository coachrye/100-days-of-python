from flask import Flask
import random

app = Flask(__name__)

the_number = random.randint(0, 10)

@app.route('/')
def home():
    return f'<h1>{the_number}Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def check_guess(guess):
    if guess > the_number:
        return f'<h1 style="color: blue;">Too High!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if guess < the_number:
        return f'<h1 style="color: red;">Too Low!</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1 style="color: green;">You Found me!</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
