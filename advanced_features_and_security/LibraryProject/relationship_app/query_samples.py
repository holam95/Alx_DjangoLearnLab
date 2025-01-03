from relationship_app.models import Author, Book, Library


def query_books_by_author(author_name):

    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):

    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(library=library_name)
    librarian = Librarian.objects.get(library=library_name)
    return librarian
