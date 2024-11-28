from django.urls import path
from . views import BookListView
frfom django.views.generic.list import ListView

urlpatterns = [path('Book/', BookListView.as_view()),]
