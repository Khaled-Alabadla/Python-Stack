from django.shortcuts import render, redirect, get_object_or_404

from .models import Author, Book


def books(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        if title:
            Book.objects.create(title=title, desc=desc)
        return redirect('books_authors_app:books')

    context = {
        'books': Book.objects.all().order_by('id'),
    }
    return render(request, 'books_authors_app/book_list.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        if author_id:
            author = get_object_or_404(Author, pk=author_id)
            book.authors.add(author)
        return redirect('books_authors_app:book_detail', book_id=book.id)

    available_authors = Author.objects.exclude(books=book).order_by('last_name', 'first_name')
    context = {
        'book': book,
        'available_authors': available_authors,
    }
    return render(request, 'books_authors_app/book_detail.html', context)


def authors(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        notes = request.POST.get('notes', '').strip()
        if first_name and last_name:
            Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect('books_authors_app:authors')

    context = {
        'authors': Author.objects.all().order_by('id'),
    }
    return render(request, 'books_authors_app/author_list.html', context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
            author.books.add(book)
        return redirect('books_authors_app:author_detail', author_id=author.id)

    available_books = Book.objects.exclude(authors=author).order_by('title')
    context = {
        'author': author,
        'available_books': available_books,
    }
    return render(request, 'books_authors_app/author_detail.html', context)
