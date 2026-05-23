# Ninja Gold Game - Django

A fun web-based game where a ninja can earn gold by visiting different locations!

## Features

- **Four Activity Locations**: Farm, Cave, House, and Quest
  - Farm: Earn 10-20 gold
  - Cave: Earn 10-20 gold
  - House: Earn 10-20 gold
  - Quest: Risky! Earn 0-50 gold or lose 0-50 gold

- **Real-time Gold Counter**: Track your ninja's total gold

- **Activity Log**: See a timestamped history of all your activities with color-coded entries:
  - Green for successful gold gains
  - Red for gold losses

- **Session-based Storage**: Activities are stored in your session (no database required)

### NINJA BONUS ✨

- **URL-based Location Passing**: Location is passed via URL parameter (e.g., `/process_money/farm`) instead of form POST data
- Uses clean, RESTful-style URLs for better code organization

## How to Play

1. **Setup Phase**: Configure your goal gold amount and maximum moves
2. **Game Phase**:
   - Your ninja starts with 0 gold
   - Click on a location (Farm, Cave, House, or Quest) to perform an activity
   - Your gold will increase or decrease based on the activity outcome
   - Quest is risky - you can earn or lose gold!
3. **Winning Conditions**:
   - Reach your goal gold amount before running out of moves
   - The game tracks both conditions and displays progress
4. **Activity Log**: Watch your activity history in real-time with timestamps

## Project Structure

```
ninja_gold/
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database
├── ninja_gold/                    # Project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── ninja/                         # Main game app
│   ├── models.py                 # (session-based, no models needed)
│   ├── views.py                  # Game logic views
│   ├── urls.py                   # App URL patterns
│   ├── migrations/
│   └── templates/
│       └── ninja/
│           ├── index.html        # Main game UI
│           └── setup.html        # Setup/configuration page
└── README.md
```

## Routes

| Route                       | Method   | Description                                           |
| --------------------------- | -------- | ----------------------------------------------------- |
| `/`                         | GET      | Display game page (redirects to setup if not started) |
| `/setup`                    | GET/POST | Setup page - configure win conditions                 |
| `/process_money/<location>` | GET      | Process activity and update gold (NINJA BONUS)        |
| `/reset`                    | GET      | Reset game and return to setup                        |
