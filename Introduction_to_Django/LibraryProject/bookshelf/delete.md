# Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(id=new_book.id)
book.delete()

# Confirm deletion by retrieving all books
remaining_books = Book.objects.all()
