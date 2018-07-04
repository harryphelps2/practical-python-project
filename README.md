# practical-python-project
## Overview
A game where users play to solve riddles and move on to the next riddle when they guess correctly. The app will keep a record of high scores for each user, and display wrong answers for other users to see.

## Features

### Views
It should present a login view to the player who can enter a username and proceed to the game. 

It should have a second view for playing the game. 

It should have a view of the leaderboard in descending order. 

# Data
It should have a dictionary of riddles and answers. 

It should store the usernames in a dictionary with a high score. 

It should have a dictionary of guesses with username and timestamp of submission.

### Functionality
It should have the ability to submit a guess of the answer to the riddle through a form. 

It should check if the guess is the same as the answer in the dictionary. 

If the answer is the same it should move on to the next riddle, increase the score associated with the username, and add to the guesses database the time of the correct guess and who guessed correctly. 

It should check if the score is higher that the current high score for that user and replace it in the database if it is. 

If the answer is wrong it should tell the user, store the answer in the answers database with a time stamp and clear the text area for another guess. 

## Testing
Test to return true if answer is right and false if wrong. 

Test if the score increments by one if the answer is right.

Test to keep the score the same if the answer is wrong.

Test to move onto the next riddle if the answer is correct.

Test to keep on the same riddle if the answer is incorrect.

Test if the score is higher than the current high score and overwrite it if it is.

## Getting set up
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
```$ python -m flask run```
