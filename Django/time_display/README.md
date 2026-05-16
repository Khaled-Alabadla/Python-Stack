# time_display

A Django project that shows the current server date and time.

## What it does

- Root route (`/`) renders a page showing the current server time.
- View used: `my_app.views.index` — it passes two values to the template:
  - `time` — a formatted human-readable timestamp (example: 2026-05-16 02:34:12 PM)
  - `iso` — the ISO 8601 timestamp (example: 2026-05-16T14:34:12)
- A custom stylesheet is included from `my_app/static/my_app/styles.css`.

## Quick start (development)

1. Create and activate a virtual environment (PowerShell):

   python -m venv env
   .\env\Scripts\Activate

2. Install Django:

   pip install django

3. Run the development server:

   python manage.py runserver

4. Open the app in your browser:

   http://localhost:8000/

## Files of interest

- `my_app/views.py` — controller that computes current time and passes it to the template.
- `my_app/templates/index.html` — template that displays the time and loads the CSS.
- `my_app/static/my_app/styles.css` — custom stylesheet used by the page.
- `time_display/settings.py` — project settings (timezone, static settings, installed apps).

## Notes on time handling

- The view currently uses Python's `datetime.now()` to get the server time. Another simple approach is `time.strftime()` with `time.gmtime()` as an example; or use `django.utils.timezone.now()`.
- Storing timestamps in UTC and converting to the user's timezone in the browser is recommended for production.
