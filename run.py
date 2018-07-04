import os
from datetime import datetime
from flask import Flask,redirect, render_template

app = Flask(__name__)

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

@app.route('/')
def index():
    """Main page with instructions for playing"""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)