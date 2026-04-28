from flask import Flask, render_template, request, redirect, session
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'ajfgdf;rngj56476594976'

LEADERBOARD_FILE = 'leaderboard.json'

# Initialize the leaderboard JSON file if it doesn't exist
def init_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump([], f)

# Retrieve the list of scores from the leaderboard file
def get_leaderboard():
    init_leaderboard()
    with open(LEADERBOARD_FILE, 'r') as f:
        return json.load(f)

# Save a new score to the leaderboard and persist it to the JSON file
def add_to_leaderboard(name, attempts):
    scores = get_leaderboard()
    scores.append({'name': name, 'attempts': attempts})
    # Sort by attempts (ascending)
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(scores, f)

# Main route: Initializes session variables and renders the game page
@app.route('/')
def index():
    if 'target_num' not in session:
        session['target_num'] = random.randint(1, 100) # Generate random number between 1 and 100
        session['attempts'] = 0
        session['status'] = None
        session['last_guess'] = None
    
    return render_template('index.html')

# Handles user guess submissions, updates status, and tracks attempts
@app.route('/guess', methods=['POST'])
def guess():
    if 'target_num' not in session:
        return redirect('/')

    user_guess = int(request.form['guess'])

    session['attempts'] += 1
    session['last_guess'] = user_guess
    
    target = session['target_num']
    attempts = session['attempts']
    
    # Check if guess is correct, too low, or too high
    if user_guess == target:
        session['status'] = 'correct'
    elif user_guess < target:
        session['status'] = 'too_low'
    else:
        session['status'] = 'too_high'
    
    # Check for loss after 5 failed attempts
    if session['status'] != 'correct' and attempts >= 5:
        session['status'] = 'lose'
        
    return redirect('/')

# Clears the session to restart the game
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

# Handles submission of the user's name for the leaderboard
@app.route('/submit_score', methods=['POST'])
def submit_score():
    name = request.form.get('name', 'Anonymous')
    attempts = session.get('attempts', 0)
    if session.get('status') == 'correct':
        add_to_leaderboard(name, attempts)
    return redirect('/leaderboard')

# Renders the leaderboard page with stored scores
@app.route('/leaderboard')
def leaderboard():
    scores = get_leaderboard()
    return render_template('leaderboard.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
