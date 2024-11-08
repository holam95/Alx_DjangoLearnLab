# Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
from bookshelf.models import Book

# Retrieve and delete the book
book_to_delete = Book.objects.get(id=new_book.id)
book_to_delete.delete()

# Confirm deletion by retrieving all books
remaining_books = Book.objects.all()
