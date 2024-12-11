from django.urls import path
from .views import LibraryDetailView, CustomLoginView, CustomLogoutView, RegisterView

from .views import list_books

urlpatterns = [
        path('Library/', LibraryDetailView.as_view()),

        path('Book/', list_book.as_view(
        path('login/', CustomLoginView.as_view(), name='login'),
        path('logout/', CustomLogoutView.as_view(), name='logout'),
        path('register/', RegisterView.as_view(), name='register')]
