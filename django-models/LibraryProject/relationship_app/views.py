from django.shortcuts import render
from .models import Book,Author
# Create your views here.
def book_list(request):
    books = Book.objects.all
    context = {books:author)

    return render(request, "books/book_list.html", context)

from django.views.generic import ListView

class BookListiListView(ListView):
    model = Book
    



























