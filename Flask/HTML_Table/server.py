# Import Flask and render_template for creating the web application
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Sample user data - list of dictionaries containing user information
users = [
   {'first_name' : 'Khaled', 'last_name' : 'Alabadla'},
   {'first_name' : 'Bilal', 'last_name' : 'Qanoa'},
   {'first_name' : 'Belal', 'last_name' : 'Alshareef'},
   {'first_name' : 'Ali', 'last_name' : 'Abdalghafour'}
]

# Route for the home page
@app.route('/')
def home():
    # Render the index.html template and pass the users list to it
    return render_template('index.html', users = users)

# Run the Flask application
if __name__ == '__main__':
    # debug=True enables auto-reload and detailed error messages during development
    app.run(debug=True)