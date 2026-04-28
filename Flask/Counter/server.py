from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'fdhfdohfdh5496549784'

@app.route('/')
def index():
    # Track page loads (visits)
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    
    # Track counter value (can be manipulated)
    # Default behavior: increments by 1 on every load
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
        
    return render_template('index.html')

@app.route('/increment_by_two')
def add_two():
    # We increment by 1 here, because redirecting to '/' will add another 1
    if 'count' in session:
        session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset_counter():
    # Remove from session so that the index route initializes it to 0
    session.pop('count', None)
    return redirect('/')

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    inc = int(request.form.get('increment', 1))
    # Subtract 1 because redirecting to '/' will add 1
    if 'count' in session:
        session['count'] += (inc - 1)

    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
