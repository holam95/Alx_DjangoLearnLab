from django.shortcuts import render, redirect
from .models import Book, Author, Library
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .utils import role_required

from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

# Role-Based Views
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})

@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()  # Added parentheses to call the queryset
    context = {'books': books}  # Fixed the dictionary key-value pair syntax
    return render(request, "relationship_app/list_books.html", context)

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Corrected template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books related to the library
        return context

# Login View
class LoginView(BaseLoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirect if the user is already authenticated

# Logout View
class LogoutView(BaseLogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



























