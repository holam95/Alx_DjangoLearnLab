from django.urls import path
from .views import LibraryDetailView, LoginView, LogoutView, register, list_books
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from .views import add_book, edit_book, delete_book, list_books  # Import the views


urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library_detail'),  # Corrected to lowercase URL
    path('books/', list_books, name='list_books'),  # Corrected to lowercase URL
    path('login/', LoginView.as_view(), name='login'),  # Template set in views.py
    path('logout/', LogoutView.as_view(), name='logout'),  # Template set in views.py
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),]