# Dojo Survey Application

A Flask web application that collects survey responses from users about their favorite programming languages and other preferences.

## Features

- **Form Collection**: Users can input their name, select a location, choose multiple favorite programming languages, and leave a comment
- **Session Management**: Stores user responses in Flask sessions
- **Results Display**: Shows submitted survey responses on a dedicated page

## Project Structure

```
Dojo Survey/
├── server.py          # Flask application and route handlers
├── templates/
│   ├── form.html      # Survey form page
│   └── show.html      # Results display page
└── README.md          # Documentation
```

## How to Run

1. Install Flask:

   ```bash
   pip install flask
   ```

2. Run the application:

   ```bash
   python server.py
   ```

3. Open your browser and navigate to `http://localhost:5000`

## How It Works

1. **Home Page**: Users fill out the survey form with their name, location, favorite languages, and optional comment
2. **Form Submission**: The form submits to `/process` endpoint via POST
3. **Session Storage**: Responses are stored in the Flask session
4. **Results Page**: User is redirected to `/show` where their survey responses are displayed
