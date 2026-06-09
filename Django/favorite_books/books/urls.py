from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('create', views.create, name='create_book'),
    path('<int:pk>/add-to-favorite', views.add_to_favorites, name="add_to_favorite"),
    path('<int:pk>/delete-from-favorite', views.delete_from_favorite, name="delete_from_favorite"),
    path('<int:pk>/details', views.book_details, name='book_details'),
    path('<int:pk>/delete', views.delete_book, name='delete_book'),
    path('<int:pk>/update', views.update_book, name='update_book')
]
