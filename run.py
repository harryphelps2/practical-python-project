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

def increment_score(old_score):
    new_score = old_score =+ 1
    return new_score

def determine_high_score(high_score, new_score):
    if high_score < new_score:
        high_score = new_score
    return high_score

def submit_guess(score, guess, answer):
    if request.method == 'POST':
        if is_correct(guess, answer):
            increment_score(score)
        else:
            print("incorrect")
    return score

def add_user(username):
    with open("data/users.txt", "r") as f:
        users = json.loads(f.read())
        users[username] = 0
    with open("data/users.txt", "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    
    
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
    with open("data/riddles.json", "r") as riddles_data:
        riddles = json.load(riddles_data)
    return render_template("riddles.html", riddles=riddles, score=score)

if __name__ == '__main__':
    app.run(debug=True)