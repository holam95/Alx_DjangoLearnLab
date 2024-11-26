## Create Operation
```python
from bookshelf.models import Book

# Create a new Book instance
new_book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)

# Expected Output:
# Book instance created with ID: <new_book.id> and details as follows:
# Title: 1984
# Author: George Orwell
# Published Year: 1949
print(new_book)  # Should display the book’s title






# Retrieve the book by ID
retrieved_book = Book.objects.get(id=new_book.id)

# Expected Output:
# Retrieved Book details:
# Title: 1984
# Author: George Orwell
# Published Year: 1949



# Retrieve the book instance
book_to_update = Book.objects.get(id=new_book.id)

# Update the title and save
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Expected Output:
# Book title updated to: Nineteen Eighty-Four




# Retrieve and delete the book
book_to_delete = Book.objects.get(id=new_book.id)
book_to_delete.delete()

# Confirm deletion by retrieving all books
remaining_books = Book.objects.all()

# Expected Output:
# Confirmation of deletion:
# All books in database: [] (should be empty if only one book was created and deleted)
