from django.urls import path
from . import views

app_name = 'books_authors_app'

urlpatterns = [
    path('', views.books, name='books'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]
