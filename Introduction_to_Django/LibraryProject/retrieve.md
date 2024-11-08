# Command: Retrieve and display all attributes of the book you just created.
from bookshelf.models import Book

# Retrieve the book by ID (replace <new_book.id> with the actual ID if known)
retrieved_book = Book.objects.get(id=new_book.id)

# Expected Output:
# Retrieved Book details:
# title: 1984
# author: George Orwell
# publication_year: 1949
