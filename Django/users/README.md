# Django Users Project

Django project that defines a custom `User` model in the `user_app` application.

## What it includes

- `user_app/models.py` - Defines the `User` model with fields:
  - `first_name`
  - `last_name`
  - `email_address`
  - `age`
  - `created_at`
  - `updated_at`
- `user_app/migrations/0001_initial.py` - Migration file to create the `User` table.
- `user_queries.txt` - Shell queries used to create, retrieve, update, delete, and sort `User` records.

## Setup

1. Activate your Python environment.
2. Install Django if needed.
3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Shell commands

Open the Django shell and import the model:

```bash
python manage.py shell
```

Then in the shell:

```python
from user_app.models import User
```

## Query examples

See `user_queries.txt` for the exact queries used to:

- create 3 users
- retrieve all users
- retrieve the first and last user
- update the user with `id=3`
- delete the user with `id=2`
- sort users by `first_name` ascending and descending
