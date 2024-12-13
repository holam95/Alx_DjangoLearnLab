from django.shortcuts import render
from .utils import role_required

@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})