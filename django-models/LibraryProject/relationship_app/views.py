from django.shortcuts import render
from .models import Book,Author
from relationship_app.templates import library_detail.html
from relationship_app.templates import list_books.html

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login


from .utils import role_required


from . import admin_view
from . import librarian_view
from . import member_view


@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})


@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})


@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})

# Create your views here.
def list_books(request):
    books = Book.objects.all
    context = {books:author)

    return render(request, "relationship_app/list_books.html", Book.objects.all())


from django.views.generic.detail import DetailView
from . models import Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relatioship_app/library_datail.html'

    def AllBooks(self):

        Allbooks = library.books.all()
        return render("relationship_app/library_detail.html", from .models import Library)




# Login View
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirect if the user is already authenticated

# Logout View
class LogoutView(LogoutView):
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

    



























