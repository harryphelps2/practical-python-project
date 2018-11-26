import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'some_secret'

#Filepaths
guesses_file_path = "data/guesses.txt"
leaderboard_file_path = "data/leaderboard.txt"
questions_file_path = "data/questions.json"
users_file_path = "data/users.txt"
    
def read_file(filepath):
    """Read data from file"""
    with open(filepath, "r") as f:
        return json.loads(f.read())

def is_correct(guess, answer):
    """Return True if the answer is equal to the guess"""
    if (answer == guess):
        return True

def increment_score(username, score):
    """Increment score by one"""
    score += 1
    return score

def add_user(username):
    users = read_file(users_file_path)
    users[username] = 0
    with open("data/users.txt", "w") as f:
        f.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))

def update_score(username, score):
    users = read_file(users_file_path)
    users[username] = str(score)
    with open("data/users.txt", "w+") as f:
        f.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
    return score

def update_incorrect_guesses(incorrect_guess, score):
    users = read_file(users_file_path)
    users.update({incorrect_guess : score})
    with open("data/guesses.txt", "w+") as f:
        f.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))

def update_leaderboard(users, number_of_questions):
    leaderboard_list = []
    for i in range(number_of_questions,-1,-1):
        for key, value in users.items():
            if int(value) == i:
                user_highscore = "{0}: {1}\n".format(key, value)
                leaderboard_list.append(user_highscore)
                with open("data/leaderboard.txt", "w") as leaderboard:
                    leaderboard.writelines(leaderboard_list)

def get_answer(score, questions):
    for question in questions:
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
    users = read_file(users_file_path)
    score = int(users[username])
    questions = read_file(questions_file_path)
    answer = get_answer(score, questions)
    incorrect_guesses = read_file(guesses_file_path)
    number_of_questions = len(questions)
    if request.method == "POST":
        guess = request.form["guess"]
        if is_correct(guess, answer):
            score = increment_score(username, score)
            update_score(username, score)
            update_leaderboard(users, number_of_questions)
        else:
            timestamp = datetime.now().strftime("%H:%M:%S")
            incorrect_guess = "{0} incorrectly guessed {1} at {2}... shame".format(username, guess, timestamp)
            update_incorrect_guesses(incorrect_guess, score)
        return redirect(username)
    if score < number_of_questions:
        return render_template("question.html", questions=questions, score=score, guesses=incorrect_guesses)
    else:
        return redirect('/completed')

@app.route('/completed')
def completed():
    return render_template("completed.html")

@app.route('/leaderboard')
def leaderboard():
    leaderboard = [line.rstrip('\n') for line in open('data/leaderboard.txt')]
    print(leaderboard)
    return render_template("leaderboard.html", leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)