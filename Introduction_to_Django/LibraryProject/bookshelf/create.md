from bookshelf.models import Book

# Create a new Book instance
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# Book instance created with ID: <new_book.id> and details as follows:
# title: 1984
# author: George Orwell
# publication_year: 1949
