from django.shortcuts import render


def index(request):
    return render(request, 'books/index.html')


def catalog(request):
    return render(request, 'books/catalog.html')


def book_page(request):
    return render(request, 'books/book-page.html')
