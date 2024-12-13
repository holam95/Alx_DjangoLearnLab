from django.shortcuts import render
from relationship_app.utils import role_required  # Import the decorator

@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})