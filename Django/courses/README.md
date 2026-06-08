# Course Management Django Project

A simple Django application for managing courses and adding comments.

## Features

- Create courses with a name and description
- View course details and comments
- Add comments to courses
- Remove comments with a confirmation modal using AJAX
- Clean, responsive UI for course listing and detail pages

## Setup

1. Create and activate your Python environment.
2. Install dependencies, e.g.:

```bash
pip install django
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Open the site at `http://127.0.0.1:8000/`.

## Notes

- AJAX deletion is used for comment removal from the course detail page.
- The confirmation modal allows the user to cancel or confirm before the comment is deleted.
- The project uses inline styling in templates for a polished visual experience without extra static files.
