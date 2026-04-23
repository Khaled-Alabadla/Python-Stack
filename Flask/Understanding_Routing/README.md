# Understanding Routing - Flask Application

A simple Flask application demonstrating basic routing concepts and URL parameters.

## Overview

This project showcases various Flask routing patterns including static routes, dynamic routes with URL parameters, and multiple parameter handling.

## Routes

- `/` - Returns "Hello World!!"
- `/Champion` - Returns "Champion!!"
- `/say/<name>` - Returns a personalized greeting with the provided name
- `/repeat/<times>/<word>` - Repeats a word a specified number of times

### Installation

1. Install Flask:

```bash
pip install flask
```

2. Run the application:

```bash
python server.py
```

3. Open your browser and navigate to:
   - `http://localhost:5000/` - Home page
   - `http://localhost:5000/Champion` - Champion page
   - `http://localhost:5000/say/YourName` - Personalized greeting
   - `http://localhost:5000/repeat/3/Hello` - Repeat "Hello" 3 times
