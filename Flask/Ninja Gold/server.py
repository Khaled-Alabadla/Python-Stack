from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'fkdhfjdhfj50469734'

# Dictionary mapping buildings to their gold range (min, max)
BUILDINGS = {
    'farm': (10, 20),
    'cave': (5, 10),
    'house': (2, 5),
    'casino': (-50, 50)
}

WIN_GOLD = 500
MAX_MOVES = 15

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['moves'] = 0
        session['game_over'] = False
        session['result'] = None # 'win' or 'loss'

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    # Handle Reset
    if request.form.get('building') == 'reset':
        session.clear()
        return redirect('/')

    if session.get('game_over'):
        return redirect('/')

    building = request.form.get('building')
    if building in BUILDINGS:
        gold_range = BUILDINGS[building]
        earned = random.randint(gold_range[0], gold_range[1])
        
        session['gold'] += earned
        session['moves'] += 1
        
        # Determine activity message and color
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if earned >= 0:
            message = f"Earned {earned} golds from the {building}! ({timestamp})"
            color = "text-success"
        else:
            message = f"Entered a casino and lost {abs(earned)} golds... Ouch.. ({timestamp})"
            color = "text-danger"
            
        # Add to activities 
        session['activities'].append({'message': message, 'color': color})
        
        # Check Win/Loss conditions 
        if session['gold'] >= WIN_GOLD:
            session['game_over'] = True
            session['result'] = 'win'
        elif session['moves'] >= MAX_MOVES:
            session['game_over'] = True
            session['result'] = 'loss'
            
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
