# Books and Authors Django Project

This Django project manages books and authors with a many-to-many relationship.

## Features

- Create books and view all books in a table
- Create authors and view all authors in a table
- View a single book with its associated authors
- View a single author with its associated books
- Add authors to a book from a dropdown list
- Add books to an author from a dropdown list
- Dropdowns only include authors or books that are not already associated with the selected item

## Pages

- `/` or `/books/` — create a book and see all books
- `/books/<id>/` — view a specific book and add authors to it
- `/authors/` — create an author and see all authors
- `/authors/<id>/` — view a specific author and add books to them

## Files

- `books_authors_app/models.py` — `Book` and `Author` models
- `books_authors_app/views.py` — views for book and author creation, listing, and detail pages
- `books_authors_app/urls.py` — URL routes for the app
- `books_authors_app/templates/books_authors_app/` — templates for list and detail pages
