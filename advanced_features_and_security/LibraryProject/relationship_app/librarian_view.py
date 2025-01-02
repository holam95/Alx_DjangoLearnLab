from django.shortcuts import render
from .utils import role_required

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})