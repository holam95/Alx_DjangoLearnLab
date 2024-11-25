from django.db import models

# Create your models here.

class Author(models.Model):
    author = models.CharField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = CharField()
    author = ForeignKey(Author, on_delete = models.CASCADE, name = 'books')
    def __str__(self):
        return self.title

class Library(models.Model):
    name = CharField()
    books = ManyToManyField(Book, name = 'library')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = CharField()
    library = OneToOneField(Library , on_delete = models.CASCADE, name = 'librarian')

    def __str__(self):
        return self.name
