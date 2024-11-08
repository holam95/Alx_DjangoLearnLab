# Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
from bookshelf.models import Book

# Retrieve the book instance
book_to_update = Book.objects.get(id=new_book.id)

# Update the title and save
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Expected Output:
# Book title updated to: Nineteen Eighty-Four
