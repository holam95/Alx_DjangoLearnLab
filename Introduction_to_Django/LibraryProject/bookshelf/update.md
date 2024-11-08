# Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(id=new_book.id)

# Update the title and save
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Book title updated to: Nineteen Eighty-Four
