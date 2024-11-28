from django.urls import path
from . views import BookListView


urlpatterns = [
        path('Library/', LibraryDetailView.as_view()),

        path('Book/', list_book.as_view()]
