# Dojo and Ninja Django App

This project contains a simple Django app with two models:

- `Dojo`: stores name, city, state, and a `desc` text field.
- `Ninja`: stores first and last name, linked to a `Dojo` via a foreign key.

## Setup

1. Activate the Python environment.
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Queries

Shell queries used are saved in `dojo_queries.txt`.

## Notes

- The `Dojo` model was updated to include a `desc` field with default value `old dojo`.
- A migration file `dojo_app/migrations/0002_dojo_desc.py` was created and applied.
