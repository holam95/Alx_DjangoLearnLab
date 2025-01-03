from django.urls import path
from .views import list_books, create_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),  # View books
    path('books/create/', create_book, name='create_book'),  # Create a book
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),  # Edit a book
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),  # Delete a book
]
