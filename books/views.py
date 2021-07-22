from django.shortcuts import render
from books.models import Book, Category
from django.views.generic.list import ListView


def index(request):
    return render(request, 'books/index.html')


def book_page(request):
    return render(request, 'books/book-page.html')


class CatalogListView(ListView):
    model = Book
    template_name = 'books/catalog.html'
    extra_context = {
        'title': 'Booksharing - Каталог книг',
        'categories': Category.objects.all()
    }

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Book.objects.all() if not category_id else Book.objects.filter(category_id=category_id)
