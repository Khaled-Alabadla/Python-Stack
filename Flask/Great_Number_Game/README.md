# Great Number Game

A simple web application built with **Python** and **Flask** where users try to guess a randomly generated number between 1 and 100.

## Features
- **Random Number Generation**: A new number is generated for each game session.
- **Feedback System**: Tells the user if their guess is "Low!", "High!", or "Correct!".
- **Attempt Tracker**: Keeps track of how many guesses the user has made.
- **Win/Loss Conditions**: 
  - The user wins if they guess the number correctly.
  - The user loses if they fail to guess the number within 5 attempts.
- **Leaderboard**: Users who win can submit their name to a persistent leaderboard saved in a JSON file.
- **Session Management**: Uses Flask sessions to maintain game state.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Data Persistence**: JSON (for leaderboard)

## Project Structure
- `server.py`: The main Flask application and route handlers.
- `leaderboard.json`: Persistent storage for winners' scores.
- `templates/`: Contains the HTML structure for the game and leaderboard.
- `static/`: Contains CSS
