# Practical Python Milestone Project - Mental Maths Game

Link to live site: https://mental-maths-hp.herokuapp.com/

A game where users play to solve mental maths questions and progress through the game when they guess correctly. The app will keep a record of high scores for each user, and display other users who have answered incorrectly on each question on a Wall of Shame.

## UX
 
- As a user I want to enter in a username to start the game.

- I want to be asked 10 challenging mental maths questions.

- I want to progress through the game if I correctly guess.

- I want to see a wall of shame of other users who have guessed it wrong.

- I want a celebration if it I get to the end.

## Features

### Views

It should present a login view to the player who can enter a username and proceed to the game.

It should have a second view for playing the game.

It should have a view of the leaderboard in descending order.

### Data

It should have a dictionary of riddles and answers.

It should store the usernames in a dictionary with a high score.

It should have a dictionary of guesses with username and timestamp of submission.

### Functionality

It should have the ability to submit a guess of the answer to the riddle through a form.

It should check if the guess is the same as the answer in the dictionary.

If the answer is the same it should move on to the next riddle, increase the score associated with the username, and add to the guesses database the time of the correct guess and who guessed correctly. 

It should check if the score is higher that the current high score for that user and replace it in the database if it is. 

If the answer is wrong it should tell the user, store the answer in the answers database with a time stamp and clear the text area for another guess. 

## Technologies Used

The site uses:

1. Python framework [Flask](http://flask.pocoo.org/) for the backend
2. [Bootstrap](https://getbootstrap.com/) for front end layout

## Testing

| Scenario                                                                 | Results                                                                                |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| User happens upon the homepage and enters a username and presses return. | The game starts sucessfully and the user is taken to question 1.                       |
| The user guesses the right answer.                                       | The user should progresses onto the next question and their score is incremented by 1. |
| The user guessed the wrong answer.                                       | The user stays on the same page and are added to the wall of shame.                    |
| The user completes the game                                              | The user is shown the leaderboard.                                                     |

### Automated tests

1. Test if the answer is correct.
2. Test if the score is incremented by 1.
3. Test to order the leaderboard in descending order.

Automated test suite can be found here: https://github.com/harryphelps2/practical-python-project/blob/master/test_run.py

## Deployment

To deploy the project on Heroku:

1. Add Procfile to tell Heroku it is a web app and to run the run.py script:

```web: python run.py```

2. Connected Heroku to the github repo.

3. Add config vars for IP 0.0.0.0 and PORT 5000.


To run locally:

1. Install python3
   On the command line install HomeBrew
   ```$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

   Then 
   ```$ brew install python```

2. Get pip if not already installed
```$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
Then
```$ python get-pip.py```

3. Use pip to install Flask
   ```pip install Flask```

4. Then run Flask with 
```$ FLASK_APP=run.py FLASK_DEBUG=1 flask run```

## Credits

### Acknowledgements

- Celebration javascript confetti animation taken from https://gist.github.com/defaultnamehere/304035030078e590138b
