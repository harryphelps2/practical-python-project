import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

def write_to_file(filename, data):
    """Write data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

def is_correct(guess, answer):
    if (answer == guess):
        return True

def increment_score(username, score):
    new_score = score + 1
    update_score(username, new_score)
    return new_score

def submit_guess(username, score, guess, answer):
    if is_correct(guess, answer):
        increment_score(username, score)
    else:
        timestamp = datetime.now().strftime("%H:%M:%S")
        incorrect_answer = "{0} incorrectly guessed {1} at {2}... shame\n".format(username, guess, timestamp)
        write_to_file("data/guesses.txt", incorrect_answer)
    return score

def add_user(username):
    with open("data/users.txt", "r") as f:
        users = json.loads(f.read())
        users[username] = 0
    with open("data/users.txt", "w") as f:
        f.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))

def update_score(username, score):
    with open("data/users.txt", "r+") as f:
        users = json.loads(f.read())
        users[username] = score
    with open("data/users.txt", "w+") as f:
        f.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
    return score

def get_answer(score, riddles):
    for question in riddles:
        if question['index'] == score:
            return question['answer']

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page with instructions for playing redirects to username url"""
    if request.method == "POST":
        username = request.form["username"]
        add_user(username)
        return redirect(username)
    return render_template("index.html")

@app.route('/<username>', methods=['GET', 'POST'])
def playgame(username):
    with open("data/users.txt", "r") as f:
        users = json.loads(f.read())
        score = users[username]
    with open("data/guesses.txt", "r") as guesses:
        guesses = guesses.readlines()
    with open("data/riddles.json", "r") as riddles_data:
        riddles = json.load(riddles_data)
    answer = get_answer(score, riddles)
    if request.method == "POST":
        submit_guess(username, score, request.form["guess"], answer)
        return redirect(username)
    return render_template("riddles.html", riddles=riddles, score=score, guesses=guesses)

if __name__ == '__main__':
    app.run(debug=True)