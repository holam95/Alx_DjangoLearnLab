from django.urls import path
from .views import LibraryDetailView, LoginView, LogoutView, register
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

from .views import list_books










urlpatterns = [path('Library/', LibraryDetailView.as_view()),]
[path('Book/', list_book.as_view, name='list_books')]
[path('login/', LoginView.as_view(template_name=login.html), name='login'),]
[path('logout/', LogoutView.as_view(template_name=logout.html ), name='logout'),]
[path('register/', views.register(template_name=register.html), name='register')]
[path('admin/', admin_view, name='admin_view'),]
[path('librarian/', librarian_view, name='librarian_view'),]
[path('member/', member_view, name='member_view'),]
        
        
