from django.shortcuts import render
from .models import Book,Author
# Create your views here.
def book_list(request):
    books = Book.objects.all
    context = {books:author)

    return render(request, "relationship_app/list_books.html", Book.objects.all())

from django.views.generic import ListView

class BookListiListView(ListView):
    model = Book
    



























