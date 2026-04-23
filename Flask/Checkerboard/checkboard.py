# Import Flask modules for web app
from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# Route for default checkerboard (8x8, black and white)
@app.route('/')
def checkboard():
  return render_template('index.html', x = 8, y = 8, color1='black', color2='white')

# Route for custom width, default height and colors
@app.route('/<x>')
def checkboard_x(x):
  return render_template('index.html', x = int(x), y = 8, color1='black', color2='white')

# Route for custom width and height, default colors
@app.route('/<x>/<y>')
def checkboard_xy(x, y):
  return render_template('index.html', x = int(x), y = int(y), color1='black', color2='white')

# Route for custom width, height, and colors
@app.route('/<x>/<y>/<color1>/<color2>')
def checkboard_xy_with_colors(x, y, color1, color2):
  return render_template('index.html', x = int(x), y = int(y), color1 = color1, color2 = color2)

# Run the app in debug mode if executed directly
if __name__ == '__main__':
  app.run(debug=True)