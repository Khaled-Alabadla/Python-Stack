# Flask Playground

A Flask web application that displays dynamic boxes with responsive styling.

## Project Structure

```
.
├── playground.py           # Flask application with routes
├── static/
│   └── style.css          # Stylesheet for the application
└── templates/
    └── playground.html    # HTML template for rendering boxes
```

## Features

- **Default Route (`/play`)**: Displays 3 boxes on the page
- **Dynamic Route (`/play/<times>`)**: Displays a custom number of boxes based on URL parameter
- **Responsive Design**: Uses flexbox layout that adapts to different screen sizes

## Usage

### Installation

1. Ensure Python and Flask are installed:

   ```bash
   pip install flask
   ```

2. Navigate to the project directory:
   ```bash
   cd Flask/Playground
   ```

### Running the Application

1. Start the Flask server:

   ```bash
   python playground.py
   ```

2. Open your browser and navigate to:
   - `http://localhost:5000/play` - Display 3 boxes (default)
   - `http://localhost:5000/play/5` - Display 5 boxes
   - `http://localhost:5000/play/10` - Display 10 boxes (or any number)

## Files Description

### playground.py

Main Flask application file containing:

- Flask app initialization
- Route handlers for displaying boxes

### templates/playground.html

HTML template that:

- Loads the stylesheet
- Uses Jinja2 templating to dynamically generate boxes
- Renders boxes based on the `times` variable passed from the backend

### static/style.css

Stylesheet providing:

- Reset of default browser styles
- Flexbox layout for responsive box arrangement
- Styling for individual boxes

## Example URLs

| URL        | Result            |
| ---------- | ----------------- |
| `/play`    | Displays 3 boxes  |
| `/play/1`  | Displays 1 box    |
| `/play/6`  | Displays 6 boxes  |
| `/play/12` | Displays 12 boxes |
