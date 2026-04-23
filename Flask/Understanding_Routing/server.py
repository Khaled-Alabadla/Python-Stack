# Import Flask module
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def hello():
  return "Hello World!!"

# Route for /Champion
@app.route('/Champion')
def champion():
  return "Champion!!"

# Route with a name parameter
@app.route('/say/<name>')
def say(name):
  return f"Hello {name}!!"

# Route with times and word parameters
@app.route('/repeat/<times>/<word>')
def repeat(times, word):
  return f"{word} " * int(times)


# Run the app in debug mode if this file is executed directly
if __name__ == '__main__':
  app.run(debug=True)