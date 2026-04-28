# Import Flask modules for web framework, templating, request handling, and session management
from flask import Flask, render_template, request, redirect, session

# Initialize Flask application
app = Flask(__name__)

# Set secret key for session encryption
app.secret_key = 'kdfkjhdfjhdklhj578686'

# Route for displaying the survey form
@app.route('/')
def form():
  return render_template('form.html')

# Route for processing form submission and storing data in session
@app.route('/process', methods=['POST'])
def process():
  # Store form data in session
  session['name'] = request.form['name']
  session['languages'] = request.form.getlist('languages[]')  # Get multiple selected languages
  session['location'] = request.form['location']
  session['comment'] = request.form['comment']
  # Redirect to results page
  return redirect('/show')

# Route for displaying survey results
@app.route('/show')
def show():
  return render_template('show.html')

# Run the application in debug mode
if __name__ == '__main__':
  app.run(debug=True)