from django.urls import path
from .views import LibraryDetailView

from .views import list_books

urlpatterns = [
        path('Library/', LibraryDetailView.as_view()),

        path('Book/', list_book.as_view()]
