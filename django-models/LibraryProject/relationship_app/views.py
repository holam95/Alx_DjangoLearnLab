from django.shortcuts import render
from .models import Book,Author
from relationship_app.templates import library_detail.html
from relationship_app.templates import list_books.html

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

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
class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Automatically log in the user after registration
        return super().form_valid(form)

    



























