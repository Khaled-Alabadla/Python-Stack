# Import Flask framework and render_template for template rendering
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Default route - displays 3 boxes
@app.route('/play')
def main_play():
    return render_template('playground.html', times = 3)

# Dynamic route - displays specified number of boxes based on URL parameter
@app.route('/play/<times>')
def main_many(times):
    return render_template('playground.html', times = int(times))

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)