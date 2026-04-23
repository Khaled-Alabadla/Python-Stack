# Checkerboard Flask App

This is a Flask web application that generates a customizable checkerboard pattern.

## Features

- Default 8x8 checkerboard with black and white colors
- Customizable grid size (width and height)
- Customizable colors for the checkerboard squares

## How to Run

1. Navigate to the project directory.
2. Run the Flask app: `python checkboard.py`
3. Open your browser and go to `http://127.0.0.1:5000/`

## Routes

- `/`: Default 8x8 checkerboard
- `/<x>`: Checkerboard with custom width x, height 8
- `/<x>/<y>`: Checkerboard with custom width x and height y
- `/<x>/<y>/<color1>/<color2>`: Checkerboard with custom size and colors

## Project Structure

- `checkboard.py`: Main Flask application
- `templates/index.html`: HTML template for the checkerboard
- `static/style.css`: CSS styles for the checkerboard
