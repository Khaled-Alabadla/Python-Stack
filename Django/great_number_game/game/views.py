import random

from django.shortcuts import redirect, render


def index(request):
    if request.method == 'POST':
        if 'reset' in request.POST:
            request.session.flush()
            return redirect('index')

        if 'target_number' not in request.session:
            request.session['target_number'] = random.randint(1, 100)
            request.session['attempts'] = 0
            request.session['game_over'] = False
            request.session['result'] = ''

        if request.session.get('game_over', False):
            return redirect('index')

        guess = request.POST.get('guess', '').strip()
        message = ''
        result_class = 'info'

        try:
            guess_value = int(guess)
        except ValueError:
            message = 'Please enter a whole number between 1 and 100.'
            request.session['result'] = message
            request.session['result_type'] = result_class
        else:
            request.session['attempts'] = request.session.get('attempts', 0) + 1
            attempts = request.session['attempts']
            target = request.session['target_number']

            if attempts > 5:
                message = f'You lose! The number was {target}. Click Play again to try again.'
                result_class = 'lose'
                request.session['game_over'] = True
            elif guess_value < target:
                message = 'Too low!'
                result_class = 'low'
            elif guess_value > target:
                message = 'Too high!'
                result_class = 'high'
            else:
                message = f'{target} was the number! You guessed it in {attempts} attempt(s).'
                result_class = 'win'
                request.session['game_over'] = True

            request.session['result'] = message
            request.session['result_type'] = result_class

    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['game_over'] = False
        request.session['result'] = ''
        request.session['result_type'] = 'info'

    context = {
        'result': request.session.get('result', ''),
        'result_type': request.session.get('result_type', 'info'),
        'attempts': request.session.get('attempts', 0),
        'game_over': request.session.get('game_over', False),
    }
    return render(request, 'game/index.html', context)
