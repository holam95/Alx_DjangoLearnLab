from django.contrib import admin

# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Specify which fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality
    search_fields = ('title', 'author')

    # Add filters for specific fields
    list_filter = ('author', 'publication_year')

# Register the Book model with custom admin configurations
admin.site.register(Book, BookAdmin)
