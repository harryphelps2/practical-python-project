import os
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

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page with instructions for playing"""
    if request.method == "POST":
        write_to_file("data/users",request.form["username"]+"\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    return render_template("riddles.html")

if __name__ == '__main__':
    app.run(debug=True)