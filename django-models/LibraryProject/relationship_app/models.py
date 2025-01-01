from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=50)  # Renamed 'author' to 'name' for clarity
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Fixed 'related_name'
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='libraries')  # Fixed 'related_name'
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')  # Fixed 'related_name'
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Meta:
    permissions = [
        ("can_add_book", "Can add a book"),
        ("can_change_book", "Can change a book"),
        ("can_delete_book", "Can delete a book"),
    ]
    