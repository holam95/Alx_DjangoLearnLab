from django.db import models

# Create your models here.

class Author(models.Model):
    author = models.CharField()

class Book(models.Model):
    title = CharField()
    author = ForeignKey(Author, on_delete = models.CASCADE, name = 'books')

class Library(models.Model):
    name = CharField()
    books = ManyToManyField(Book, name = 'library')

class Librarian(models.Model):
    name = CharField()
    library = OneToOneField(Library , on_delete = models.CASCADE, name = 'librarian')
