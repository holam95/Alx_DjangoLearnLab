from django.urls import path
from .views import LibraryDetailView, LoginView, LogoutView, register

from .views import list_books

urlpatterns = [
        path('Library/', LibraryDetailView.as_view()),

        path('Book/', list_book.as_view(
        path('login/', LoginView.as_view(template_name=login.html), name='login'),
        path('logout/', LogoutView.as_view(template_name=logout.html ), name='logout'),
        path('register/', views.register(template_name=register.html), name='register')]
