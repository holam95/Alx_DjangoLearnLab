from django.shortcuts import render
from .utils import role_required

@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})