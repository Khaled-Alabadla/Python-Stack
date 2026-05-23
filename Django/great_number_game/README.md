# Great Number Game

A Django app that lets users play a number guessing game.

## Features

- Picks a random number between 1 and 100 when the user visits the site
- Stores the target number in session
- Lets the user submit guesses and shows whether the guess is too high, too low, or correct
- Offers a play again option after winning

## Setup

1. Create and activate a Python virtual environment.
2. Install Django if needed:
   ```bash
   pip install django
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Open `http://127.0.0.1:8000/` in your browser and follow the prompts to guess the number.
