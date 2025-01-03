from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model
        fields = ['title', 'author', 'publication_year']  # Include the new field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_year': 'Publication Year',
        }