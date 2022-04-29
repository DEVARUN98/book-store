import django_filters
from bookstoreapp.models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies"]