from django.shortcuts import render
from .models import Book,Author
from relationship_app.templates import library_detail.html
from relationship_app.templates import list_books.html
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




    



























