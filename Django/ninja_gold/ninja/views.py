import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest


def setup(request):
    """Game setup page - configure win conditions"""
    if request.method == 'POST':
        # Get win conditions from form
        try:
            goal_gold = int(request.POST.get('goal_gold', 100))
            max_moves = int(request.POST.get('max_moves', 20))
        except (ValueError, TypeError):
            goal_gold = 100
            max_moves = 20
        
        # Ensure values are positive
        goal_gold = max(1, goal_gold)
        max_moves = max(1, max_moves)
        
        # Initialize session data
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
        request.session['goal_gold'] = goal_gold
        request.session['max_moves'] = max_moves
        request.session['game_started'] = True
        request.session.modified = True
        
        return redirect('ninja:index')
    
    context = {
        'game_started': request.session.get('game_started', False),
    }
    return render(request, 'ninja/setup.html', context)


def index(request):
    """Main game page"""
    # Check if game has been initialized
    if not request.session.get('game_started', False):
        return redirect('ninja:setup')
    
    # Get game data
    gold = request.session.get('gold', 0)
    activities = request.session.get('activities', [])
    moves = request.session.get('moves', 0)
    goal_gold = request.session.get('goal_gold', 100)
    max_moves = request.session.get('max_moves', 20)
    
    # Determine game status
    game_over = False
    win = False
    lose = False
    message = ""
    
    if moves >= max_moves:
        game_over = True
        if gold >= goal_gold:
            win = True
            message = f"🎉 You won! You reached {gold} gold in {moves} moves!"
        else:
            lose = True
            message = f"💀 Game Over! You only earned {gold} gold (needed {goal_gold}) in {moves} moves."
    elif gold >= goal_gold:
        game_over = True
        win = True
        message = f"🎉 You won! You reached {gold} gold in {moves} moves!"
    
    context = {
        'gold': gold,
        'activities': activities,
        'moves': moves,
        'goal_gold': goal_gold,
        'max_moves': max_moves,
        'game_over': game_over,
        'win': win,
        'lose': lose,
        'message': message,
    }
    return render(request, 'ninja/index.html', context)


def process_money(request, location):
    """Process the gold transaction based on location from URL"""
    # Only accept valid locations
    valid_locations = ['farm', 'cave', 'house', 'quest']
    if location not in valid_locations:
        return redirect('ninja:index')
    
    # Check if game is over
    if request.session.get('moves', 0) >= request.session.get('max_moves', 20):
        return redirect('ninja:index')
    
    # Initialize session data if not present
    if 'gold' not in request.session:
        return redirect('ninja:setup')
    
    # Determine gold earned/lost based on location
    gold_change = 0
    activity_message = ""
    
    if location == 'farm':
        gold_change = random.randint(10, 20)
        activity_message = f"You entered a farm and earned {gold_change} gold."
    elif location == 'cave':
        gold_change = random.randint(10, 20)
        activity_message = f"You entered a cave and earned {gold_change} gold."
    elif location == 'house':
        gold_change = random.randint(10, 20)
        activity_message = f"You entered a house and earned {gold_change} gold."
    elif location == 'quest':
        # Quest can be positive or negative
        if random.choice([True, False]):
            gold_change = random.randint(0, 50)
            activity_message = f"You completed a quest and earned {gold_change} gold."
        else:
            gold_change = -random.randint(0, 50)
            activity_message = f"You failed a quest and lost {-gold_change} gold. Ouch."
    
    # Update session gold
    request.session['gold'] += gold_change
    
    # Increment moves
    request.session['moves'] = request.session.get('moves', 0) + 1
    
    # Add activity to session
    timestamp = datetime.now().strftime("%B %d %Y %I:%M %p")
    activity_record = {
        'message': activity_message,
        'timestamp': timestamp,
        'gold_amount': gold_change
    }
    request.session['activities'].insert(0, activity_record)
    
    # Mark session as modified
    request.session.modified = True
    
    return redirect('ninja:index')


def reset_game(request):
    """Reset the game"""
    if 'gold' in request.session:
        del request.session['gold']
    if 'activities' in request.session:
        del request.session['activities']
    if 'moves' in request.session:
        del request.session['moves']
    if 'goal_gold' in request.session:
        del request.session['goal_gold']
    if 'max_moves' in request.session:
        del request.session['max_moves']
    if 'game_started' in request.session:
        del request.session['game_started']
    
    request.session.modified = True
    return redirect('ninja:setup')
