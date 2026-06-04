# Books and Authors Django Project

This Django project manages books and authors with a many-to-many relationship.

## What was done

- Added `Book` and `Author` models in `books_authors_app/models.py`
- Registered `books_authors_app` in `books_authors_proj/settings.py`
- Created and applied migrations for the initial models
- Added an `Author.notes` text field and ensured the schema includes it
- Created queries in `queries.txt` for:
  - creating books and authors
  - updating book and author fields
  - assigning authors to books
  - retrieving and modifying many-to-many relationships

## Files

- `books_authors_app/models.py` - contains `Book` and `Author` models
- `books_authors_app/migrations/0001_initial.py` - initial migration
- `queries.txt` - shell commands used for the requested operations
- `README.md` - project summary and usage notes
