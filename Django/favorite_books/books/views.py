from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages

def create(request):

  if 'user_id' not in request.session:
    return redirect('login')

  if request.method == 'POST':
    errors = Book.objects.validate(request.POST)
    if errors:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('books:create_book')
    
    user = User.objects.get(id=request.session.get('user_id'))
    book = Book.objects.create_book(user, request.POST.get('title',''), request.POST.get('description', ''))
    user.liked_books.add(book)

    return redirect('books:create_book')

  user_id = request.session.get('user_id', None)
  user = User.objects.get(id=user_id)
  books = Book.objects.all().order_by()
  return render(request,'books/create.html', {
    'books': books,
    'user': user
  })

def add_to_favorites(request, pk):
    if 'user_id' not in request.session:
      return redirect('login')
    
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('login')
            
        user = User.objects.get(id=request.session.get('user_id'))
        book = Book.objects.get(id=pk)
        
        user.liked_books.add(book)
        
    return redirect('books:create_book')

def delete_from_favorite(request, pk):
    if 'user_id' not in request.session:
      return redirect('login')
    
    if request.method == 'POST':
      book = get_object_or_404(Book, pk=pk)
      user_id = request.session.get('user_id')
      user = get_object_or_404(User, pk=user_id)
      
      user.liked_books.remove(book)
      return redirect('books:create_book')

def book_details(request, pk):
    if 'user_id' not in request.session:
      return redirect('login')
    book = get_object_or_404(Book, pk=pk)
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    users_who_like = book.users_who_like.all()

    return render(request, "books/book_details.html", {
      'book': book,
      'users_who_like': users_who_like,
      'user': user
})

def delete_book(request, pk):
    if 'user_id' not in request.session:
      return redirect('login')
    
    if request.method == 'POST':
      book = get_object_or_404(Book, pk=pk)
      user_id = request.session.get('user_id')
      user = get_object_or_404(User, pk=user_id)

      if user_id != book.uploaded_by.id:
        return redirect('books:create_book')
      
      book.delete()
      return redirect('books:create_book')
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, User

def update_book(request, pk):
    if 'user_id' not in request.session:
        return redirect('login')
    
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        user_id = request.session.get('user_id')
        
        if user_id != book.uploaded_by.id:
            messages.error(request, "You do not have permission to edit this book.")
            return redirect('books:create_book')
        
        errors = Book.objects.validate(request.POST, id=book.id)

        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('books:update_book', pk=book.id)

        Book.objects.update_book(book, request.POST)
        
        messages.success(request, "Book updated successfully!")
        return redirect('books:create_book')
  
    return render(request, 'books/update-book.html', {
        'book': book
    })


